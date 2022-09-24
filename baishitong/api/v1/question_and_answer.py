from fastapi import APIRouter

router = APIRouter()


@router.post("/question")
def add_question():
    pass


@router.get("/questions")
def list_requstion():
    pass
