import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from sqlalchemy import select
from database.database import SessionLocal
from models.subject import Subject

DEFAULT_SUBJECTS = [
    ("math", "Toán"),
    ("physics", "Vật lý"),
    ("chemistry", "Hóa học"),
]

with SessionLocal() as db:
    for slug, name in DEFAULT_SUBJECTS:
        existing = db.scalar(select(Subject).where(Subject.slug == slug))
        if existing is None:
            db.add(Subject(slug=slug, name=name))
    db.commit()

print("Default subjects seeded.")
