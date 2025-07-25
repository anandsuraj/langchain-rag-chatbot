import os
from fastapi import FastAPI
from dotenv import load_dotenv
from pydantic import BaseModel

from langchain_openai import ChatOpenAI
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langserve import add_routes

from langchain.callbacks.tracers import LangChainTracer

# Load environment variables
load_dotenv()

# Configure environment variables for API keys and tracing
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# Initialize FastAPI application
app = FastAPI(
    title="LangServe Content Generation API",
    version="1.0",
    description="API for generating essays and poems using OpenAI and Ollama via LangServe",
)

# Initialize output parser
parser = StrOutputParser()

# Define input models
class EssayRequest(BaseModel):
    topic: str
    word_count: int = 100  # Optional parameter for flexibility

class PoemRequest(BaseModel):
    topic: str
    audience: str = "general"  # Optional parameter for audience customization

# OpenAI endpoint: Essay generation
essay_prompt = ChatPromptTemplate.from_template(
    "Write a well-structured essay on the topic '{topic}' in exactly {word_count} words. "
    "Ensure the essay is clear, concise, and engaging, with a logical flow including an introduction, body, and conclusion."
)

essay_chain = essay_prompt | ChatOpenAI(model="gpt-3.5-turbo", callbacks=[LangChainTracer()]) | parser

add_routes(
    app,
    essay_chain,
    path="/essay",
    input_type=EssayRequest,
    config_keys=[],
)

# Ollama endpoint: Poem generation
poem_prompt = ChatPromptTemplate.from_template(
    "Compose a creative and heartfelt poem on the topic '{topic}' tailored for a {audience} audience. "
    "Use vivid imagery and an appropriate tone to make the poem engaging and emotionally resonant."
)

poem_chain = poem_prompt | Ollama(model="llama2", callbacks=[LangChainTracer()]) | parser

add_routes(
    app,
    poem_chain,
    path="/poem",
    input_type=PoemRequest,
    config_keys=[],
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)