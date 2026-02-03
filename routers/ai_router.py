from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.llm_service import LLMService

router = APIRouter(prefix="/ai", tags=["AI"])

llm_service = LLMService()

class PromptRequest(BaseModel):
    prompt: str

@router.post("/chat")
def chat(request: PromptRequest):
    try:
        response = llm_service.generate_response(request.prompt)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
