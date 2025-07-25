# Import necessary classes from LangChain and other libraries.
from langchain_ollama.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import os
import streamlit as st
from dotenv import load_dotenv

# Load environment variables from a .env file.
load_dotenv()

# Optional: LangSmith tracing
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# Prompt definition
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please provide responses to user queries."),
        ("user", "Question: {text}"),
    ]
)

# Streamlit UI configuration
st.set_page_config(page_title="LangChain Chatbot with Ollama", page_icon=":robot_face:")
st.title("LangChain Chatbot with Ollama")
st.write("Ask me anything! I'm running on a local Llama2 model.")

# LLM and chain initialization
llm = ChatOllama(model="llama2", temperature=2)
output_parser = StrOutputParser()
chat_chain = prompt | llm | output_parser

# User input handling
input_text = st.text_input("Enter your question:")

if input_text:
    with st.spinner("Thinking..."):
        st.write_stream(chat_chain.stream({"text": input_text}))