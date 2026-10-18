from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from database.database import Base

class Game(Base):
    __tablename__ = "games"

    id: Mapped[int] = mapped_column(primary_key=True)
    lesson_id: Mapped[int | None] = mapped_column(ForeignKey("lessons.id"), index=True)
    name: Mapped[str] = mapped_column(String(200))
    game_type: Mapped[str] = mapped_column(String(50))
