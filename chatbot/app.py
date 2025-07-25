# Import ChatOpenAI for interacting with OpenAI chat models
from langchain_openai import ChatOpenAI
# Import ChatPromptTemplate for creating prompt templates
from langchain_core.prompts import ChatPromptTemplate
# Import StrOutputParser for parsing string outputs from the model
from langchain_core.output_parsers import StrOutputParser


import os
import streamlit as st
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set API keys from environment variables
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# Create a chat prompt template with system and user messages
prompt = ChatPromptTemplate.from_messages(
    [
        # System message sets the assistant's behavior
        ("system", "You are a helpful assistant. Please provide responses to user queries."),
        # User message template, {text} will be replaced with actual user input
        ("user", "Question: {text}"),
    ]
)

# Streamlit UI setup
st.set_page_config(page_title="LangChain Chatbot", page_icon=":robot_face:")
st.title("LangChain Chatbot")
st.write("Ask me anything!")

# Initialize the language model
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

# Output parser for the model's response
output_parser = StrOutputParser()

# Chain: prompt -> LLM -> output parser
chat_chain = prompt | llm | output_parser

# User input
input_text = st.text_input("Enter your question:")
if input_text:
    response = chat_chain.invoke({"text": input_text})
    st.write("Response:", response)