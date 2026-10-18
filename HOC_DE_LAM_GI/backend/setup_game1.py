from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from sqlalchemy import select

from database.database import SessionLocal
from models.game import Game
from models.lesson import Lesson

GAME_TYPE = "store_management"
GAME_NAME = "Quản lý cửa hàng"

with SessionLocal() as db:
    lesson = db.scalar(
        select(Lesson).where(
            Lesson.grade == 10,
            Lesson.topic == "ham-so"
        )
    )

    if lesson is None:
        print("KHONG TIM THAY LESSON: Toan 10 - ham-so")
        raise SystemExit(1)

    # Game hiện tại của bài Hàm số sẽ được dùng làm Game 01.
    game = db.scalar(
        select(Game).where(Game.lesson_id == lesson.id)
        .order_by(Game.id)
    )

    if game is None:
        game = Game(
            lesson_id=lesson.id,
            name=GAME_NAME,
            game_type=GAME_TYPE
        )
        db.add(game)
    else:
        game.name = GAME_NAME
        game.game_type = GAME_TYPE

    lesson.game_title = "Thử thách thực tế: Quản lý cửa hàng"
    lesson.game_description = (
        "Điều hành một cửa hàng trong 5 ngày: chọn giá bán và lượng nhập "
        "để tối ưu doanh thu, chi phí và lợi nhuận bằng kiến thức hàm số."
    )
    lesson.game_type = GAME_TYPE

    db.commit()
    db.refresh(game)

    print("DA CAI GAME 01")
    print("Lesson ID:", lesson.id)
    print("Game ID:", game.id)
    print("Game type:", game.game_type)
    print("Tên:", game.name)
