import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set API keys from environment variables
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# Get API base URL from environment variable or default to localhost
API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")

# Set up the Streamlit app
st.set_page_config(page_title="AI Content Generation Platform", page_icon="🤖")
st.title("AI Content Generation Platform")
st.markdown("""
**Professional AI-Powered Writing Assistant**

This enterprise-grade application leverages advanced language models to generate high-quality essays and poetry. 
Built on LangChain architecture with OpenAI GPT-3.5-turbo and Ollama Llama2 integration for scalable content creation.

*Ideal for content creators, educators, researchers, and businesses requiring automated writing solutions.*
""")

def get_openai_response(input_text):
    url = f"{API_BASE_URL}/essay/invoke"
    payload = {"input": {"topic": input_text}}
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raise exception for non-200 status codes
        return response
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to connect to the API: {str(e)}")
        return None

def get_poem_response(input_text):
    url = f"{API_BASE_URL}/poem/invoke"
    payload = {"input": {"topic": input_text}}
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to connect to the API: {str(e)}")
        return None

# Input fields with placeholders
essay_input = st.text_input("Enter a topic for an essay:", placeholder="e.g., Artificial Intelligence")
poem_input = st.text_input("Enter a topic for a poem:", placeholder="e.g., Nature")

# Buttons to trigger API calls
if st.button("Generate Essay"):
    if essay_input:
        with st.spinner("Getting essay from OpenAI..."):
            response = get_openai_response(essay_input)
            if response:
                if response.status_code == 200:
                    data = response.json()
                    output = data.get("output")
                    if output:
                        st.success("Essay generated successfully!")
                        st.write("**Essay from OpenAI:**")
                        st.write(output)
                    else:
                        st.error("No output found in the response.")
                else:
                    st.error(f"Error: {response.status_code} - {response.text}")
    else:
        st.warning("Please enter a topic for the essay.")

if st.button("Generate Poem"):
    if poem_input:
        with st.spinner("Getting poem from Ollama..."):
            response = get_poem_response(poem_input)
            if response:
                if response.status_code == 200:
                    data = response.json()
                    output = data.get("output")
                    if output:
                        st.success("Poem generated successfully!")
                        st.write("**Poem from Ollama:**")
                        st.write(output)
                    else:
                        st.error("No output found in the response.")
                else:
                    st.error(f"Error: {response.status_code} - {response.text}")
    else:
        st.warning("Please enter a topic for the poem.")