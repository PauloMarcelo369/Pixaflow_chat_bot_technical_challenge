from fastapi import APIRouter, Depends
from sqlmodel import Session
from infra.db.engine import get_session
from infra.repositories.fruit_repository import FruitRepository
from domain.services.fruit_service import FruitService
from domain.intents.fruit_intent_handler import FruitIntentHandler
from domain.intents.gemini_service import GeminiService

router = APIRouter()
gemini = GeminiService()

@router.post("/chat")
def chat(user_question : str, session : Session = Depends(get_session)):
    repo = FruitRepository(session)
    service = FruitService(repo)
    handler = FruitIntentHandler(service)

    gemini_json = gemini.get_intent(user_question)

    response_text = handler.handle(intent=gemini_json["intent"], params=gemini_json["parameters"])

    return {"response": response_text}