import os
import asyncio
import streamlit as st
from fastmcp import Client
import google.generativeai as genai

st.set_page_config(page_title="Website Q&A Assistant", page_icon="🌐", layout="centered")
st.title("🌐 Website Q&A Assistant")
st.write("Enter a website URL, then ask a question about its content.")

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error("GEMINI_API_KEY is not set. Add it before running the app.")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")

MCP_SERVER_URL = "https://mcp-server-490177762521.us-central1.run.app/sse"

async def scrape_via_mcp(url: str) -> str:
    async with Client(MCP_SERVER_URL) as client:
        result = await client.call_tool("scrape_website", {"url": url})
        return result.content[0].text

def fetch_website_text(url: str) -> str:
    return asyncio.run(scrape_via_mcp(url))

url = st.text_input("Website URL", placeholder="https://example.com")
question = st.text_area("Your question", placeholder="What is this website about?")

if st.button("Get Answer"):
    if not url.strip():
        st.warning("Please enter a website URL.")
        st.stop()
    if not question.strip():
        st.warning("Please enter a question.")
        st.stop()
    try:
        with st.spinner("Fetching website content via MCP..."):
            website_text = fetch_website_text(url)
        prompt = f"""
You are a helpful AI assistant.
Use only the website content below to answer the user's question.
If the answer is not clearly present in the content, say:
"I could not find that information on the provided website."

Website content:
{website_text}

User question:
{question}
"""
        with st.spinner("Generating answer..."):
            result = model.generate_content(prompt)

        st.subheader("Answer")
        st.write(result.text)

        with st.expander("Show extracted website content"):
            st.write(website_text)

    except Exception as e:
        st.error(f"Something went wrong: {e}")
