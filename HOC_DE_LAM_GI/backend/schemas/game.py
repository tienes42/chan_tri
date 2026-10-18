from datetime import datetime

from pydantic import BaseModel, ConfigDict


class GameSessionCreate(BaseModel):
    user_id: int
    game_id: int


class GameSessionOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    game_id: int
    started_at: datetime
    score: int | None


class GameEventCreate(BaseModel):
    action: str
    event_data: str | None = None