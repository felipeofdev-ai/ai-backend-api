🚀 AI Backend API

A production-ready AI backend API built with FastAPI and Python, designed for scalable AI-powered applications.

This project demonstrates clean architecture, service abstraction, environment-based configuration, centralized logging, and real-world integration with Large Language Models (LLMs).

🧠 Features

REST API for AI-powered text generation

Clean separation of concerns (routers & services)

Centralized environment configuration using config/settings.py

Centralized structured logging using config/logger.py

Ready for testing, scaling, and deployment

Interactive API documentation (Swagger UI)

🏗️ Project Structure
ai-backend-api/
│
├── main.py
├── requirements.txt
├── .env.example
│
├── services/
│   └── llm_service.py
│
├── routers/
│   └── ai_router.py
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   └── logger.py
│
├── tests/
│   ├── __init__.py
│   ├── test_health.py
│   └── test_ai_endpoint.py
│
├── Dockerfile
└── .dockerignore

🛠️ Technologies

Python 3.10+

FastAPI

OpenAI API (LLMs)

Pydantic

Uvicorn

python-dotenv

Docker

⚙️ Setup
1️⃣ Clone the repository
git clone https://github.com/your-username/ai-backend-api.git
cd ai-backend-api

2️⃣ Create a virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Configure environment variables

Create a .env file based on .env.example:

OPENAI_API_KEY=your_api_key_here
APP_PORT=8000

▶️ Running the API
Local (development)
uvicorn main:app --reload


API Base URL: http://127.0.0.1:8000

Swagger UI: http://127.0.0.1:8000/docs

Docker (production-ready)
# Build Docker image
docker build -t ai-backend-api .

# Run container
docker run -d -p 8000:8000 --env-file .env ai-backend-api

📡 API Endpoints
POST /ai/generate

Generate a response using an LLM.

Request

{
  "prompt": "Explain FastAPI in simple terms"
}


Response

{
  "response": "FastAPI is a modern Python web framework..."
}

📝 Logging & Monitoring

Centralized structured logging using config/logger.py

Logs include timestamps, levels, module names, and messages

Compatible with Docker and cloud monitoring

🧪 Next Improvements (Roadmap)

Unit and integration tests

Authentication (JWT / API Key)

Rate limiting

Caching (Redis)

Docker & Cloud deployment

📄 License

MIT License
