
from fastapi import APIRouter

from baishitong.api.v1 import demo, question_and_answer, user

api_router = APIRouter()
api_router.include_router(demo.router, tags=["demo"])
api_router.include_router(question_and_answer.router, tags=["Q&A"])
api_router.include_router(user.router, tags=["user"])
