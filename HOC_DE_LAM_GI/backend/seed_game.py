import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from sqlalchemy import select

from database.database import SessionLocal
from models.game import Game
from models.lesson import Lesson
from models.user import User

with SessionLocal() as db:


# Tạo user demo
 user = db.scalar(
    select(User).where(User.username == "demo")
)

if user is None:
    user = User(
        username="demo",
        password_hash="demo",
        name="Người chơi Demo",
        grade=10
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    print("DA TAO USER DEMO")

else:
    print("USER DEMO DA TON TAI")

print("User ID:", user.id)

# Tìm bài Hàm số lớp 10
lesson = db.scalar(
    select(Lesson).where(
        Lesson.grade == 10,
        Lesson.topic == "ham-so"
    )
)

if lesson is None:
    print("KHONG TIM THAY BAI HAM SO LOP 10")
    sys.exit(1)

# Tạo game
game = db.scalar(
    select(Game).where(
        Game.lesson_id == lesson.id,
        Game.game_type == "function_challenge"
    )
)

if game is None:
    game = Game(
        lesson_id=lesson.id,
        name="Thử thách Hàm số",
        game_type="function_challenge"
    )

    db.add(game)
    db.commit()
    db.refresh(game)

    print("DA TAO GAME")

else:
    print("GAME DA TON TAI")

print("Game ID:", game.id)
print("Lesson ID:", lesson.id)

