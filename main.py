# 📁 Beyond_Chats/main.py

import argparse
from persona_builder.scraper import scrape_reddit_user
from persona_builder.utils import clean_and_chunk
from persona_builder.llm_persona import generate_persona
from persona_builder.formatter import format_and_save_persona

def main():
    parser = argparse.ArgumentParser(description="Generate a Reddit user persona using a hosted LLM via HuggingFace API.")
    parser.add_argument('--url', required=True, help='Reddit profile URL (e.g. https://www.reddit.com/user/kojied/)')
    parser.add_argument('--limit', type=int, default=None, help='Limit number of text chunks for faster testing')
    args = parser.parse_args()

    # Step 1: Scrape Reddit content
    try:
        username, data = scrape_reddit_user(args.url)
    except Exception as e:
        print(f"[ERROR] Failed to scrape user: {e}")
        return

    if not data['posts'] and not data['comments']:
        print(f"[INFO] No data found for user: {username}")
        return

    # Step 2: Clean and chunk text
    chunks = clean_and_chunk(data)
    if not chunks:
        print("[INFO] Not enough content to analyze.")
        return

    if args.limit:
        chunks = chunks[:args.limit]

    # Step 3: Generate traits using LLM
    print(f"[INFO] Generating persona for u/{username}...")
    persona = generate_persona(username, chunks)

    # Step 4: Debug output (optional)
    print("[DEBUG] Sample traits returned by model:")
    for i, trait in enumerate(persona, 1):
        print(f"Trait {i}: {trait}")

    # Step 5: Save to file
    format_and_save_persona(username, persona)

if __name__ == '__main__':
    main()
