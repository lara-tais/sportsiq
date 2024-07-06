from pydantic import BaseModel
from typing import List, Dict, Optional

class QuestionBase(BaseModel):
    title: str
    answers: Dict[str, str]
    correct_answer: str

class QuestionCreate(QuestionBase):
    quiz_id: int

class Question(QuestionBase):
    id: int
    quiz_id: int

    class Config:
        orm_mode = True

class QuizBase(BaseModel):
    sport: str
    title: str
    level: str

class QuizCreate(QuizBase):
    pass

class Quiz(QuizBase):
    id: int
    questions: List[Question] = []

    class Config:
        orm_mode = True

class ScoreResult(BaseModel):
    total_questions: int
    correct_answers: int
    score: float
