from typing import List

from pydantic import BaseModel

from candidate_assessment import config


class Question(BaseModel):
    text: str
    options: List[str] = config.QuestionAnswers.level_of_sufficiency.value


class UserResponse(BaseModel):
    user_id: str
    answers: List[str]
