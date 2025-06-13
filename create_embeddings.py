import os
import numpy as np
from tqdm import tqdm
import google.generativeai as genai
from google.api_core import retry
import re

# --- CONFIGURATION ---
dirs = ["discourse_md", "tds_pages_md"]
chunk_size = 1000  # Increased to 1000 characters
chunk_overlap = 50
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
EMBEDDING_MODEL = "text-embedding-004"  # Official Gemini free embedding model
COST_PER_1K_TOKENS = 0.0001  # Gemini embedding cost (verify current pricing)

if not GEMINI_API_KEY:
    raise ValueError("Set GEMINI_API_KEY environment variable")

genai.configure(api_key=GEMINI_API_KEY)

# --- TEXT SPLITTING ---
class Document:
    def __init__(self, page_content, metadata):
        self.page_content = page_content
        self.metadata = metadata

class RecursiveCharacterTextSplitter:
    def __init__(self, chunk_size=1000, chunk_overlap=50):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split_text(self, text):
        chunks = []
        start = 0
        while start < len(text):
            end = min(start + self.chunk_size, len(text))
            chunks.append(text[start:end])
            start += self.chunk_size - self.chunk_overlap
        return chunks

# --- EMBEDDING WITH RETRIES ---
@retry.Retry(initial=1, maximum=3, deadline=30)  # Auto-retry on rate limits
def get_embedding(text):
    return genai.embed_content(
        model=EMBEDDING_MODEL,
        content=text,
        task_type="SEMANTIC_SIMILARITY"
    )["embedding"]

# --- MAIN PROCESS ---
def main():
    # 1. Chunk files
    print("🔄 Chunking markdown files...")
    splitter = RecursiveCharacterTextSplitter(chunk_size, chunk_overlap)
    documents = []
    
    for dir_path in dirs:
        if not os.path.exists(dir_path):
            print(f"⚠️ Missing directory: {dir_path}")
            continue
            
        for filename in os.listdir(dir_path):
            if not filename.endswith(".md"):
                continue
                
            filepath = os.path.join(dir_path, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
                chunks = splitter.split_text(content)
                print(f"📄 {filename}: Split into {len(chunks)} chunks")
                
                for i, chunk in enumerate(chunks):
                    metadata = {"source": f"{dir_path}/{filename}#chunk{i}"}
                    documents.append(Document(chunk, metadata))

    # 2. Calculate token estimates
    total_chunks = len(documents)
    tokens_per_chunk = int(chunk_size * 0.75)  # 0.75 tokens/char estimate
    total_tokens = total_chunks * tokens_per_chunk
    estimated_cost = (total_tokens / 1000) * COST_PER_1K_TOKENS
    
    print(f"\n📊 Statistics:")
    print(f"• Total chunks: {total_chunks}")
    print(f"• Tokens per chunk: ~{tokens_per_chunk}")
    print(f"• Estimated total tokens: {total_tokens:,}")
    print(f"• Estimated cost: ${estimated_cost:.5f}\n")

    # 3. Generate embeddings
    embeddings = []
    metadatas = []
    texts = []

    print("🔮 Generating embeddings...")
    for doc in tqdm(documents, desc="Processing chunks"):
        try:
            emb = np.array(get_embedding(doc.page_content), dtype=np.float32)
            embeddings.append(emb)
            metadatas.append(doc.metadata["source"])
            texts.append(doc.page_content)
        except Exception as e:
            print(f"\n⚠️ Failed on chunk {doc.metadata['source']}: {str(e)}")
            continue

    # 4. Save results
    embeddings = np.stack(embeddings)
    np.savez_compressed(
        "all_embeddings.npz",
        embeddings=embeddings,
        sources=np.array(metadatas),
        texts=np.array(texts)
    )
    print("\n✅ Done! Embeddings saved to all_embeddings.npz")
    print(f"Final embedding shape: {embeddings.shape}")

if __name__ == "__main__":
    main()
