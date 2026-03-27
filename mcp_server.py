from fastmcp import FastMCP
import requests
from bs4 import BeautifulSoup

mcp = FastMCP("website-qa-server")

@mcp.tool()
def scrape_website(url: str) -> str:
    """Fetches and returns the text content of a website given its URL."""
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, timeout=15)
    soup = BeautifulSoup(response.text, "html.parser")
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()
    text = soup.get_text(separator=" ", strip=True)
    return text[:12000]

if __name__ == "__main__":
    mcp.run(transport="sse", host="0.0.0.0", port=8080)
