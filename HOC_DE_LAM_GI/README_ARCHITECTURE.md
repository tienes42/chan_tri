# HỌC ĐỂ LÀM GÌ — v3

## Bước đã hoàn thành
- Giữ nguyên frontend cũ.
- FastAPI backend.
- SQLAlchemy models.
- PostgreSQL-ready Docker Compose.
- REST API cho subjects, lessons, games.
- Game session/event API để chuẩn bị cho AI phân tích.
- Seed 3 môn mặc định: Toán, Vật lý, Hóa học.

## Chạy PostgreSQL
```bash
docker compose up -d postgres
```

Tạo `backend/.env` từ `backend/.env.example`.

## Chạy backend
```bash
python -m venv .venv
# Windows PowerShell:
.venv\\Scripts\\Activate.ps1
pip install -r backend/requirements.txt
uvicorn backend.main:app --reload
```

API docs:
`http://127.0.0.1:8000/docs`

## Khởi tạo dữ liệu
```bash
python backend/init_db.py
python backend/seed.py
```

## API hiện có
- GET `/api/health`
- GET `/api/content/subjects`
- GET `/api/content/subjects/{slug}`
- GET `/api/content/subjects/{slug}/lessons`
- GET `/api/content/lessons/{lesson_id}`
- GET `/api/content/lessons/{lesson_id}/games`
- POST `/api/games/sessions`
- POST `/api/games/sessions/{session_id}/events`
- POST `/api/games/sessions/{session_id}/finish`

## Quan trọng
Frontend hiện tại chưa bị ép chuyển sang API. Đây là chủ ý:
1. dựng backend;
2. kiểm tra database;
3. nhập/chuyển dữ liệu hiện tại;
4. sau đó chuyển từng trang sang API.

Không kết nối frontend trực tiếp với PostgreSQL.
