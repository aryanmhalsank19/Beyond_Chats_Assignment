import praw
from urllib.parse import urlparse

# Configure with your Reddit app credentials (get from https://www.reddit.com/prefs/apps)
reddit = praw.Reddit(
    client_id="Zz0gjhlUg0UCUJM2z-KSXA",
    client_secret="DEAzKUN2FPlRE0V43zkxcQaguYvOzw",
    user_agent="PersonaGenScript by u/BeyondChatsPersona"
)

def extract_username(url: str) -> str:
    """Extracts Reddit username from a profile URL."""
    parsed = urlparse(url)
    parts = parsed.path.strip("/").split("/")
    return parts[1] if len(parts) >= 2 and parts[0] == 'user' else None

def scrape_reddit_user(url: str):
    """Scrapes recent submissions and comments of the Reddit user."""
    username = extract_username(url)
    if not username:
        raise ValueError("Invalid Reddit URL format")

    redditor = reddit.redditor(username)

    posts = [
        {"id": post.id, "text": f"{post.title}\n{post.selftext}"}
        for post in redditor.submissions.new(limit=100)
        if post.selftext or post.title
    ]

    comments = [
        {"id": comment.id, "text": comment.body}
        for comment in redditor.comments.new(limit=200)
        if comment.body
    ]

    return username, {"posts": posts, "comments": comments}
