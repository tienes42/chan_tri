import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from sqlalchemy import select
from database.database import SessionLocal
from models.lesson import Lesson
from models.subject import Subject


# =========================================================
# DỮ LIỆU NỘI DUNG CHI TIẾT
# =========================================================

CONTENT = {

    # =====================================================
    # TOÁN 10
    # =====================================================

    ("math", 10, "menh-de"): {
        "definition": (
            "Mệnh đề là một câu khẳng định có tính đúng hoặc sai xác định. "
            "Một mệnh đề không thể đồng thời vừa đúng vừa sai."
        ),

        "concept": (
            "Mệnh đề thường được ký hiệu bằng các chữ p, q, r,... "
            "Mệnh đề đúng có thể nhận giá trị Đúng, mệnh đề sai nhận giá trị Sai.\n\n"
            "Cần phân biệt mệnh đề với câu hỏi, câu cảm thán hoặc câu chưa xác định được tính đúng sai.\n\n"
            "Mệnh đề phủ định của p được ký hiệu là ¬p."
        ),

        "formulas": [
            {
                "category": "I. Phủ định mệnh đề",
                "items": [
                    {
                        "name": "Phủ định",
                        "formula": "¬p",
                        "note": "¬p đúng khi p sai và ngược lại."
                    }
                ]
            },
            {
                "category": "II. Mệnh đề kéo theo",
                "items": [
                    {
                        "name": "Kéo theo",
                        "formula": "p ⇒ q",
                        "note": "Nếu p đúng và q sai thì p ⇒ q sai."
                    }
                ]
            },
            {
                "category": "III. Mệnh đề tương đương",
                "items": [
                    {
                        "name": "Tương đương",
                        "formula": "p ⇔ q",
                        "note": "p ⇔ q đúng khi p và q cùng giá trị đúng/sai."
                    }
                ]
            },
            {
                "category": "IV. Điều kiện cần và đủ",
                "items": [
                    {
                        "name": "Điều kiện đủ",
                        "formula": "p ⇒ q",
                        "note": "p là điều kiện đủ để có q."
                    },
                    {
                        "name": "Điều kiện cần",
                        "formula": "q ⇒ p",
                        "note": "q là điều kiện cần để có p."
                    },
                    {
                        "name": "Cần và đủ",
                        "formula": "p ⇔ q"
                    }
                ]
            }
        ],

        "meaning": (
            "Mệnh đề là nền tảng của logic toán học và được sử dụng để xây dựng "
            "định lý, điều kiện, thuật toán và các chương trình máy tính."
        ),

        "real_life": (
            "Logic mệnh đề xuất hiện trong lập trình với các điều kiện IF/ELSE, "
            "trong hệ thống điều khiển, tìm kiếm dữ liệu và ra quyết định tự động."
        )
    },


    # =====================================================
    # TẬP HỢP
    # =====================================================

    ("math", 10, "tap-hop"): {
        "definition": (
            "Tập hợp là một nhóm các đối tượng xác định rõ ràng. "
            "Mỗi đối tượng thuộc tập hợp được gọi là một phần tử."
        ),

        "concept": (
            "Tập hợp có thể được biểu diễn bằng cách liệt kê các phần tử "
            "hoặc chỉ ra tính chất đặc trưng của các phần tử.\n\n"
            "Các tập số thường gặp gồm số tự nhiên N, số nguyên Z, "
            "số hữu tỉ Q, số thực R."
        ),

        "formulas": [
            {
                "category": "I. Quan hệ thuộc",
                "items": [
                    {
                        "name": "Phần tử thuộc tập hợp",
                        "formula": "x ∈ A"
                    },
                    {
                        "name": "Phần tử không thuộc",
                        "formula": "x ∉ A"
                    }
                ]
            },
            {
                "category": "II. Quan hệ tập hợp",
                "items": [
                    {
                        "name": "Tập con",
                        "formula": "A ⊂ B"
                    },
                    {
                        "name": "Hai tập hợp bằng nhau",
                        "formula": "A = B ⇔ A ⊂ B và B ⊂ A"
                    }
                ]
            },
            {
                "category": "III. Các phép toán",
                "items": [
                    {
                        "name": "Hợp",
                        "formula": "A ∪ B"
                    },
                    {
                        "name": "Giao",
                        "formula": "A ∩ B"
                    },
                    {
                        "name": "Hiệu",
                        "formula": "A \\ B"
                    },
                    {
                        "name": "Phần bù",
                        "formula": "C_A B = A \\ B"
                    }
                ]
            },
            {
                "category": "IV. Số phần tử",
                "items": [
                    {
                        "name": "Công thức số phần tử của hợp",
                        "formula": "n(A ∪ B) = n(A) + n(B) - n(A ∩ B)"
                    }
                ]
            }
        ],

        "meaning": (
            "Tập hợp giúp tổ chức và phân loại đối tượng theo những đặc điểm "
            "chung, là nền tảng của đại số, xác suất và thống kê."
        ),

        "real_life": (
            "Tập hợp được dùng để phân loại học sinh, sản phẩm, dữ liệu khách hàng, "
            "tìm kiếm dữ liệu và lọc thông tin."
        )
    },


    # =====================================================
    # HÀM SỐ - TOÁN 10
    # =====================================================

    ("math", 10, "ham-so"): {
        "definition": (
            "Hàm số là một quy tắc cho tương ứng mỗi giá trị của biến x thuộc "
            "tập xác định với duy nhất một giá trị y."
        ),

        "concept": (
            "Hàm số thường được viết dưới dạng y = f(x).\n\n"
            "Tập xác định là tập các giá trị của x mà biểu thức f(x) có nghĩa.\n\n"
            "Đồ thị hàm số là tập hợp các điểm M(x; f(x)) trên mặt phẳng tọa độ."
        ),

        "formulas": [
            {
                "category": "I. Hàm số bậc nhất",
                "items": [
                    {
                        "name": "Dạng tổng quát",
                        "formula": "y = ax + b, a ≠ 0"
                    },
                    {
                        "name": "Hệ số góc",
                        "formula": "k = a"
                    },
                    {
                        "name": "Giao trục tung",
                        "formula": "A(0; b)"
                    },
                    {
                        "name": "Nghiệm",
                        "formula": "x = -b/a"
                    }
                ]
            },
            {
                "category": "II. Hàm số bậc hai",
                "items": [
                    {
                        "name": "Dạng tổng quát",
                        "formula": "y = ax² + bx + c, a ≠ 0"
                    },
                    {
                        "name": "Biệt thức",
                        "formula": "Δ = b² - 4ac"
                    },
                    {
                        "name": "Tọa độ đỉnh",
                        "formula": "I(-b/(2a); -Δ/(4a))"
                    },
                    {
                        "name": "Trục đối xứng",
                        "formula": "x = -b/(2a)"
                    }
                ]
            },
            {
                "category": "III. Phép biến đổi đồ thị",
                "items": [
                    {
                        "name": "Tịnh tiến theo Oy",
                        "formula": "y = f(x) + k"
                    },
                    {
                        "name": "Tịnh tiến theo Ox",
                        "formula": "y = f(x - h)"
                    }
                ]
            }
        ],

        "meaning": (
            "Hàm số mô tả mối quan hệ giữa các đại lượng và cho phép dự đoán "
            "một đại lượng thay đổi như thế nào khi đại lượng khác thay đổi."
        ),

        "real_life": (
            "Hàm số được dùng để mô hình hóa quãng đường theo thời gian, "
            "chi phí theo số lượng sản phẩm, doanh thu, nhiệt độ, tốc độ "
            "và rất nhiều hiện tượng thực tế."
        )
    },


    # =====================================================
    # VECTO
    # =====================================================

    ("math", 10, "vecto"): {
        "definition": (
            "Vectơ là một đoạn thẳng có hướng. Vectơ được đặc trưng bởi "
            "điểm đầu, điểm cuối, phương, hướng và độ dài."
        ),

        "concept": (
            "Hai vectơ bằng nhau khi chúng cùng hướng và có cùng độ dài.\n\n"
            "Vectơ không có độ dài bằng 0.\n\n"
            "Vectơ có thể được biểu diễn bằng tọa độ trong mặt phẳng."
        ),

        "formulas": [
            {
                "category": "I. Tọa độ vectơ",
                "items": [
                    {
                        "name": "Vectơ AB",
                        "formula": "→AB = (xB - xA; yB - yA)"
                    },
                    {
                        "name": "Độ dài vectơ",
                        "formula": "|u| = √(x² + y²)"
                    }
                ]
            },
            {
                "category": "II. Phép toán vectơ",
                "items": [
                    {
                        "name": "Tổng",
                        "formula": "u + v = (u₁ + v₁; u₂ + v₂)"
                    },
                    {
                        "name": "Hiệu",
                        "formula": "u - v = (u₁ - v₁; u₂ - v₂)"
                    },
                    {
                        "name": "Nhân với số",
                        "formula": "ku = (ku₁; ku₂)"
                    }
                ]
            },
            {
                "category": "III. Tích vô hướng",
                "items": [
                    {
                        "name": "Tích vô hướng",
                        "formula": "u·v = u₁v₁ + u₂v₂"
                    },
                    {
                        "name": "Theo góc",
                        "formula": "u·v = |u||v|cosθ"
                    },
                    {
                        "name": "Vuông góc",
                        "formula": "u ⟂ v ⇔ u·v = 0"
                    }
                ]
            }
        ],

        "meaning": (
            "Vectơ giúp biểu diễn đại lượng có hướng như vận tốc, lực, "
            "độ dịch chuyển và được sử dụng rộng rãi trong hình học."
        ),

        "real_life": (
            "Trong vật lý, vận tốc và lực được biểu diễn bằng vectơ. "
            "Trong đồ họa máy tính, vectơ dùng để xác định vị trí và hướng chuyển động."
        )
    },


    # =====================================================
    # TAM GIÁC
    # =====================================================

    ("math", 10, "hinh-hoc"): {
        "definition": (
            "Tam giác là hình gồm ba đoạn thẳng nối ba điểm không thẳng hàng. "
            "Ba đoạn thẳng đó tạo thành ba cạnh và ba góc."
        ),

        "concept": (
            "Tam giác có thể được phân loại theo cạnh hoặc theo góc. "
            "Các yếu tố quan trọng gồm cạnh, góc, đường cao, đường trung tuyến, "
            "đường phân giác, đường trung trực, bán kính đường tròn nội tiếp "
            "và bán kính đường tròn ngoại tiếp."
        ),

        "formulas": [
            {
                "category": "I. Góc trong tam giác",
                "items": [
                    {
                        "name": "Tổng ba góc",
                        "formula": "A + B + C = 180°"
                    },
                    {
                        "name": "Góc ngoài",
                        "formula": "Góc ngoài = tổng hai góc trong không kề"
                    }
                ]
            },
            {
                "category": "II. Chu vi và diện tích",
                "items": [
                    {
                        "name": "Chu vi",
                        "formula": "P = a + b + c"
                    },
                    {
                        "name": "Diện tích theo đáy và chiều cao",
                        "formula": "S = 1/2 · a · h_a"
                    },
                    {
                        "name": "Diện tích theo hai cạnh và góc xen giữa",
                        "formula": "S = 1/2 · ab · sin C"
                    },
                    {
                        "name": "Công thức Heron",
                        "formula": "S = √[p(p-a)(p-b)(p-c)]"
                    },
                    {
                        "name": "Nửa chu vi",
                        "formula": "p = (a+b+c)/2"
                    },
                    {
                        "name": "Theo bán kính nội tiếp",
                        "formula": "S = p·r"
                    },
                    {
                        "name": "Theo bán kính ngoại tiếp",
                        "formula": "S = abc/(4R)"
                    }
                ]
            },
            {
                "category": "III. Định lý Pythagore",
                "items": [
                    {
                        "name": "Tam giác vuông",
                        "formula": "a² + b² = c²",
                        "note": "c là cạnh huyền."
                    }
                ]
            },
            {
                "category": "IV. Định lý Cosin",
                "items": [
                    {
                        "name": "Định lý Cosin",
                        "formula": "a² = b² + c² - 2bc·cos A"
                    },
                    {
                        "name": "Dạng tương tự",
                        "formula": "b² = a² + c² - 2ac·cos B"
                    },
                    {
                        "name": "Dạng tương tự",
                        "formula": "c² = a² + b² - 2ab·cos C"
                    }
                ]
            },
            {
                "category": "V. Định lý Sin",
                "items": [
                    {
                        "name": "Định lý Sin",
                        "formula": "a/sin A = b/sin B = c/sin C = 2R"
                    }
                ]
            },
            {
                "category": "VI. Đường trung tuyến",
                "items": [
                    {
                        "name": "Trung tuyến từ A",
                        "formula": "m_a = 1/2√(2b² + 2c² - a²)"
                    },
                    {
                        "name": "Trung tuyến từ B",
                        "formula": "m_b = 1/2√(2a² + 2c² - b²)"
                    },
                    {
                        "name": "Trung tuyến từ C",
                        "formula": "m_c = 1/2√(2a² + 2b² - c²)"
                    }
                ]
            },
            {
                "category": "VII. Tam giác đặc biệt",
                "items": [
                    {
                        "name": "Tam giác đều",
                        "formula": "S = a²√3/4"
                    },
                    {
                        "name": "Tam giác đều - đường cao",
                        "formula": "h = a√3/2"
                    },
                    {
                        "name": "Tam giác vuông cân",
                        "formula": "c = a√2"
                    }
                ]
            }
        ],

        "meaning": (
            "Các công thức tam giác cho phép tính cạnh, góc, diện tích, "
            "chu vi và các yếu tố hình học khi không thể đo trực tiếp."
        ),

        "real_life": (
            "Tam giác và các định lý của nó được sử dụng trong xây dựng, "
            "đo đạc đất đai, thiết kế cầu, kiến trúc, định vị và kỹ thuật."
        )
    },


    # =====================================================
    # ĐẠO HÀM
    # =====================================================

    ("math", 11, "dao-ham"): {
        "definition": (
            "Đạo hàm của hàm số tại một điểm biểu thị tốc độ thay đổi tức thời "
            "của hàm số tại điểm đó."
        ),

        "concept": (
            "Về hình học, đạo hàm tại một điểm là hệ số góc của tiếp tuyến "
            "với đồ thị hàm số tại điểm đó.\n\n"
            "Về vật lý, nếu s(t) là quãng đường thì s'(t) là vận tốc tức thời; "
            "s''(t) là gia tốc."
        ),

        "formulas": [
            {
                "category": "I. Định nghĩa đạo hàm",
                "items": [
                    {
                        "name": "Đạo hàm tại x₀",
                        "formula": "f'(x₀) = lim[h→0] [f(x₀+h)-f(x₀)]/h"
                    }
                ]
            },
            {
                "category": "II. Công thức cơ bản",
                "items": [
                    {
                        "name": "Hằng số",
                        "formula": "(C)' = 0"
                    },
                    {
                        "name": "x",
                        "formula": "(x)' = 1"
                    },
                    {
                        "name": "Lũy thừa",
                        "formula": "(x^n)' = n·x^(n-1)"
                    },
                    {
                        "name": "Hệ số",
                        "formula": "(ku)' = k·u'"
                    }
                ]
            },
            {
                "category": "III. Quy tắc tính đạo hàm",
                "items": [
                    {
                        "name": "Tổng",
                        "formula": "(u+v)' = u' + v'"
                    },
                    {
                        "name": "Hiệu",
                        "formula": "(u-v)' = u' - v'"
                    },
                    {
                        "name": "Tích",
                        "formula": "(uv)' = u'v + uv'"
                    },
                    {
                        "name": "Thương",
                        "formula": "(u/v)' = (u'v-uv')/v²",
                        "note": "v ≠ 0"
                    },
                    {
                        "name": "Hàm hợp",
                        "formula": "(f(u))' = f'(u)·u'"
                    }
                ]
            },
            {
                "category": "IV. Hàm lượng giác",
                "items": [
                    {
                        "name": "Sin",
                        "formula": "(sin x)' = cos x"
                    },
                    {
                        "name": "Cos",
                        "formula": "(cos x)' = -sin x"
                    },
                    {
                        "name": "Tan",
                        "formula": "(tan x)' = 1/cos²x"
                    },
                    {
                        "name": "Cot",
                        "formula": "(cot x)' = -1/sin²x"
                    }
                ]
            },
            {
                "category": "V. Hàm mũ và logarit",
                "items": [
                    {
                        "name": "e^x",
                        "formula": "(e^x)' = e^x"
                    },
                    {
                        "name": "a^x",
                        "formula": "(a^x)' = a^x·ln a"
                    },
                    {
                        "name": "ln x",
                        "formula": "(ln x)' = 1/x"
                    },
                    {
                        "name": "log_a x",
                        "formula": "(log_a x)' = 1/(x·ln a)"
                    }
                ]
            },
            {
                "category": "VI. Ứng dụng đạo hàm",
                "items": [
                    {
                        "name": "Tiếp tuyến",
                        "formula": "y = f'(x₀)(x-x₀)+f(x₀)"
                    },
                    {
                        "name": "Điều kiện cực trị",
                        "formula": "f'(x₀)=0"
                    },
                    {
                        "name": "Vận tốc",
                        "formula": "v(t)=s'(t)"
                    },
                    {
                        "name": "Gia tốc",
                        "formula": "a(t)=v'(t)=s''(t)"
                    }
                ]
            }
        ],

        "meaning": (
            "Đạo hàm cho phép nghiên cứu tốc độ thay đổi, tìm cực trị, "
            "khảo sát đồ thị và tối ưu hóa."
        ),

        "real_life": (
            "Đạo hàm có thể dùng để tìm thời điểm xe đạt tốc độ lớn nhất, "
            "tìm thời điểm một vật chuyển động nhanh nhất, tối ưu chi phí, "
            "diện tích, lợi nhuận và nhiều bài toán kỹ thuật."
        ),

        "game_title": "Điều khiển chiếc xe đạt tốc độ tối ưu",
        "game_description": (
            "Xây dựng và điều chỉnh hàm quãng đường theo thời gian, "
            "sau đó dùng đạo hàm để xác định thời điểm xe đạt tốc độ lớn nhất."
        ),
        "game_type": "function_challenge"
    },


    # =====================================================
    # NGUYÊN HÀM
    # =====================================================

    ("math", 12, "nguyen-ham"): {
        "definition": (
            "Hàm số F(x) được gọi là một nguyên hàm của f(x) trên một khoảng "
            "nếu F'(x) = f(x) trên khoảng đó."
        ),

        "concept": (
            "Nếu F là một nguyên hàm của f thì mọi nguyên hàm của f có dạng "
            "F(x) + C, trong đó C là hằng số."
        ),

        "formulas": [
            {
                "category": "I. Tính chất",
                "items": [
                    {
                        "name": "Định nghĩa",
                        "formula": "F'(x) = f(x)"
                    },
                    {
                        "name": "Họ nguyên hàm",
                        "formula": "∫f(x)dx = F(x) + C"
                    },
                    {
                        "name": "Tuyến tính",
                        "formula": "∫[f(x) ± g(x)]dx = ∫f(x)dx ± ∫g(x)dx"
                    },
                    {
                        "name": "Nhân hằng số",
                        "formula": "∫k·f(x)dx = k∫f(x)dx"
                    }
                ]
            },
            {
                "category": "II. Nguyên hàm cơ bản",
                "items": [
                    {
                        "name": "Lũy thừa",
                        "formula": "∫x^n dx = x^(n+1)/(n+1) + C",
                        "note": "n ≠ -1"
                    },
                    {
                        "name": "1/x",
                        "formula": "∫1/x dx = ln|x| + C"
                    },
                    {
                        "name": "e^x",
                        "formula": "∫e^x dx = e^x + C"
                    },
                    {
                        "name": "a^x",
                        "formula": "∫a^x dx = a^x/ln(a) + C"
                    },
                    {
                        "name": "sin x",
                        "formula": "∫sin x dx = -cos x + C"
                    },
                    {
                        "name": "cos x",
                        "formula": "∫cos x dx = sin x + C"
                    }
                ]
            }
        ],

        "meaning": (
            "Nguyên hàm là phép toán ngược của đạo hàm và là nền tảng để "
            "tính tích phân, diện tích và nhiều đại lượng tích lũy."
        ),

        "real_life": (
            "Nếu biết vận tốc theo thời gian, có thể dùng nguyên hàm để "
            "tính quãng đường. Trong vật lý và kỹ thuật, nguyên hàm dùng "
            "để tính các đại lượng tích lũy theo thời gian."
        )
    },


    # =====================================================
    # SỐ PHỨC
    # =====================================================

    ("math", 12, "so-phuc"): {
        "definition": (
            "Số phức có dạng z = a + bi, trong đó a,b là số thực và i² = -1."
        ),

        "concept": (
            "a được gọi là phần thực, b là phần ảo. "
            "Số phức có thể biểu diễn trên mặt phẳng phức."
        ),

        "formulas": [
            {
                "category": "I. Phép toán",
                "items": [
                    {
                        "name": "Cộng",
                        "formula": "(a+bi)+(c+di)=(a+c)+(b+d)i"
                    },
                    {
                        "name": "Trừ",
                        "formula": "(a+bi)-(c+di)=(a-c)+(b-d)i"
                    },
                    {
                        "name": "Nhân",
                        "formula": "(a+bi)(c+di)=(ac-bd)+(ad+bc)i"
                    },
                    {
                        "name": "Liên hợp",
                        "formula": "z̄ = a-bi"
                    },
                    {
                        "name": "Môđun",
                        "formula": "|z| = √(a²+b²)"
                    }
                ]
            },
            {
                "category": "II. Chia số phức",
                "items": [
                    {
                        "name": "Chia",
                        "formula": "z₁/z₂ = z₁·z̄₂ / |z₂|²",
                        "note": "z₂ ≠ 0"
                    }
                ]
            }
        ],

        "meaning": (
            "Số phức mở rộng hệ thống số thực và cho phép giải nhiều "
            "phương trình không có nghiệm thực."
        ),

        "real_life": (
            "Số phức được sử dụng trong kỹ thuật điện, xử lý tín hiệu, "
            "điện xoay chiều và kỹ thuật điều khiển."
        )
    }
}


# =========================================================
# CẬP NHẬT DATABASE
# =========================================================

def update_lessons():

    updated = 0
    skipped = 0

    with SessionLocal() as db:

        subject_cache = {}

        for key, data in CONTENT.items():

            subject_slug, grade, topic = key

            if subject_slug not in subject_cache:

                subject_cache[subject_slug] = db.scalar(
                    select(Subject).where(
                        Subject.slug == subject_slug
                    )
                )

            subject = subject_cache[subject_slug]

            if subject is None:
                print(
                    f"[BO QUA] Khong co mon: {subject_slug}"
                )
                skipped += 1
                continue

            lesson = db.scalar(
                select(Lesson).where(
                    Lesson.subject_id == subject.id,
                    Lesson.grade == grade,
                    Lesson.topic == topic
                )
            )

            if lesson is None:
                print(
                    f"[BO QUA] Khong tim thay: "
                    f"{subject_slug} lop {grade} {topic}"
                )
                skipped += 1
                continue

            lesson.definition = data.get(
                "definition"
            )

            lesson.concept = data.get(
                "concept"
            )

            lesson.formulas = data.get(
                "formulas"
            )

            lesson.meaning = data.get(
                "meaning"
            )

            lesson.real_life = data.get(
                "real_life"
            )

            if "game_title" in data:
                lesson.game_title = data["game_title"]

            if "game_description" in data:
                lesson.game_description = data["game_description"]

            if "game_type" in data:
                lesson.game_type = data["game_type"]

            updated += 1

            print(
                f"[OK] {subject_slug} | "
                f"Lop {grade} | {topic}"
            )

        db.commit()

    print()
    print("========================================")
    print(f"DA CAP NHAT: {updated} BAI")
    print(f"BO QUA:      {skipped} BAI")
    print("========================================")


if __name__ == "__main__":
    update_lessons()