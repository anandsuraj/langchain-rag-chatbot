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

# Load the .env file
load_dotenv()

# Set API keys from environment variables
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

app = FastAPI(
    title="LangServe Example API",
    version="1.0",
    description="Endpoints powered by OpenAI and Ollama via LangServe",
)

parser = StrOutputParser()

# Define input models
class EssayRequest(BaseModel):
    topic: str

class PoemRequest(BaseModel):
    topic: str

# OpenAI endpoint: essay
essay_prompt = ChatPromptTemplate.from_template(
    "Write me an essay about: {topic} in exactly 100 words."
)

essay_chain = essay_prompt | ChatOpenAI(model="gpt-3.5-turbo", callbacks=[LangChainTracer()]) | parser

add_routes(
    app,
    essay_chain,
    path="/essay",
    input_type=EssayRequest,
    config_keys=[],  
)

# Ollama endpoint: poem
poem_prompt = ChatPromptTemplate.from_template(
    "Write me a poem about: {topic} for a 20-year-old girl."
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