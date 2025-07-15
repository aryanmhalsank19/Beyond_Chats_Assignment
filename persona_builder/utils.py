import re
from nltk.tokenize import sent_tokenize
from itertools import islice

def clean_text(text: str) -> str:
    """Basic cleaning: remove links, special chars, extra whitespace."""
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^\x00-\x7F]+", " ", text)
    return text.strip()

def chunk_text(texts, chunk_size=1000):
    """Tokenizes and chunks user content into digestible LLM inputs."""
    combined = "\n".join(texts)
    sentences = sent_tokenize(combined)
    chunks = []
    iterator = iter(sentences)
    while True:
        chunk = list(islice(iterator, chunk_size))
        if not chunk:
            break
        chunks.append(" ".join(chunk))
    return chunks

def clean_and_chunk(data):
    """Cleans and chunks post/comment text into batches."""
    texts = [clean_text(item["text"]) for item in data["posts"] + data["comments"]]
    return chunk_text(texts, chunk_size=10)
