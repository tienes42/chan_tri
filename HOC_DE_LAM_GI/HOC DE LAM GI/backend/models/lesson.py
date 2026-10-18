from sqlalchemy import ForeignKey, Integer, String, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from database.database import Base


class Lesson(Base):
    __tablename__ = "lessons"

    id: Mapped[int] = mapped_column(primary_key=True)

    subject_id: Mapped[int] = mapped_column(
        ForeignKey("subjects.id"),
        index=True,
        nullable=False,
    )

    grade: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
        index=True,
    )

    topic: Mapped[str] = mapped_column(
        String(150),
        index=True,
        nullable=False,
    )

    title: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    icon: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    context_title: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    context: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    theory: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    formula: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    example: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    example_answer: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    question: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    answers: Mapped[list[str] | None] = mapped_column(
        JSONB,
        nullable=True,
    )

    correct: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    application: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    challenge: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    challenge_answer: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )