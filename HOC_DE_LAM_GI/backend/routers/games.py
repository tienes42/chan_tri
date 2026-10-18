import json
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.database import get_db
from models.game import Game
from models.game_event import GameEvent
from models.game_session import GameSession
from schemas.game import GameEventCreate, GameSessionCreate, GameSessionOut

router = APIRouter(prefix="/games", tags=["games"])

@router.post("/sessions")
def create_session(
    payload: GameSessionCreate,
    db: Session = Depends(get_db)
):
    game = db.get(Game, payload.game_id)

    if game is None:
        raise HTTPException(
            status_code=404,
            detail="Game not found"
        )

    session = GameSession(
        user_id=payload.user_id,
        game_id=payload.game_id
    )

    db.add(session)
    db.commit()
    db.refresh(session)

    return {
        "id": session.id,
        "user_id": session.user_id,
        "game_id": session.game_id,
        "started_at": session.started_at,
        "score": session.score
    }

@router.post("/sessions/{session_id}/events")
def add_event(
    session_id: int,
    payload: GameEventCreate,
    db: Session = Depends(get_db),
):
    if db.get(GameSession, session_id) is None:
        raise HTTPException(status_code=404, detail="Game session not found")

    event = GameEvent(
        session_id=session_id,
        action=payload.action,
        event_data=payload.event_data,
    )
    db.add(event)
    db.commit()
    db.refresh(event)
    return {"id": event.id, "status": "recorded"}

@router.post("/sessions/{session_id}/finish")
def finish_session(
    session_id: int,
    score: int | None = None,
    db: Session = Depends(get_db),
):
    session = db.get(GameSession, session_id)
    if session is None:
        raise HTTPException(status_code=404, detail="Game session not found")

    session.finished_at = datetime.utcnow()
    session.score = score
    db.commit()
    return {"status": "finished", "session_id": session.id, "score": score}
