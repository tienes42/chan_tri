from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from database.database import get_db
from models.game import Game
from models.lesson import Lesson
from models.subject import Subject
from schemas.content import GameOut, LessonOut, SubjectOut

router = APIRouter(prefix="/content", tags=["content"])

@router.get("/subjects", response_model=list[SubjectOut])
def list_subjects(db: Session = Depends(get_db)):
    return list(db.scalars(select(Subject).order_by(Subject.id)).all())

@router.get("/subjects/{slug}", response_model=SubjectOut)
def get_subject(slug: str, db: Session = Depends(get_db)):
    subject = db.scalar(select(Subject).where(Subject.slug == slug))
    if subject is None:
        raise HTTPException(status_code=404, detail="Subject not found")
    return subject

@router.get("/subjects/{slug}/lessons", response_model=list[LessonOut])
def list_lessons(
    slug: str,
    grade: int | None = None,
    topic: str | None = None,
    db: Session = Depends(get_db),
):
    subject = db.scalar(select(Subject).where(Subject.slug == slug))
    if subject is None:
        raise HTTPException(status_code=404, detail="Subject not found")

    stmt = select(Lesson).where(Lesson.subject_id == subject.id)
    if grade is not None:
        stmt = stmt.where(Lesson.grade == grade)
    if topic:
        stmt = stmt.where(Lesson.topic == topic)

    return list(db.scalars(stmt.order_by(Lesson.id)).all())

@router.get("/lessons/{lesson_id}", response_model=LessonOut)
def get_lesson(lesson_id: int, db: Session = Depends(get_db)):
    lesson = db.get(Lesson, lesson_id)
    if lesson is None:
        raise HTTPException(status_code=404, detail="Lesson not found")
    return lesson

@router.get("/lessons/{lesson_id}/games", response_model=list[GameOut])
def list_lesson_games(lesson_id: int, db: Session = Depends(get_db)):
    if db.get(Lesson, lesson_id) is None:
        raise HTTPException(status_code=404, detail="Lesson not found")
    return list(db.scalars(
        select(Game).where(Game.lesson_id == lesson_id).order_by(Game.id)
    ).all())
