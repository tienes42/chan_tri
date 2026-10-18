from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from database.database import Base

class Progress(Base):
    __tablename__ = "progress"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    lesson_id: Mapped[int] = mapped_column(ForeignKey("lessons.id"), index=True)
    progress: Mapped[int] = mapped_column(default=0)
    completed: Mapped[bool] = mapped_column(default=False)
