from fastapi import APIRouter

from candidate_assessment import utils

router = APIRouter()

@router.get("/")
async def root():
    return {
        "message": "Hello!"
    }

@router.get("/get-questions-level-of-sufficiency")
async def get_questions_level_of_sufficiency():
    return utils.Questions.get_level_of_sufficiency()
