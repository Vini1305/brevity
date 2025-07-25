import requests
from readability import Document

def fetch_text_from_url(url: str) -> str:
    """Fetch and extract readable text from a URL"""
    try:
        res = requests.get(url, timeout=5)
        content = Document(res.text).summary()  # cleaner content
        return content.strip()
    
    except Exception as e:
        return f"Error fetching URL: {e}"