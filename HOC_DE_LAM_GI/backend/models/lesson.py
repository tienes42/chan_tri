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

    # =========================
    # GIỚI THIỆU
    # =========================

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # =========================
    # ĐỊNH NGHĨA / KHÁI NIỆM
    # =========================

    definition: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    concept: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # =========================
    # CÔNG THỨC
    # =========================

    formulas: Mapped[list | None] = mapped_column(
        JSONB,
        nullable=True,
    )

    # =========================
    # Ý NGHĨA
    # =========================

    meaning: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # =========================
    # KIẾN THỨC DÙNG TRONG ĐỜI SỐNG
    # =========================

    real_life: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # =========================
    # NỘI DUNG CŨ
    # Giữ lại để không mất dữ liệu hiện tại
    # =========================

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

    # =========================
    # GAME
    # =========================

    game_title: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    game_description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    game_type: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )