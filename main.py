from fastapi import FastAPI
from routers.ai_router import router as ai_router

app = FastAPI(
    title="AI Backend API",
    description="Professional AI backend built with FastAPI",
    version="1.0.0"
)

app.include_router(ai_router)

@app.get("/")
def health_check():
    return {"status": "ok"}
