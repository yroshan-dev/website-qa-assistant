import os
import requests
import streamlit as st
from bs4 import BeautifulSoup
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


def fetch_website_text(url: str) -> str:
    """Fetch website HTML and extract readable text."""
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers, timeout=15)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    text = soup.get_text(separator=" ", strip=True)
    return text[:12000]  # keep prompt size manageable


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
        with st.spinner("Fetching website content..."):
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

    except requests.exceptions.RequestException as e:
        st.error(f"Failed to fetch the website: {e}")
    except Exception as e:
        st.error(f"Something went wrong: {e}")