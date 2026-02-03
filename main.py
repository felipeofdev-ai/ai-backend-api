from fastapi import FastAPI
from routers.ai_router import router as ai_router
from config.settings import settings

app = FastAPI(
    title=settings.app_name,
    description="Professional AI backend built with FastAPI",
    version=settings.version
)

app.include_router(ai_router)

@app.get("/")
def root():
    return {"message": f"{settings.app_name} is running", "version": settings.version}

@app.get("/health")
def health_check():
    return {"status": "ok"}
