from fastapi import FastAPI
from routers.ai_router import router as ai_router
from config.settings import settings
from config.logger import logger  # <-- adiciona o logger centralizado

app = FastAPI(
    title=settings.app_name,
    description="Professional AI backend built with FastAPI",
    version=settings.version
)

app.include_router(ai_router)

@app.get("/")
def root():
    logger.info("Root endpoint accessed")  # log do acesso
    return {"message": f"{settings.app_name} is running", "version": settings.version}

@app.get("/health")
def health_check():
    logger.info("Health check endpoint accessed")  # log do health check
    return {"status": "ok"}
