import os
import json
import re
from pathlib import Path
import requests
import google.generativeai as genai
from PIL import Image
from io import BytesIO

# --- CONFIGURATION ---
input_dir = 'discourse_json'
output_dir = 'discourse_md'
os.makedirs(output_dir, exist_ok=True)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("Set your GEMINI_API_KEY environment variable.")

genai.configure(api_key=GEMINI_API_KEY)

def is_emoji_image(url):
    # Heuristic: skip images from emoji CDN or unicode emoji
    return "emoji" in url or "twemoji" in url or re.search(r"/emoji/|/emojis/", url)

def get_image_bytes(image_url):
    try:
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        return response.content
    except Exception as e:
        print(f"Failed to fetch image {image_url}: {e}")
        return None

def get_gemini_image_description(image_url):
    image_bytes = get_image_bytes(image_url)
    if not image_bytes:
        return "Image"
    try:
        image = Image.open(BytesIO(image_bytes))
        model = genai.GenerativeModel('gemini-2.0-flash')
        prompt = "Describe this image for use as alt text in Markdown."
        result = model.generate_content([prompt, image])
        desc = result.text.strip()
        # Gemini may return empty or generic responses, fallback:
        if not desc or "image" in desc.lower():
            return "Image"
        return desc
    except Exception as e:
        print(f"Gemini API error for {image_url}: {e}")
        return "Image"

def post_to_markdown(post):
    md = []
    # Title
    title = post.get('topic_title', 'No Title')
    md.append(f'# {title}')
    # Add the original post URL if available
    post_url = post.get('url')
    if not post_url:
        topic_id = post.get('topic_id')
        post_number = post.get('post_number')
        if topic_id and post_number:
            post_url = f"https://discourse.onlinedegree.iitm.ac.in/t/{topic_id}/{post_number}"
    if post_url:
        md.append(f'[Original Post]({post_url})')
    # Content
    content = post.get('content') or post.get('cooked') or ''
    md.append(content)
    # Find all image links in content (Markdown or HTML)
    image_urls = set()
    image_urls.update(re.findall(r'!\[.*?\]\((.*?)\)', content))
    image_urls.update(re.findall(r'<img [^>]*src="([^"]+)"', content))
    image_urls.update(post.get('image_urls', []))
    for img_url in image_urls:
        if not is_emoji_image(img_url):
            desc = get_gemini_image_description(img_url)
            md.append(f'![{desc}]({img_url})')
    # URL links
    links = post.get('url_links', [])
    for link in links:
        md.append(f'[Link]({link})')
    return '\n\n'.join(md)

def main():
    for filename in os.listdir(input_dir):
        if filename.endswith('.json'):
            filepath = os.path.join(input_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                try:
                    posts = json.load(f)
                    if isinstance(posts, dict) and 'post_stream' in posts:
                        posts = posts['post_stream'].get('posts', [])
                    for i, post in enumerate(posts):
                        md_text = post_to_markdown(post)
                        md_filename = f'{Path(filename).stem}_post_{i+1}.md'
                        md_filepath = os.path.join(output_dir, md_filename)
                        with open(md_filepath, 'w', encoding='utf-8') as mdf:
                            mdf.write(md_text)
                except Exception as e:
                    print(f'Error processing {filename}: {e}')
    print(f"Markdown files created in '{output_dir}' directory.")

if __name__ == "__main__":
    main()
