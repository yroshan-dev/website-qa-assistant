# Website Q&A Assistant

An AI-powered Website Question & Answer Assistant built using Google Gemini, FastMCP, Python, and Streamlit.

The application allows users to provide a website URL and ask questions about its content in natural language. Website content is retrieved through a FastMCP server, processed, and then analyzed by Google's Gemini model to generate accurate responses.

---

## Features

- Ask questions about any public website
- Website retrieval through FastMCP
- AI-powered answers using Google Gemini
- Streamlit-based user interface
- Deployable on Google Cloud Run
- Website content inspection for transparency

---

## Architecture

User
→ Streamlit Frontend
→ FastMCP Client
→ FastMCP Server
→ scrape_website Tool
→ Website Content Retrieval
→ Google Gemini
→ Generated Answer

---

## Technologies Used

- Google Gemini API
- FastMCP
- Python
- Streamlit
- BeautifulSoup
- Requests
- Google Cloud Run

---

## Example Use Cases

- University website analysis
- Scholarship information lookup
- Technical documentation summarization
- Organization and business research
- General website content exploration

---

## Project Structure

app.py
- Streamlit frontend application

mcp_server.py
- FastMCP server implementation

requirements.txt
- Python dependencies

Dockerfile
- Application containerization

Dockerfile.mcp
- MCP server containerization

---

## How It Works

1. User enters a website URL.
2. User asks a question.
3. FastMCP retrieves website content.
4. Content is cleaned using BeautifulSoup.
5. Gemini analyzes the content.
6. A natural language answer is generated.

---

## Author

Yelaka Roshan Kumar

GitHub:
https://github.com/yroshan-dev

LinkedIn:
https://www.linkedin.com/in/roshan-y
