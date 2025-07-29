
# RAG-Based Intelligent Q&A & Content Platform

An AI platform that combines multi-source knowledge retrieval with LLM-powered content generation. Acts as an intelligent assistant capable of answering questions, retrieving accurate information from diverse data sources, and generating context-aware content.

Built with FastAPI for APIs, Streamlit for UI, and LangChain for managing advanced LLM workflows, featuring integrated RAG pipelines for document-aware interactions.

Key Technologies: FastAPI • Streamlit • LangChain • OpenAI GPT-3.5 • Ollama Llama2 • Vector Databases

Use Cases: Multi-source chatbots, document-based Q&A, enterprise knowledge assistants, AI-driven content generation, educational and research tools

## Features

| Feature                   | Implementation                   | Purpose                                                |
| ------------------------- | -------------------------------- | ------------------------------------------------------ |
| **LLM-based Chatbot**     | FastAPI APIs + Streamlit UI      | Conversational interface with contextual understanding |
| **RAG Pipeline**          | Vector databases + LangChain     | Accurate document-based Q\&A with source context       |
| **Multi-source Agents**   | Wikipedia + JSON/Text/Web/PDF    | Pulls information from multiple data sources           |
| **Content Generation**    | LLM APIs (OpenAI, Llama2)        | Generates high-quality content and summaries           |
| **Scalable Architecture** | FastAPI backend + modular design | Flexible for enterprise or product integration         |

![API Client Demo](screenshots/api-client-demo.png)
*Professional web interface for generating essays and poems with AI*

## Project Structure

```
├── api/
│   ├── app.py          # FastAPI server with essay/poem endpoints
│   └── client.py       # Streamlit web interface
├── agents/
│   └── agents.ipynb    # Multi-source RAG agents with Wikipedia integration
├── rag/
│   ├── simplerag.ipynb # Basic RAG pipeline with vector database
│   ├── chain.ipynb     # Advanced RAG chain implementations
│   └── *.pdf, *.json   # Sample documents and data sources
├── chatbot/
│   └── app.py          # Experimental chatbot interface
├── requirements.txt    # Python dependencies
└── .env               # API keys (create this file)
```

**Key Components:**
- **API**: Production-ready FastAPI endpoints with web interface
- **Agents**: Advanced AI agents with multi-source data retrieval
- **RAG**: Retrieval-Augmented Generation experiments and implementations
- **Chatbot**: Interactive conversational AI prototypes

## Prerequisites

**Software Requirements:**
- Python 3.8+ (`python --version`)
- Git (optional, for cloning)

**API Keys Required:**
- [OpenAI API Key](https://platform.openai.com/account/api-keys) - ~$0.002 per essay, $5 free credit
- [LangChain API Key](https://smith.langchain.com/) - Free for monitoring
- [Ollama](https://ollama.ai/) - Free local AI model

## Quick Start

1. **Clone and Install**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   pip install -r requirements.txt
   ```

2. **Setup Environment**
   Create `.env` file:
   ```env
   LANGCHAIN_API_KEY=your-langchain-key
   OPENAI_API_KEY=your-openai-key
   LANGCHAIN_PROJECT=langchain_project
   LANGCHAIN_TRACING_V2=true
   ```

3. **Install Ollama (for poems)**
   ```bash
   # Download from https://ollama.ai/
   ollama pull llama2
   ```

4. **Run the Application**
   ```bash
   # Terminal 1: Start API server
   uvicorn api.app:app --reload
   
   # Terminal 2: Start web interface
   streamlit run api/client.py
   ```

5. **Access the App**
   - Web Interface: http://localhost:8501
   - API Documentation: http://localhost:8000/docs

## Usage

### Web Interface
Visit http://localhost:8501 and use the intuitive forms to generate content.

### API Endpoints

**Essay Generation:**
```bash
curl -X POST "http://localhost:8000/essay/invoke" \
  -H "Content-Type: application/json" \
  -d '{"topic": "Renewable Energy", "word_count": 150}'
```

**Poem Generation:**
```bash
curl -X POST "http://localhost:8000/poem/invoke" \
  -H "Content-Type: application/json" \
  -d '{"topic": "Autumn Leaves", "audience": "young adult"}'
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| **API Key Error** | Verify `.env` file format, check OpenAI credits, restart server |
| **Ollama Not Found** | Run `ollama serve` and `ollama pull llama2` |
| **Port in Use** | Use different ports: `--port 8001` or `--server.port 8502` |
| **Module Not Found** | Run `pip install -r requirements.txt` |

**Debug Steps:**
1. Check terminal logs for detailed errors
2. Verify you're in the correct directory
3. Test API endpoints at http://localhost:8000/docs

## Development

**Restart Checklist:**
- [ ] Python installed (`python --version`)
- [ ] API keys valid (check OpenAI billing)
- [ ] Ollama running (`ollama serve`)
- [ ] Dependencies installed (`pip install -r requirements.txt`)

**Extension Ideas:**
- Additional AI models (Claude, Gemini)
- User authentication and content saving
- Multiple writing styles and formats
- Batch processing capabilities

## License

MIT License - see [LICENSE](LICENSE) file for details.
