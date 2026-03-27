from fastmcp import FastMCP
import requests
from bs4 import BeautifulSoup

mcp = FastMCP("website-qa-server")

@mcp.tool()
def scrape_website(url: str) -> str:
    """Fetches and returns the text content of a website given its URL."""
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")
    return " ".join([p.text for p in soup.find_all("p")])

if __name__ == "__main__":
    mcp.run(transport="sse", host="0.0.0.0", port=8080)
