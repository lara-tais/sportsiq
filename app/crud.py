from sqlalchemy.orm import Session
from app.models import Quiz, Question
from app.schemas import QuizCreate, QuestionCreate

def create_quiz(db: Session, quiz: QuizCreate):
    db_quiz = Quiz(**quiz.dict())
    db.add(db_quiz)
    db.commit()
    db.refresh(db_quiz)
    return db_quiz

def create_question(db: Session, question: QuestionCreate, quiz_id: int):
    db_question = Question(**question.dict(), quiz_id=quiz_id)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question

def get_quiz(db: Session, quiz_id: int):
    return db.query(Quiz).filter(Quiz.id == quiz_id).first()

def get_quizzes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Quiz).offset(skip).limit(limit).all()
