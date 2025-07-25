
# LangChain Content Generation API

A FastAPI-based API powered by LangChain, integrating OpenAI and Ollama to generate essays and poems. Includes a Streamlit web interface for seamless interaction with the API endpoints.

## Features

- **Essay API**: `/essay/invoke`  
  Generates customizable essays on any topic using OpenAI's GPT-3.5-turbo. Default word count: 100 words (adjustable).

- **Poem API**: `/poem/invoke`  
  Creates tailored poems on any topic using Ollama (Llama2), with customizable audience targeting (default: general).

- **Streamlit Client**  
  A user-friendly web interface for testing and prototyping API interactions.

## Project Structure

### `api/`
- **Purpose**: Hosts the FastAPI backend and API logic.
- **Files**:
  - `app.py`: Core FastAPI app exposing `/essay/invoke` and `/poem/invoke` endpoints.
  - `client.py`: Streamlit-based client for interactive API testing.
- **Notes**: Extensible design for adding new endpoints or models. Securely handles API keys via `.env`.

### `chatbot/`
- **Purpose**: Contains Streamlit apps for conversational AI demos.
- **Files**:
  - `app.py`: Streamlit interface for prototyping and prompt engineering.
- **Notes**: Customizable for additional models, prompts, or features like chat history.

## Prerequisites

- Python 3.8+
- API keys for [OpenAI](https://platform.openai.com/account/api-keys) and [LangChain](https://smith.langchain.com/)
- [Ollama](https://ollama.ai/) installed locally with the Llama2 model (`ollama pull llama2`)

## Quick Start

1. **Clone the Repository**  
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**  
   Create a `.env` file in the project root:  
   ```plaintext
   LANGCHAIN_API_KEY=<your-langchain-api-key>
   OPENAI_API_KEY=<your-openai-api-key>
   LANGCHAIN_PROJECT=langchain_project
   LANGCHAIN_TRACING_V2=true
   ```

4. **Run the FastAPI Server**  
   ```bash
   uvicorn api.app:app --host 127.0.0.1 --port 8000 --reload
   ```

5. **Access API Documentation**  
   Visit [http://localhost:8000/docs](http://localhost:8000/docs) to explore and test endpoints.

6. **Launch Streamlit Client**  
   ```bash
   streamlit run api/client.py
   ```

## Usage Examples

- **Essay API** (POST to `/essay/invoke`)  
  ```json
  {
    "topic": "The Impact of Renewable Energy",
    "word_count": 150
  }
  ```

- **Poem API** (POST to `/poem/invoke`)  
  ```json
  {
    "topic": "Autumn Leaves",
    "audience": "young adult"
  }
  ```

- **Streamlit Interface**  
  Open [http://localhost:8501](http://localhost:8501) to input topics and audience details via a web form.

## Troubleshooting

- **API Key Errors**: Ensure `.env` is correctly configured and keys are valid.
- **Ollama Issues**: Verify Ollama is running locally (`ollama run llama2`) before starting the API.
- **Port Conflicts**: Change the port in the `uvicorn` command if `8000` is in use.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.