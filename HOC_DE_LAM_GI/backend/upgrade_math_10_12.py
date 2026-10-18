from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from sqlalchemy import select
from database.database import SessionLocal
from models.lesson import Lesson


DATA = {

    # =========================================================
    # TOÁN 10
    # =========================================================

    (10, "menh-de"): {
        "description": "Mệnh đề là một khẳng định có thể xác định được tính đúng hoặc sai.",
        "definition": "Mệnh đề là một câu khẳng định mà ta xác định được nó đúng hoặc sai. Một mệnh đề không thể đồng thời vừa đúng vừa sai.",
        "concept": "Cần phân biệt mệnh đề với câu hỏi, câu cảm thán, câu yêu cầu và những câu chưa xác định được giá trị đúng sai.",
        "formulas": [
            {
                "category": "Mệnh đề",
                "items": [
                    {
                        "name": "Phủ định",
                        "formula": "Phủ định của P là ¬P",
                        "note": "Nếu P đúng thì ¬P sai và ngược lại."
                    },
                    {
                        "name": "Mệnh đề kéo theo",
                        "formula": "P ⇒ Q",
                        "note": "Đọc là nếu P thì Q."
                    },
                    {
                        "name": "Mệnh đề tương đương",
                        "formula": "P ⇔ Q",
                        "note": "P đúng khi và chỉ khi Q đúng."
                    }
                ]
            },
            {
                "category": "Mệnh đề chứa ký hiệu ∀ và ∃",
                "items": [
                    {
                        "name": "Mọi",
                        "formula": "∀x ∈ A, P(x)",
                        "note": "P(x) đúng với mọi x thuộc A."
                    },
                    {
                        "name": "Tồn tại",
                        "formula": "∃x ∈ A : P(x)",
                        "note": "Có ít nhất một x thuộc A để P(x) đúng."
                    }
                ]
            }
        ],
        "meaning": "Mệnh đề là nền tảng của tư duy logic và cách xây dựng các lập luận toán học.",
        "real_life": "Logic mệnh đề được sử dụng trong lập trình, điều kiện rẽ nhánh, kiểm tra dữ liệu và ra quyết định."
    },

    (10, "tap-hop"): {
        "description": "Tập hợp dùng để mô tả một nhóm các đối tượng có cùng đặc điểm.",
        "definition": "Tập hợp là một khái niệm cơ bản của toán học, gồm các phần tử được xác định rõ ràng.",
        "concept": "Các phép toán quan trọng gồm hợp, giao, hiệu và phần bù.",
        "formulas": [
            {
                "category": "Phép toán tập hợp",
                "items": [
                    {
                        "name": "Giao",
                        "formula": "A ∩ B",
                        "note": "Gồm các phần tử đồng thời thuộc A và B."
                    },
                    {
                        "name": "Hợp",
                        "formula": "A ∪ B",
                        "note": "Gồm các phần tử thuộc A hoặc B."
                    },
                    {
                        "name": "Hiệu",
                        "formula": "A \\ B",
                        "note": "Gồm các phần tử thuộc A nhưng không thuộc B."
                    },
                    {
                        "name": "Phần bù",
                        "formula": "C_U A = U \\ A",
                        "note": "Phần bù của A trong tập hợp U."
                    }
                ]
            },
            {
                "category": "Số phần tử",
                "items": [
                    {
                        "name": "Công thức cộng",
                        "formula": "|A ∪ B| = |A| + |B| − |A ∩ B|",
                        "note": "Dùng khi hai tập hợp có phần giao."
                    }
                ]
            }
        ],
        "meaning": "Tập hợp giúp tổ chức và phân loại đối tượng một cách chính xác.",
        "real_life": "Được sử dụng trong cơ sở dữ liệu, tìm kiếm, phân loại sản phẩm và xử lý dữ liệu."
    },

    (10, "ham-so"): {
        "description": "Hàm số mô tả sự phụ thuộc của một đại lượng vào một đại lượng khác.",
        "definition": "Cho tập D. Hàm số f xác định trên D là quy tắc đặt tương ứng mỗi x thuộc D với đúng một số thực f(x).",
        "concept": "Các nội dung quan trọng gồm tập xác định, tập giá trị, tính đồng biến, nghịch biến và đồ thị.",
        "formulas": [
            {
                "category": "Hàm số bậc nhất",
                "items": [
                    {
                        "name": "Dạng tổng quát",
                        "formula": "y = ax + b, a ≠ 0",
                        "note": "Đồ thị là một đường thẳng."
                    },
                    {
                        "name": "Hệ số góc",
                        "formula": "a",
                        "note": "a > 0: hàm đồng biến; a < 0: hàm nghịch biến."
                    }
                ]
            },
            {
                "category": "Hàm số bậc hai",
                "items": [
                    {
                        "name": "Dạng tổng quát",
                        "formula": "y = ax² + bx + c, a ≠ 0",
                        "note": "Đồ thị là một parabol."
                    },
                    {
                        "name": "Đỉnh parabol",
                        "formula": "x_I = −b/(2a), y_I = −Δ/(4a)",
                        "note": "I là đỉnh của parabol."
                    },
                    {
                        "name": "Biệt thức",
                        "formula": "Δ = b² − 4ac",
                        "note": "Dùng để xét nghiệm của phương trình ax² + bx + c = 0."
                    }
                ]
            }
        ],
        "meaning": "Hàm số là công cụ quan trọng để mô hình hóa mối quan hệ giữa các đại lượng.",
        "real_life": "Được dùng để mô tả quãng đường theo thời gian, chi phí theo số lượng sản phẩm, doanh thu và nhiều hiện tượng thực tế."
    },

    (10, "vecto"): {
        "description": "Vectơ biểu diễn một đại lượng có hướng và độ lớn.",
        "definition": "Vectơ là một đoạn thẳng có hướng, được xác định bởi điểm đầu và điểm cuối.",
        "concept": "Các phép toán cơ bản gồm tổng, hiệu, tích vectơ với một số và tọa độ vectơ.",
        "formulas": [
            {
                "category": "Tọa độ vectơ",
                "items": [
                    {
                        "name": "Tọa độ vectơ",
                        "formula": "AB⃗ = (x_B − x_A, y_B − y_A)",
                        "note": "Dùng khi biết tọa độ A và B."
                    },
                    {
                        "name": "Độ dài",
                        "formula": "|AB⃗| = √((x_B−x_A)² + (y_B−y_A)²)",
                        "note": "Là khoảng cách giữa A và B."
                    }
                ]
            },
            {
                "category": "Phép toán",
                "items": [
                    {
                        "name": "Tổng",
                        "formula": "a⃗ + b⃗",
                        "note": "Có thể thực hiện theo quy tắc hình bình hành hoặc tọa độ."
                    },
                    {
                        "name": "Tích vô hướng",
                        "formula": "a⃗·b⃗ = |a⃗||b⃗|cos(a⃗,b⃗)",
                        "note": "Dùng để nghiên cứu góc và vuông góc."
                    }
                ]
            }
        ],
        "meaning": "Vectơ giúp biểu diễn đồng thời độ lớn và hướng của một đại lượng.",
        "real_life": "Được dùng trong vật lý để biểu diễn vận tốc, lực, gia tốc và chuyển động."
    },

    (10, "hinh-hoc"): {
        "description": "Hình học tọa độ dùng hệ trục tọa độ để biểu diễn điểm, đường thẳng và các đối tượng hình học.",
        "definition": "Mỗi điểm trong mặt phẳng được xác định bởi một cặp tọa độ (x, y).",
        "concept": "Các nội dung chính gồm tọa độ điểm, khoảng cách, trung điểm, phương trình đường thẳng và đường tròn.",
        "formulas": [
            {
                "category": "Điểm và đoạn thẳng",
                "items": [
                    {
                        "name": "Khoảng cách hai điểm",
                        "formula": "AB = √((x_B−x_A)² + (y_B−y_A)²)",
                        "note": "Công thức khoảng cách trong mặt phẳng tọa độ."
                    },
                    {
                        "name": "Trung điểm",
                        "formula": "M((x_A+x_B)/2, (y_A+y_B)/2)",
                        "note": "M là trung điểm AB."
                    }
                ]
            },
            {
                "category": "Đường thẳng",
                "items": [
                    {
                        "name": "Phương trình tổng quát",
                        "formula": "ax + by + c = 0",
                        "note": "a và b không đồng thời bằng 0."
                    },
                    {
                        "name": "Khoảng cách từ điểm đến đường thẳng",
                        "formula": "d(M,Δ)=|ax_M+by_M+c|/√(a²+b²)",
                        "note": "M là điểm cần tính khoảng cách."
                    }
                ]
            },
            {
                "category": "Đường tròn",
                "items": [
                    {
                        "name": "Phương trình đường tròn",
                        "formula": "(x−a)² + (y−b)² = R²",
                        "note": "Tâm I(a,b), bán kính R."
                    }
                ]
            }
        ],
        "meaning": "Hình học tọa độ chuyển các bài toán hình học thành bài toán đại số.",
        "real_life": "Được dùng trong bản đồ số, GPS, thiết kế kỹ thuật và đồ họa máy tính."
    },

    (10, "thong-ke"): {
        "description": "Thống kê giúp thu thập, tổ chức, phân tích và diễn giải dữ liệu.",
        "definition": "Một mẫu dữ liệu gồm các giá trị thu thập được từ một đối tượng hoặc hiện tượng cần nghiên cứu.",
        "concept": "Các đại lượng đặc trưng giúp mô tả xu hướng trung tâm và mức độ phân tán của dữ liệu.",
        "formulas": [
            {
                "category": "Các số đặc trưng",
                "items": [
                    {
                        "name": "Số trung bình",
                        "formula": "x̄ = (x₁ + x₂ + ... + x_n)/n",
                        "note": "Tổng các giá trị chia cho số lượng giá trị."
                    },
                    {
                        "name": "Khoảng biến thiên",
                        "formula": "R = x_max − x_min",
                        "note": "Đo mức độ trải rộng của dữ liệu."
                    }
                ]
            },
            {
                "category": "Trung vị và tứ phân vị",
                "items": [
                    {
                        "name": "Trung vị",
                        "formula": "Me",
                        "note": "Giá trị nằm giữa dãy số đã sắp xếp."
                    },
                    {
                        "name": "Khoảng tứ phân vị",
                        "formula": "Δ_Q = Q_3 − Q_1",
                        "note": "Đo độ phân tán của 50% dữ liệu trung tâm."
                    }
                ]
            }
        ],
        "meaning": "Thống kê giúp biến dữ liệu thô thành thông tin có thể sử dụng để phân tích.",
        "real_life": "Được sử dụng trong khảo sát, kinh doanh, khoa học, thể thao và phân tích dữ liệu."
    },

    # =========================================================
    # TOÁN 11
    # =========================================================

    (11, "ham-so"): {
        "description": "Hàm số ở lớp 11 mở rộng việc nghiên cứu các hàm lượng giác và các tính chất biến thiên.",
        "definition": "Hàm số lượng giác mô tả các quan hệ giữa góc và các giá trị sin, cos, tan, cot.",
        "concept": "Cần nắm tập xác định, chu kỳ, tính chẵn lẻ, giá trị đặc biệt và đồ thị.",
        "formulas": [
            {
                "category": "Công thức lượng giác cơ bản",
                "items": [
                    {
                        "name": "Hệ thức cơ bản",
                        "formula": "sin²x + cos²x = 1",
                        "note": "Công thức nền tảng của lượng giác."
                    },
                    {
                        "name": "Tang",
                        "formula": "tan x = sin x / cos x",
                        "note": "Điều kiện cos x ≠ 0."
                    },
                    {
                        "name": "Cotang",
                        "formula": "cot x = cos x / sin x",
                        "note": "Điều kiện sin x ≠ 0."
                    }
                ]
            },
            {
                "category": "Công thức cộng",
                "items": [
                    {
                        "name": "Sin tổng",
                        "formula": "sin(a+b)=sin a cos b + cos a sin b",
                        "note": ""
                    },
                    {
                        "name": "Cos tổng",
                        "formula": "cos(a+b)=cos a cos b − sin a sin b",
                        "note": ""
                    }
                ]
            }
        ],
        "meaning": "Hàm lượng giác giúp mô hình hóa các hiện tượng tuần hoàn.",
        "real_life": "Xuất hiện trong sóng âm, dao động, tín hiệu điện và chuyển động tuần hoàn."
    },

    (11, "gioi-han"): {
        "description": "Giới hạn mô tả xu hướng của một hàm số hoặc dãy số khi biến tiến tới một giá trị.",
        "definition": "Giới hạn cho biết giá trị mà một đại lượng tiến gần tới khi biến số tiến gần một điểm hoặc vô cực.",
        "concept": "Giới hạn là nền tảng để xây dựng khái niệm đạo hàm và liên tục.",
        "formulas": [
            {
                "category": "Giới hạn cơ bản",
                "items": [
                    {
                        "name": "Giới hạn tổng",
                        "formula": "lim(f(x)+g(x)) = lim f(x) + lim g(x)",
                        "note": "Khi các giới hạn ở vế phải tồn tại."
                    },
                    {
                        "name": "Giới hạn tích",
                        "formula": "lim(f(x)g(x)) = lim f(x) · lim g(x)",
                        "note": ""
                    },
                    {
                        "name": "Giới hạn thương",
                        "formula": "lim(f(x)/g(x)) = lim f(x)/lim g(x)",
                        "note": "Mẫu khác 0 tại giới hạn."
                    }
                ]
            },
            {
                "category": "Giới hạn đặc biệt",
                "items": [
                    {
                        "name": "Giới hạn lượng giác",
                        "formula": "lim(x→0) sin x/x = 1",
                        "note": "Góc x tính theo radian."
                    }
                ]
            }
        ],
        "meaning": "Giới hạn là cầu nối giữa đại số và giải tích.",
        "real_life": "Giúp mô tả những quá trình thay đổi liên tục và các đại lượng tiến gần đến một giá trị."
    },

    (11, "dao-ham"): {
        "description": "Đạo hàm mô tả tốc độ thay đổi tức thời của một hàm số.",
        "definition": "Đạo hàm của hàm số tại một điểm là giới hạn của tỉ số giữa độ biến thiên của hàm số và độ biến thiên của biến số.",
        "concept": "Đạo hàm có thể được hiểu là hệ số góc của tiếp tuyến với đồ thị tại một điểm.",
        "formulas": [
            {
                "category": "Định nghĩa",
                "items": [
                    {
                        "name": "Đạo hàm tại một điểm",
                        "formula": "f'(x)=lim(h→0)[f(x+h)−f(x)]/h",
                        "note": "Đây là định nghĩa cơ bản."
                    }
                ]
            },
            {
                "category": "Quy tắc đạo hàm",
                "items": [
                    {
                        "name": "Hằng số",
                        "formula": "(C)' = 0",
                        "note": ""
                    },
                    {
                        "name": "Lũy thừa",
                        "formula": "(x^n)' = n x^(n−1)",
                        "note": ""
                    },
                    {
                        "name": "Tổng",
                        "formula": "(f+g)' = f' + g'",
                        "note": ""
                    },
                    {
                        "name": "Tích",
                        "formula": "(fg)' = f'g + fg'",
                        "note": ""
                    },
                    {
                        "name": "Thương",
                        "formula": "(f/g)' = (f'g − fg')/g²",
                        "note": "g(x) ≠ 0."
                    }
                ]
            },
            {
                "category": "Đạo hàm hàm cơ bản",
                "items": [
                    {
                        "name": "Hàm mũ",
                        "formula": "(e^x)' = e^x",
                        "note": ""
                    },
                    {
                        "name": "Logarit",
                        "formula": "(ln x)' = 1/x",
                        "note": "x > 0."
                    },
                    {
                        "name": "Sin",
                        "formula": "(sin x)' = cos x",
                        "note": ""
                    },
                    {
                        "name": "Cos",
                        "formula": "(cos x)' = −sin x",
                        "note": ""
                    }
                ]
            }
        ],
        "meaning": "Đạo hàm cho biết tốc độ thay đổi tức thời và giúp nghiên cứu tính đơn điệu, cực trị của hàm số.",
        "real_life": "Đạo hàm được dùng để tính vận tốc tức thời, gia tốc, tốc độ tăng trưởng và tối ưu hóa."
    },

    (11, "hinh-hoc"): {
        "description": "Hình học không gian nghiên cứu điểm, đường thẳng, mặt phẳng và quan hệ giữa chúng trong không gian.",
        "definition": "Không gian ba chiều được mô tả bởi các đối tượng hình học và quan hệ song song, vuông góc, cắt nhau.",
        "concept": "Các quan hệ quan trọng gồm song song, vuông góc, góc và khoảng cách.",
        "formulas": [
            {
                "category": "Khối đa diện",
                "items": [
                    {
                        "name": "Thể tích hình hộp chữ nhật",
                        "formula": "V = abc",
                        "note": "a, b, c là ba kích thước."
                    },
                    {
                        "name": "Thể tích hình chóp",
                        "formula": "V = 1/3 Sh",
                        "note": "S là diện tích đáy."
                    },
                    {
                        "name": "Thể tích lăng trụ",
                        "formula": "V = Sh",
                        "note": ""
                    }
                ]
            },
            {
                "category": "Góc và khoảng cách",
                "items": [
                    {
                        "name": "Khoảng cách",
                        "formula": "d(M,α)",
                        "note": "Khoảng cách từ điểm đến mặt phẳng."
                    }
                ]
            }
        ],
        "meaning": "Hình học không gian giúp mô tả và tính toán các vật thể ba chiều.",
        "real_life": "Ứng dụng trong kiến trúc, xây dựng, cơ khí, thiết kế nội thất và mô hình 3D."
    },

    (11, "xac-suat"): {
        "description": "Xác suất đo mức độ có khả năng xảy ra của một biến cố.",
        "definition": "Xác suất của biến cố A là một số trong đoạn từ 0 đến 1 biểu thị khả năng xảy ra của A.",
        "concept": "Cần phân biệt không gian mẫu, biến cố, biến cố đối và các quy tắc tính xác suất.",
        "formulas": [
            {
                "category": "Xác suất cơ bản",
                "items": [
                    {
                        "name": "Xác suất cổ điển",
                        "formula": "P(A)=n(A)/n(Ω)",
                        "note": "Các kết quả sơ cấp có khả năng xảy ra như nhau."
                    },
                    {
                        "name": "Biến cố đối",
                        "formula": "P(Ā)=1−P(A)",
                        "note": ""
                    }
                ]
            },
            {
                "category": "Quy tắc xác suất",
                "items": [
                    {
                        "name": "Cộng",
                        "formula": "P(A∪B)=P(A)+P(B)−P(A∩B)",
                        "note": ""
                    },
                    {
                        "name": "Hai biến cố xung khắc",
                        "formula": "P(A∪B)=P(A)+P(B)",
                        "note": "Khi A∩B=∅."
                    }
                ]
            }
        ],
        "meaning": "Xác suất giúp định lượng sự không chắc chắn.",
        "real_life": "Được dùng trong bảo hiểm, thống kê, tài chính, trò chơi và đánh giá rủi ro."
    },

    (11, "thong-ke"): {
        "description": "Thống kê giúp phân tích dữ liệu và rút ra thông tin từ một tập dữ liệu.",
        "definition": "Dữ liệu thống kê là các giá trị được thu thập để nghiên cứu một đặc điểm của đối tượng.",
        "concept": "Các đại lượng đặc trưng giúp đánh giá xu hướng trung tâm và mức độ phân tán.",
        "formulas": [
            {
                "category": "Số trung bình",
                "items": [
                    {
                        "name": "Trung bình cộng",
                        "formula": "x̄ = (Σx_i)/n",
                        "note": ""
                    }
                ]
            },
            {
                "category": "Độ phân tán",
                "items": [
                    {
                        "name": "Khoảng biến thiên",
                        "formula": "R=x_max−x_min",
                        "note": ""
                    },
                    {
                        "name": "Phương sai",
                        "formula": "s²=(1/n)Σ(x_i−x̄)²",
                        "note": "Đo mức độ phân tán của dữ liệu quanh giá trị trung bình."
                    },
                    {
                        "name": "Độ lệch chuẩn",
                        "formula": "s=√s²",
                        "note": ""
                    }
                ]
            }
        ],
        "meaning": "Các đại lượng thống kê giúp so sánh và đánh giá dữ liệu.",
        "real_life": "Ứng dụng trong nghiên cứu khoa học, khảo sát, kinh doanh và phân tích kết quả học tập."
    },

    # =========================================================
    # TOÁN 12
    # =========================================================

    (12, "ham-so"): {
        "description": "Khảo sát hàm số nghiên cứu toàn diện đặc điểm của hàm thông qua đạo hàm và đồ thị.",
        "definition": "Khảo sát hàm số thường gồm tập xác định, giới hạn, đạo hàm, tính đơn điệu, cực trị, tiệm cận và đồ thị.",
        "concept": "Đạo hàm giúp xác định khoảng đồng biến, nghịch biến và các điểm cực trị.",
        "formulas": [
            {
                "category": "Đạo hàm",
                "items": [
                    {
                        "name": "Điều kiện cực trị",
                        "formula": "f'(x₀)=0",
                        "note": "Đây là điều kiện cần trong nhiều trường hợp, không phải điều kiện đủ."
                    },
                    {
                        "name": "Đồng biến",
                        "formula": "f'(x)>0",
                        "note": "Nếu đạo hàm dương trên một khoảng thì hàm số đồng biến trên khoảng đó."
                    },
                    {
                        "name": "Nghịch biến",
                        "formula": "f'(x)<0",
                        "note": "Nếu đạo hàm âm trên một khoảng thì hàm số nghịch biến trên khoảng đó."
                    }
                ]
            },
            {
                "category": "Tiệm cận",
                "items": [
                    {
                        "name": "Tiệm cận đứng",
                        "formula": "lim(x→x₀)f(x)=±∞",
                        "note": "Đường thẳng x=x₀ có thể là tiệm cận đứng."
                    },
                    {
                        "name": "Tiệm cận ngang",
                        "formula": "lim(x→±∞)f(x)=L",
                        "note": "Đường thẳng y=L là tiệm cận ngang."
                    }
                ]
            }
        ],
        "meaning": "Khảo sát hàm số cho phép dự đoán và mô tả hình dạng đồ thị.",
        "real_life": "Được dùng trong tối ưu hóa, mô hình hóa kinh tế và phân tích các đại lượng thay đổi."
    },

    (12, "nguyen-ham"): {
        "description": "Nguyên hàm là khái niệm ngược với đạo hàm.",
        "definition": "F là nguyên hàm của f trên khoảng K nếu F'(x)=f(x) với mọi x thuộc K.",
        "concept": "Tập hợp các nguyên hàm của cùng một hàm số sai khác nhau một hằng số.",
        "formulas": [
            {
                "category": "Nguyên hàm cơ bản",
                "items": [
                    {
                        "name": "Lũy thừa",
                        "formula": "∫x^n dx = x^(n+1)/(n+1)+C, n≠−1",
                        "note": ""
                    },
                    {
                        "name": "Hàm mũ",
                        "formula": "∫e^x dx = e^x + C",
                        "note": ""
                    },
                    {
                        "name": "Hàm 1/x",
                        "formula": "∫1/x dx = ln|x| + C",
                        "note": "x ≠ 0."
                    },
                    {
                        "name": "Hàm sin",
                        "formula": "∫sin x dx = −cos x + C",
                        "note": ""
                    },
                    {
                        "name": "Hàm cos",
                        "formula": "∫cos x dx = sin x + C",
                        "note": ""
                    }
                ]
            },
            {
                "category": "Tính chất",
                "items": [
                    {
                        "name": "Tuyến tính",
                        "formula": "∫[af(x)+bg(x)]dx = a∫f(x)dx+b∫g(x)dx",
                        "note": ""
                    }
                ]
            }
        ],
        "meaning": "Nguyên hàm là công cụ cơ bản để đi từ tốc độ thay đổi về đại lượng ban đầu.",
        "real_life": "Nếu biết vận tốc theo thời gian, nguyên hàm có thể giúp tìm quãng đường."
    },

    (12, "hinh-hoc"): {
        "description": "Hình học không gian lớp 12 tập trung vào việc mô hình hóa không gian bằng tọa độ.",
        "definition": "Trong hệ tọa độ Oxyz, mỗi điểm được biểu diễn bởi ba tọa độ.",
        "concept": "Các nội dung quan trọng gồm phương trình mặt phẳng, đường thẳng, mặt cầu và khoảng cách.",
        "formulas": [
            {
                "category": "Khoảng cách trong Oxyz",
                "items": [
                    {
                        "name": "Khoảng cách hai điểm",
                        "formula": "AB=√((x_B−x_A)²+(y_B−y_A)²+(z_B−z_A)²)",
                        "note": ""
                    }
                ]
            },
            {
                "category": "Mặt phẳng",
                "items": [
                    {
                        "name": "Phương trình mặt phẳng",
                        "formula": "Ax+By+Cz+D=0",
                        "note": "(A,B,C) là một vectơ pháp tuyến."
                    },
                    {
                        "name": "Khoảng cách điểm đến mặt phẳng",
                        "formula": "d(M,(P))=|Ax_M+By_M+Cz_M+D|/√(A²+B²+C²)",
                        "note": ""
                    }
                ]
            },
            {
                "category": "Mặt cầu",
                "items": [
                    {
                        "name": "Phương trình mặt cầu",
                        "formula": "(x−a)²+(y−b)²+(z−c)²=R²",
                        "note": "Tâm I(a,b,c), bán kính R."
                    }
                ]
            }
        ],
        "meaning": "Hệ tọa độ Oxyz giúp giải quyết các bài toán không gian bằng phương pháp đại số.",
        "real_life": "Ứng dụng trong thiết kế 3D, robot, kỹ thuật, mô phỏng không gian và định vị."
    },

    (12, "xac-suat"): {
        "description": "Xác suất lớp 12 mở rộng cách tính xác suất và mô hình hóa các hiện tượng ngẫu nhiên.",
        "definition": "Xác suất là đại lượng định lượng khả năng xảy ra của một biến cố.",
        "concept": "Các quy tắc xác suất và biến ngẫu nhiên giúp xây dựng mô hình cho các hiện tượng không chắc chắn.",
        "formulas": [
            {
                "category": "Quy tắc xác suất",
                "items": [
                    {
                        "name": "Biến cố đối",
                        "formula": "P(Ā)=1−P(A)",
                        "note": ""
                    },
                    {
                        "name": "Cộng xác suất",
                        "formula": "P(A∪B)=P(A)+P(B)−P(A∩B)",
                        "note": ""
                    }
                ]
            },
            {
                "category": "Xác suất có điều kiện",
                "items": [
                    {
                        "name": "Xác suất có điều kiện",
                        "formula": "P(A|B)=P(A∩B)/P(B)",
                        "note": "P(B)>0."
                    },
                    {
                        "name": "Công thức nhân",
                        "formula": "P(A∩B)=P(B)P(A|B)",
                        "note": ""
                    }
                ]
            }
        ],
        "meaning": "Xác suất giúp đánh giá và xử lý sự không chắc chắn trong các tình huống thực tế.",
        "real_life": "Ứng dụng trong dự báo, bảo hiểm, y tế, tài chính và khoa học dữ liệu."
    },

    (12, "so-phuc"): {
        "description": "Số phức mở rộng tập số thực bằng cách đưa vào đơn vị ảo i.",
        "definition": "Số phức có dạng z=a+bi, trong đó a,b là số thực và i²=−1.",
        "concept": "Có thể biểu diễn số phức trên mặt phẳng phức và thực hiện các phép toán đại số.",
        "formulas": [
            {
                "category": "Dạng đại số",
                "items": [
                    {
                        "name": "Dạng đại số",
                        "formula": "z=a+bi",
                        "note": "a là phần thực, b là phần ảo."
                    },
                    {
                        "name": "Môđun",
                        "formula": "|z|=√(a²+b²)",
                        "note": ""
                    },
                    {
                        "name": "Số phức liên hợp",
                        "formula": "z̄=a−bi",
                        "note": ""
                    }
                ]
            },
            {
                "category": "Phép toán",
                "items": [
                    {
                        "name": "Cộng",
                        "formula": "(a+bi)+(c+di)=(a+c)+(b+d)i",
                        "note": ""
                    },
                    {
                        "name": "Nhân",
                        "formula": "(a+bi)(c+di)=(ac−bd)+(ad+bc)i",
                        "note": "Sử dụng i²=−1."
                    }
                ]
            }
        ],
        "meaning": "Số phức giúp mở rộng hệ thống số và giải được những phương trình không có nghiệm thực.",
        "real_life": "Số phức xuất hiện trong kỹ thuật điện, xử lý tín hiệu và mô hình hóa dao động."
    },

    (12, "on-tap-thpt"): {
        "description": "Ôn tập Toán THPT tổng hợp các kiến thức quan trọng từ đại số, giải tích, hình học và xác suất.",
        "definition": "Đây là bài tổng hợp nhằm kết nối các chủ đề và kỹ năng toán học quan trọng.",
        "concept": "Cần biết nhận dạng dạng bài, lựa chọn công cụ và kiểm tra kết quả.",
        "formulas": [
            {
                "category": "Giải tích",
                "items": [
                    {
                        "name": "Đạo hàm",
                        "formula": "f'(x)",
                        "note": "Dùng để nghiên cứu biến thiên và cực trị."
                    },
                    {
                        "name": "Nguyên hàm",
                        "formula": "∫f(x)dx=F(x)+C",
                        "note": "F'(x)=f(x)."
                    }
                ]
            },
            {
                "category": "Hình học",
                "items": [
                    {
                        "name": "Khoảng cách hai điểm Oxyz",
                        "formula": "AB=√((x_B−x_A)²+(y_B−y_A)²+(z_B−z_A)²)",
                        "note": ""
                    }
                ]
            },
            {
                "category": "Xác suất",
                "items": [
                    {
                        "name": "Xác suất biến cố đối",
                        "formula": "P(Ā)=1−P(A)",
                        "note": ""
                    }
                ]
            }
        ],
        "meaning": "Ôn tập giúp kết nối kiến thức thành một hệ thống thay vì học từng công thức riêng lẻ.",
        "real_life": "Kỹ năng lựa chọn công cụ toán học cũng được sử dụng khi giải quyết các bài toán thực tế."
    }
}


def update_lessons():

    with SessionLocal() as db:

        lessons = list(
            db.scalars(
                select(Lesson)
                .where(Lesson.grade >= 10)
                .order_by(Lesson.grade, Lesson.id)
            ).all()
        )

        updated = 0
        skipped = 0

        print(f"Tim thay {len(lessons)} bai Toan lop 10-12.")
        print()

        for lesson in lessons:

            key = (lesson.grade, lesson.topic)

            if key not in DATA:
                print(
                    f"[BO QUA] Lop {lesson.grade} | "
                    f"{lesson.topic} | {lesson.title}"
                )
                skipped += 1
                continue

            content = DATA[key]

            lesson.description = content["description"]
            lesson.definition = content["definition"]
            lesson.concept = content["concept"]
            lesson.formulas = content["formulas"]
            lesson.meaning = content["meaning"]
            lesson.real_life = content["real_life"]

            updated += 1

            print(
                f"[OK] Lop {lesson.grade} | "
                f"{lesson.topic} | {lesson.title}"
            )

        db.commit()

        print()
        print("=" * 60)
        print(f"DA CAP NHAT: {updated} BAI")
        print(f"BO QUA: {skipped} BAI")
        print("=" * 60)


if __name__ == "__main__":
    update_lessons()