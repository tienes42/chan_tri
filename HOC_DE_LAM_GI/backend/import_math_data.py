import re
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from sqlalchemy import select
from database.database import SessionLocal
from models.subject import Subject
from models.lesson import Lesson


BASE_DIR = Path(__file__).resolve().parent
MATH_FILE = BASE_DIR.parent / "HOC DE LAM GI" / "math-data.js"


def extract_object(text, start):
    depth = 0
    in_string = False
    escape = False
    quote = None

    for i in range(start, len(text)):
        char = text[i]

        if in_string:
            if escape:
                escape = False
            elif char == "\\":
                escape = True
            elif char == quote:
                in_string = False
            continue

        if char in ('"', "'"):
            in_string = True
            quote = char

        elif char == "{":
            depth += 1

        elif char == "}":
            depth -= 1

            if depth == 0:
                return text[start:i + 1]

    raise ValueError("Không tìm thấy object MATH_DATABASE.")


def remove_comments(text):
    result = []

    i = 0
    in_string = False
    escape = False
    quote = None

    while i < len(text):
        char = text[i]

        if in_string:
            result.append(char)

            if escape:
                escape = False
            elif char == "\\":
                escape = True
            elif char == quote:
                in_string = False

            i += 1
            continue

        if char in ('"', "'"):
            in_string = True
            quote = char
            result.append(char)
            i += 1
            continue

        # // comment
        if char == "/" and i + 1 < len(text) and text[i + 1] == "/":
            i += 2

            while i < len(text) and text[i] not in "\r\n":
                i += 1

            continue

        # /* comment */
        if char == "/" and i + 1 < len(text) and text[i + 1] == "*":
            i += 2

            while i + 1 < len(text):
                if text[i] == "*" and text[i + 1] == "/":
                    i += 2
                    break
                i += 1

            continue

        result.append(char)
        i += 1

    return "".join(result)


def quote_javascript_keys(text):
    """
    Chuyển:

        1: {
            title: "..."
        }

    thành:

        "1": {
            "title": "..."
        }
    """

    result = []

    i = 0
    in_string = False
    escape = False
    quote = None

    while i < len(text):
        char = text[i]

        if in_string:
            result.append(char)

            if escape:
                escape = False
            elif char == "\\":
                escape = True
            elif char == quote:
                in_string = False

            i += 1
            continue

        if char in ('"', "'"):
            in_string = True
            quote = char
            result.append(char)
            i += 1
            continue

        match = re.match(
            r'([A-Za-z_$][\w$-]*|\d+)\s*:',
            text[i:]
        )

        if match:
            key = match.group(1)

            result.append('"')
            result.append(key)
            result.append('":')

            i += len(match.group(0))
            continue

        result.append(char)
        i += 1

    return "".join(result)


def load_math_database():

    if not MATH_FILE.exists():
        raise FileNotFoundError(
            f"Không tìm thấy file:\n{MATH_FILE}"
        )

    print(f"Đọc dữ liệu: {MATH_FILE}")

    text = MATH_FILE.read_text(
        encoding="utf-8"
    )

    marker = "const MATH_DATABASE"

    marker_pos = text.find(marker)

    if marker_pos == -1:
        raise ValueError(
            "Không tìm thấy MATH_DATABASE trong math-data.js"
        )

    object_start = text.find(
        "{",
        marker_pos
    )

    if object_start == -1:
        raise ValueError(
            "Không tìm thấy object MATH_DATABASE."
        )

    object_text = extract_object(
        text,
        object_start
    )

    object_text = remove_comments(
        object_text
    )

    object_text = quote_javascript_keys(
        object_text
    )

    try:
        data = json.loads(object_text)

    except json.JSONDecodeError as e:
        print("\nLỖI PHÂN TÍCH math-data.js")
        print(e)
        raise

    return data


def main():

    print("=" * 38)
    print(" IMPORT MATH DATABASE")
    print("=" * 38)

    data = load_math_database()

    print(
        f"Đã đọc {len(data)} lớp."
    )

    total = 0

    for grade, lessons in data.items():
        print(
            f"  Lớp {grade}: {len(lessons)} bài"
        )
        total += len(lessons)

    print("-" * 38)
    print(
        f"TỔNG CỘNG: {total} bài"
    )

    with SessionLocal() as db:

        subject = db.scalar(
            select(Subject).where(
                Subject.slug == "math"
            )
        )

        if subject is None:
            print(
                "Chưa có subject math. Đang tạo..."
            )

            subject = Subject(
                slug="math",
                name="Toán"
            )

            db.add(subject)
            db.flush()

        # Xóa dữ liệu Toán cũ
        old_lessons = db.scalars(
            select(Lesson).where(
                Lesson.subject_id == subject.id
            )
        ).all()

        for lesson in old_lessons:
            db.delete(lesson)

        db.flush()

        print(
            f"Đã xóa {len(old_lessons)} bài cũ."
        )

        inserted = 0

        for grade, topics in data.items():

            grade_number = int(grade)

            for topic, item in topics.items():

                lesson = Lesson(
                    subject_id=subject.id,
                    grade=grade_number,
                    topic=topic,

                    title=item.get("title"),
                    icon=item.get("icon"),
                    description=item.get("description"),

                    context_title=item.get(
                        "contextTitle"
                    ),

                    context=item.get(
                        "context"
                    ),

                    theory=item.get(
                        "theory"
                    ),

                    formula=item.get(
                        "formula"
                    ),

                    example=item.get(
                        "example"
                    ),

                    example_answer=item.get(
                        "exampleAnswer"
                    ),

                    question=item.get(
                        "question"
                    ),

                    answers=item.get(
                        "answers"
                    ),

                    correct=item.get(
                        "correct"
                    ),

                    application=item.get(
                        "application"
                    ),

                    challenge=item.get(
                        "challenge"
                    ),

                    challenge_answer=item.get(
                        "challengeAnswer"
                    ),
                )

                db.add(lesson)

                inserted += 1

        db.commit()

    print("=" * 38)
    print(" IMPORT THÀNH CÔNG")
    print("=" * 38)
    print(
        f"Đã import: {inserted} bài Toán"
    )


if __name__ == "__main__":
    main()