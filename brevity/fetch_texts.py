import requests
from bs4 import BeautifulSoup

def fetch_text_from_url(url: str) -> str:
    """Fetch and extract readable text from a URL"""
    try:
        res = requests.get(url, timeout=5)
        soup = BeautifulSoup(res.text, "html.parser")

        # Get only visible text (basic approach)
        paragraphs = soup.find_all("p")
        content = " ".join(p.get_text() for p in paragraphs)
        return content.strip()
    
    except Exception as e:
        return f"Error fetching URL: {e}"