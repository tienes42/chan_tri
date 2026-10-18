from pydantic import BaseModel, ConfigDict


class SubjectOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    slug: str
    name: str


class LessonOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    subject_id: int
    grade: int | None
    topic: str
    title: str
    icon: str | None

    description: str | None

    # Nội dung bài học mới
    definition: str | None
    concept: str | None
    formulas: list | None
    meaning: str | None
    real_life: str | None

    # Nội dung cũ
    context_title: str | None
    context: str | None
    theory: str | None
    formula: str | None
    example: str | None
    example_answer: str | None
    question: str | None
    answers: list[str] | None
    correct: int | None
    application: str | None
    challenge: str | None
    challenge_answer: str | None

    # Game
    game_title: str | None
    game_description: str | None
    game_type: str | None


class GameOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    lesson_id: int | None
    name: str
    game_type: str