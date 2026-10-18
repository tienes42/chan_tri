from database.database import Base, engine

# Import tất cả models để SQLAlchemy đăng ký các bảng
from models.user import User
from models.subject import Subject
from models.lesson import Lesson
from models.game import Game
from models.progress import Progress
from models.game_session import GameSession
from models.game_event import GameEvent


def init_db():
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully.")


if __name__ == "__main__":
    init_db()