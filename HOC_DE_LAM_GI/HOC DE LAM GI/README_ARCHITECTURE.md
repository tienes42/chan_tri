# HỌC ĐỂ LÀM GÌ — kiến trúc v2

Frontend cũ được giữ nguyên. Backend mới chạy song song.

Frontend (HTML/CSS/JS) -> REST API -> Python/FastAPI -> PostgreSQL
                                             |
                                             +-> Game modules
                                             +-> AI analysis

Database cốt lõi: users, subjects, lessons, games, progress, game_sessions, game_events.
`game_events` lưu quá trình chơi, không chỉ điểm số, để phục vụ phân tích AI.

## Chạy nhanh
1. `python -m venv .venv`
2. Windows: `.venv\\Scripts\\Activate.ps1` | macOS/Linux: `source .venv/bin/activate`
3. `pip install -r backend/requirements.txt`
4. `uvicorn backend.main:app --reload`
5. Mở `http://127.0.0.1:8000/docs`

Mặc định database local là SQLite để backend chạy ngay. Khi dùng PostgreSQL thật, tạo `backend/.env` từ `.env.example`.
