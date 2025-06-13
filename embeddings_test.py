import numpy as np

data = np.load("all_embeddings.npz")
texts = data["texts"]
sources = data["sources"]

for idx, (text, source) in enumerate(zip(texts, sources)):
    # Convert to string if needed
    if not isinstance(text, str):
        text = str(text)
    if not isinstance(source, str):
        source = str(source)
    # Check for the Docker/Podman page
    if "docker" in text.lower() or "podman" in text.lower() or "docker" in source.lower():
        print(f"Index: {idx}")
        print(f"Source: {source}")
        print(f"Text: {text[:250]}...\n")
