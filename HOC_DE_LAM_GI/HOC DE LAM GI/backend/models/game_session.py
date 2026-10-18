from datetime import datetime
from sqlalchemy import ForeignKey,DateTime
from sqlalchemy.orm import Mapped,mapped_column
from database.database import Base
class GameSession(Base):
    __tablename__='game_sessions'
    id: Mapped[int]=mapped_column(primary_key=True)
    user_id: Mapped[int]=mapped_column(ForeignKey('users.id'))
    game_id: Mapped[int]=mapped_column(ForeignKey('games.id'))
    started_at: Mapped[datetime]=mapped_column(DateTime,default=datetime.utcnow)
    finished_at: Mapped[datetime|None]=mapped_column(DateTime)
    score: Mapped[int|None]
