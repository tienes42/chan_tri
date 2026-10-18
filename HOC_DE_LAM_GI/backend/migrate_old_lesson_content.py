import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from sqlalchemy import select
from database.database import SessionLocal
from models.lesson import Lesson


def migrate():

    updated = 0

    with SessionLocal() as db:

        lessons = list(
            db.scalars(
                select(Lesson).order_by(
                    Lesson.grade,
                    Lesson.id
                )
            ).all()
        )

        print(f"Tim thay {len(lessons)} bai hoc trong database.")
        print()

        for lesson in lessons:

            # ==========================================
            # DEFINITION
            # ==========================================

            if not lesson.definition:

                lesson.definition = (
                    lesson.theory
                    or lesson.context
                    or lesson.description
                    or ""
                )


            # ==========================================
            # CONCEPT
            # ==========================================

            if not lesson.concept:

                lesson.concept = (
                    lesson.context
                    or lesson.theory
                    or ""
                )


            # ==========================================
            # FORMULAS
            # ==========================================

            if not lesson.formulas:

                formulas = []

                if lesson.formula:

                    formulas.append({
                        "category": "Công thức / kiến thức chính",
                        "items": [
                            {
                                "name": "Công thức",
                                "formula": lesson.formula,
                                "note": ""
                            }
                        ]
                    })

                lesson.formulas = formulas


            # ==========================================
            # MEANING
            # ==========================================

            if not lesson.meaning:

                lesson.meaning = (
                    lesson.application
                    or lesson.description
                    or ""
                )


            # ==========================================
            # REAL LIFE
            # ==========================================

            if not lesson.real_life:

                lesson.real_life = (
                    lesson.application
                    or lesson.context
                    or ""
                )


            updated += 1

            print(
                f"[OK] Lop {lesson.grade} | "
                f"{lesson.topic} | "
                f"{lesson.title}"
            )


        db.commit()


    print()
    print("=" * 60)
    print(f"DA CHUYEN DOI: {updated} BAI")
    print("=" * 60)


if __name__ == "__main__":
    migrate()