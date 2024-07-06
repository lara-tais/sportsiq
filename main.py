from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.models import Quiz, Question
from app.schemas import QuizCreate, Quiz as QuizSchema, ScoreResult
from app.database import SessionLocal, engine, Base
from app.crud import create_quiz, get_quiz, get_quizzes

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/quizzes/", response_model=list[QuizSchema])
def read_quizzes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    quizzes = get_quizzes(db, skip=skip, limit=limit)
    return quizzes

@app.get("/api/quizzes/{quiz_id}", response_model=QuizSchema)
def read_quiz(quiz_id: int, db: Session = Depends(get_db)):
    quiz = get_quiz(db, quiz_id=quiz_id)
    if quiz is None:
        raise HTTPException(status_code=404, detail="Quiz not found")
    return quiz

@app.post("/api/quizzes/", response_model=QuizSchema)
def create_quiz(quiz: QuizCreate, db: Session = Depends(get_db)):
    return create_quiz(db=db, quiz=quiz)

@app.post("/api/quizzes/{quiz_id}/score", response_model=ScoreResult)
def calculate_score(quiz_id: int, answers: dict, db: Session = Depends(get_db)):
    quiz = get_quiz(db, quiz_id=quiz_id)
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")

    total_questions = len(quiz.questions)
    correct_answers = 0

    for question in quiz.questions:
        question_id = str(question.id)
        if question_id in answers['answers'] and answers['answers'][question_id] == question.correct_answer:
            correct_answers += 1

    score_result = {
        "total_questions": total_questions,
        "correct_answers": correct_answers,
        "score": correct_answers / total_questions * 100 if total_questions > 0 else 0
    }

    return score_result

# Serve the HTML file
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def serve_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
