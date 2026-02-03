# AI Backend API

This project is a clean and scalable backend API built with FastAPI and
Generative AI. It exposes AI capabilities through REST endpoints, following
good backend architecture practices.

The goal is to demonstrate how to integrate LLMs into a backend service
with clear separation of concerns.

## Features

- REST API built with FastAPI
- AI-powered text generation endpoint
- AI-powered text summarization endpoint
- Clean project structure (routers, services)
- Environment-based configuration

## Technologies

- Python 3
- FastAPI
- OpenAI API
- Generative AI / LLMs
- Backend architecture best practices

## Project Structure
ai-backend-api/
│── README.md
│── requirements.txt
│── .env.example
│── main.py
│── services/
│ └── llm_service.py
│── routers/
│ └── ai_routes.py

## How to Run

Create a virtual environment and install dependencies:

```bash
pip install -r requirements.txt
Create a .env file based on .env.example and add your API key.

Run the API server:
uvicorn main:app --reload

Access the interactive API documentation at:
http://127.0.0.1:8000/docs

Purpose

Demonstrate backend API design

Integrate Generative AI into services

Build production-ready foundations

Author

Felipe Oliveira
Python Developer | Backend | Automation | Generative AI

