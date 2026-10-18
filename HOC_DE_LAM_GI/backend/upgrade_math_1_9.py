"""
Nâng cấp nội dung 45 bài Toán lớp 1-9.

Cấu trúc mỗi bài:
- definition : định nghĩa
- concept    : kiến thức trọng tâm
- formulas   : công thức
- meaning    : ý nghĩa
- real_life  : ứng dụng thực tế

Chạy:
    python upgrade_math_1_9.py
"""

from database.database import SessionLocal
from models.lesson import Lesson

def to_formula_list(text):
    if not text:
        return []

    return [
        line.strip()
        for line in text.strip().splitlines()
        if line.strip()
    ]

LESSONS = {

    # =========================================================
    # LỚP 1
    # =========================================================

    (1, "so-hoc"): {
        "definition": "Số tự nhiên dùng để đếm số lượng đồ vật và biểu thị thứ tự. Ở lớp 1, học sinh làm quen với các số trong phạm vi 100.",
        "concept": """
Nhận biết và đọc viết số tự nhiên.
So sánh số lớn hơn, nhỏ hơn, bằng nhau.
Hiểu số lượng tương ứng với một nhóm đồ vật.
Biết số liền trước, số liền sau.
Biết tách và gộp số thành các phần.
""",
        "formulas": """
Số liền trước của n: n - 1
Số liền sau của n: n + 1

Ví dụ:
5 = 2 + 3
7 = 5 + 2
10 = 6 + 4

So sánh:
a > b: a lớn hơn b
a < b: a nhỏ hơn b
a = b: a bằng b
""",
        "meaning": "Giúp học sinh hình thành tư duy về số lượng, thứ tự và khả năng so sánh trong cuộc sống.",
        "real_life": "Dùng để đếm đồ vật, đếm tiền, đếm số người, số sản phẩm, số bước đi hoặc thứ tự của một vật."
    },

    (1, "phep-cong"): {
        "definition": "Phép cộng là phép toán dùng để gộp hai hoặc nhiều nhóm lại với nhau để tìm tổng số lượng.",
        "concept": """
Hiểu ý nghĩa của dấu cộng (+).
Biết cộng trong phạm vi đã học.
Nhận biết số hạng và tổng.
Có thể sử dụng đồ vật hoặc hình ảnh để thực hiện phép cộng.
""",
        "formulas": """
a + b = c

Trong đó:
a, b là các số hạng
c là tổng

Tính chất:
a + 0 = a
a + b = b + a
""",
        "meaning": "Phép cộng mô tả việc nhiều nhóm được gộp thành một nhóm lớn hơn.",
        "real_life": "Tính tổng số tiền khi mua nhiều món đồ, tổng số học sinh trong các nhóm hoặc tổng số sản phẩm."
    },

    (1, "phep-tru"): {
        "definition": "Phép trừ là phép toán dùng để lấy bớt một phần khỏi một số lượng ban đầu.",
        "concept": """
Hiểu ý nghĩa của dấu trừ (-).
Biết tìm phần còn lại.
Biết mối quan hệ giữa số bị trừ, số trừ và hiệu.
""",
        "formulas": """
a - b = c

a là số bị trừ
b là số trừ
c là hiệu

a - 0 = a
a - a = 0
""",
        "meaning": "Phép trừ giúp mô tả việc lấy đi, giảm đi hoặc tìm phần còn thiếu.",
        "real_life": "Tính số tiền còn lại sau khi mua hàng, số đồ vật còn lại hoặc lượng nước còn trong bình."
    },

    (1, "do-luong"): {
        "definition": "Đo lường là quá trình dùng đơn vị để xác định độ dài, khối lượng, thời gian hoặc lượng của một đại lượng.",
        "concept": """
Nhận biết độ dài.
Biết sử dụng thước.
Nhận biết các đơn vị quen thuộc như cm, m.
Nhận biết thời gian qua giờ và ngày.
""",
        "formulas": """
1 m = 100 cm
1 cm = 10 mm
1 giờ = 60 phút
1 ngày = 24 giờ
""",
        "meaning": "Đo lường giúp con người mô tả chính xác kích thước, thời gian và số lượng thay vì chỉ ước lượng.",
        "real_life": "Đo chiều cao, đo chiều dài bàn, xem giờ, đo khoảng cách hoặc kiểm tra kích thước đồ vật."
    },

    (1, "hinh-hoc"): {
        "definition": "Hình học nghiên cứu hình dạng, vị trí và đặc điểm của các vật thể trong không gian.",
        "concept": """
Nhận biết hình vuông, hình chữ nhật, hình tam giác và hình tròn.
Nhận biết cạnh, góc và các đặc điểm đơn giản của hình.
Nhận biết vị trí trên, dưới, trái, phải.
""",
        "formulas": """
Hình vuông có 4 cạnh bằng nhau.
Hình chữ nhật có 4 góc vuông.
Hình tam giác có 3 cạnh.
Hình tròn có tâm và đường tròn bao quanh tâm.
""",
        "meaning": "Giúp trẻ nhận biết hình dạng và vị trí của các vật trong thế giới thực.",
        "real_life": "Nhận dạng cửa sổ, biển báo, bánh xe, mặt bàn, hộp và các vật dụng xung quanh."
    },


    # =========================================================
    # LỚP 2
    # =========================================================

    (2, "so-hoc"): {
        "definition": "Số học nghiên cứu các số tự nhiên và những quan hệ cơ bản giữa chúng.",
        "concept": """
Đọc và viết số trong phạm vi lớn hơn.
So sánh số.
Phân tích số theo hàng đơn vị, chục, trăm.
Nhận biết số chẵn và số lẻ đơn giản.
""",
        "formulas": """
100 = 1 trăm
10 = 1 chục
1 chục = 10 đơn vị

Số chẵn chia hết cho 2.
Số lẻ không chia hết cho 2.
""",
        "meaning": "Giúp học sinh hiểu cấu tạo của số và sử dụng số trong các tình huống thực tế.",
        "real_life": "Đọc giá tiền, số nhà, số lượng sản phẩm, số trang sách và số lượng người."
    },

    (2, "phep-cong"): {
        "definition": "Phép cộng dùng để gộp các số lượng thành một tổng.",
        "concept": """
Cộng có nhớ trong phạm vi đã học.
Đặt tính theo hàng.
Tính tổng nhiều số.
Kiểm tra kết quả bằng phép tính ngược.
""",
        "formulas": """
a + b = b + a
(a + b) + c = a + (b + c)
a + 0 = a
""",
        "meaning": "Phép cộng giúp tổng hợp nhiều lượng riêng lẻ thành một lượng chung.",
        "real_life": "Tính tổng tiền, tổng sản phẩm, tổng khoảng cách hoặc tổng thời gian."
    },

    (2, "phep-tru"): {
        "definition": "Phép trừ dùng để tìm phần còn lại hoặc sự chênh lệch giữa hai số.",
        "concept": """
Trừ có nhớ.
Đặt tính theo hàng.
Tìm số chưa biết.
Liên hệ phép cộng và phép trừ.
""",
        "formulas": """
a - b = c
a - 0 = a
a - a = 0

Nếu a - b = c thì:
a - c = b
b + c = a
""",
        "meaning": "Giúp xác định lượng còn lại hoặc lượng chênh lệch.",
        "real_life": "Tính tiền thừa, số hàng còn lại, tuổi chênh lệch hoặc khoảng cách còn thiếu."
    },

    (2, "phep-nhan"): {
        "definition": "Phép nhân là cách viết gọn của phép cộng nhiều số giống nhau.",
        "concept": """
Hiểu phép nhân thông qua các nhóm bằng nhau.
Học bảng nhân cơ bản.
Nhận biết thừa số và tích.
""",
        "formulas": """
a × b = a + a + ... + a (b lần)

a × 1 = a
a × 0 = 0
a × b = b × a
""",
        "meaning": "Phép nhân giúp tính nhanh khi có nhiều nhóm có cùng số lượng.",
        "real_life": "Tính số bánh trong nhiều hộp, số ghế trong các hàng hoặc tổng số sản phẩm."
    },

    (2, "dai-luong"): {
        "definition": "Đại lượng là những đặc điểm có thể đo được như độ dài, khối lượng và thời gian.",
        "concept": """
Đo độ dài.
Đo khối lượng.
Xem giờ.
Nhận biết đơn vị đo.
""",
        "formulas": """
1 m = 100 cm
1 kg = 1000 g
1 giờ = 60 phút
1 ngày = 24 giờ
""",
        "meaning": "Giúp mô tả chính xác kích thước, khối lượng và thời gian.",
        "real_life": "Cân thực phẩm, đo chiều dài, xem lịch, tính thời gian di chuyển."
    },


    # =========================================================
    # LỚP 3
    # =========================================================

    (3, "so-tu-nhien"): {
        "definition": "Số tự nhiên là các số dùng để đếm và xác định thứ tự.",
        "concept": """
Đọc viết số đến hàng nghìn.
So sánh và sắp xếp số.
Cấu tạo số theo hàng.
Làm tròn số ở mức đơn giản.
""",
        "formulas": """
1 nghìn = 10 trăm
1 trăm = 10 chục
1 chục = 10 đơn vị
""",
        "meaning": "Giúp biểu diễn số lượng lớn hơn và xử lý các dữ liệu thường gặp.",
        "real_life": "Đếm dân số, số hàng trong kho, số tiền hoặc số lượng sản phẩm."
    },

    (3, "phep-nhan"): {
        "definition": "Phép nhân là phép toán biểu diễn nhiều nhóm có cùng số lượng.",
        "concept": """
Thực hiện phép nhân số có nhiều chữ số.
Sử dụng bảng nhân.
Giải bài toán có lời văn bằng phép nhân.
""",
        "formulas": """
a × b = b × a
a × (b + c) = a×b + a×c
a × 1 = a
a × 0 = 0
""",
        "meaning": "Giúp tính nhanh tổng của các nhóm bằng nhau.",
        "real_life": "Tính sản lượng, số lượng hàng hóa, diện tích theo hàng và cột."
    },

    (3, "phep-chia"): {
        "definition": "Phép chia dùng để chia một số thành các phần bằng nhau hoặc xác định một số chứa được bao nhiêu nhóm.",
        "concept": """
Nhận biết số bị chia, số chia và thương.
Chia hết và chia có dư.
Liên hệ giữa phép nhân và phép chia.
""",
        "formulas": """
a : b = c

Nếu a : b = c thì:
a = b × c

Số bị chia = số chia × thương + số dư
""",
        "meaning": "Giúp phân chia công bằng hoặc xác định số nhóm có thể tạo ra.",
        "real_life": "Chia bánh cho mọi người, chia tiền, đóng gói sản phẩm hoặc phân nhóm học sinh."
    },

    (3, "hinh-hoc"): {
        "definition": "Hình học nghiên cứu các hình và đặc điểm hình dạng của chúng.",
        "concept": """
Nhận biết điểm, đoạn thẳng.
Nhận biết góc.
Nhận biết hình chữ nhật, hình vuông.
Tính chu vi đơn giản.
""",
        "formulas": """
Chu vi hình chữ nhật:
P = (a + b) × 2

Chu vi hình vuông:
P = 4a
""",
        "meaning": "Giúp đo và mô tả hình dạng, kích thước của các vật thể.",
        "real_life": "Tính lượng dây cần quây sân, khung ảnh, hàng rào hoặc viền bàn."
    },

    (3, "du-lieu"): {
        "definition": "Dữ liệu là những thông tin được thu thập để mô tả một sự vật hoặc hiện tượng.",
        "concept": """
Thu thập dữ liệu.
Đọc bảng.
Đọc biểu đồ tranh và biểu đồ đơn giản.
So sánh số liệu.
""",
        "formulas": """
Tổng số = tổng các giá trị thành phần.

Ví dụ:
Số học sinh nam + số học sinh nữ
= tổng số học sinh.
""",
        "meaning": "Giúp biến thông tin thực tế thành dạng dễ quan sát và so sánh.",
        "real_life": "Thống kê điểm số, số học sinh, thời tiết, doanh số hoặc kết quả khảo sát."
    },


    # =========================================================
    # LỚP 4
    # =========================================================

    (4, "so-tu-nhien"): {
        "definition": "Số tự nhiên được sử dụng để biểu diễn các đại lượng và thứ tự trong thực tế.",
        "concept": """
Đọc viết số lớn.
Hàng và lớp của số.
So sánh số.
Làm tròn số.
Thực hiện bốn phép tính.
""",
        "formulas": """
1 lớp đơn vị = hàng đơn vị, chục, trăm
1 lớp nghìn = hàng nghìn, chục nghìn, trăm nghìn

a + b = tổng
a - b = hiệu
a × b = tích
a : b = thương
""",
        "meaning": "Tạo nền tảng cho các phép tính và mô hình hóa những lượng lớn.",
        "real_life": "Tính ngân sách, số lượng hàng hóa, dân số và các dữ liệu lớn."
    },

    (4, "phan-so"): {
        "definition": "Phân số biểu diễn một hoặc nhiều phần bằng nhau của một đơn vị.",
        "concept": """
Nhận biết tử số và mẫu số.
Đọc phân số.
So sánh phân số.
Phân số bằng nhau.
""",
        "formulas": """
a/b với b ≠ 0

a/b = (a×n)/(b×n)

Nếu cùng mẫu:
a/b > c/b khi a > c
""",
        "meaning": "Giúp biểu diễn những lượng không nguyên hoặc một phần của một tổng thể.",
        "real_life": "Chia bánh, chia thời gian, biểu diễn phần trăm diện tích hoặc khối lượng."
    },

    (4, "hinh-hoc"): {
        "definition": "Hình học nghiên cứu các hình phẳng và quan hệ về độ dài, góc và diện tích.",
        "concept": """
Góc.
Đường thẳng.
Hình chữ nhật.
Hình vuông.
Diện tích hình chữ nhật và hình vuông.
""",
        "formulas": """
Hình chữ nhật:
P = 2(a+b)
S = a×b

Hình vuông:
P = 4a
S = a²
""",
        "meaning": "Giúp tính kích thước và diện tích của các khu vực trong thực tế.",
        "real_life": "Tính diện tích phòng, nền nhà, sân vườn và lượng vật liệu cần dùng."
    },

    (4, "dai-luong"): {
        "definition": "Đại lượng là những thuộc tính có thể đo bằng các đơn vị xác định.",
        "concept": """
Độ dài.
Khối lượng.
Diện tích.
Thời gian.
Đổi đơn vị.
""",
        "formulas": """
1 km = 1000 m
1 m = 100 cm
1 kg = 1000 g
1 m² = 10000 cm²
1 giờ = 60 phút
""",
        "meaning": "Giúp chuyển đổi và tính toán các đại lượng trong đời sống.",
        "real_life": "Đo đường đi, cân hàng, tính diện tích đất và tính thời gian."
    },

    (4, "bieu-do"): {
        "definition": "Biểu đồ là cách trình bày dữ liệu bằng hình ảnh để dễ quan sát và so sánh.",
        "concept": """
Đọc biểu đồ cột.
Đọc biểu đồ tranh.
So sánh dữ liệu.
Tính tổng và hiệu từ biểu đồ.
""",
        "formulas": """
Tổng = cộng các giá trị.
Chênh lệch = giá trị lớn - giá trị nhỏ.
""",
        "meaning": "Giúp con người nhìn thấy xu hướng và sự khác biệt giữa các dữ liệu.",
        "real_life": "Theo dõi doanh thu, số học sinh, nhiệt độ, điểm kiểm tra và thống kê thể thao."
    },


    # =========================================================
    # LỚP 5
    # =========================================================

    (5, "so-thap-phan"): {
        "definition": "Số thập phân dùng để biểu diễn những số có phần nguyên và phần nhỏ hơn một đơn vị.",
        "concept": """
Phần nguyên và phần thập phân.
Đọc viết số thập phân.
So sánh số thập phân.
Cộng, trừ, nhân, chia số thập phân.
""",
        "formulas": """
0,5 = 5/10
0,25 = 25/100

a,b = a + b/10 + ...
""",
        "meaning": "Cho phép biểu diễn chính xác những đại lượng không nguyên.",
        "real_life": "Đo chiều dài 1,5 m, cân 2,5 kg, tính giá tiền và đo nhiệt độ."
    },

    (5, "phan-so"): {
        "definition": "Phân số biểu diễn một phần của đơn vị hoặc thương của hai số nguyên.",
        "concept": """
Phân số tối giản.
Quy đồng mẫu số.
Cộng trừ phân số.
Nhân chia phân số.
""",
        "formulas": """
a/b + c/b = (a+c)/b

a/b × c/d = ac/bd

a/b : c/d = a/b × d/c

a/b = ka/kb
""",
        "meaning": "Giúp tính toán chính xác các phần của một đại lượng.",
        "real_life": "Chia nguyên liệu, chia thời gian, tính phần diện tích và khẩu phần."
    },

    (5, "hinh-hoc"): {
        "definition": "Hình học lớp 5 mở rộng việc tính chu vi, diện tích và thể tích của những hình quen thuộc.",
        "concept": """
Hình tam giác.
Hình thang.
Hình tròn.
Hình hộp chữ nhật.
Hình lập phương.
""",
        "formulas": """
Tam giác:
S = a×h/2

Hình thang:
S = (a+b)×h/2

Hình tròn:
C = 2πr
S = πr²

Hộp chữ nhật:
V = a×b×c
""",
        "meaning": "Giúp tính lượng không gian và diện tích cần thiết cho các vật thể.",
        "real_life": "Tính vật liệu xây dựng, thể tích hộp, diện tích đất và kích thước đồ vật."
    },

    (5, "ti-so"): {
        "definition": "Tỉ số là thương của hai số dùng để so sánh chúng với nhau.",
        "concept": """
Tỉ số của hai số.
Tỉ lệ.
Bài toán tỉ lệ thuận đơn giản.
Tìm giá trị chưa biết.
""",
        "formulas": """
Tỉ số của a và b:
a : b = a/b

Nếu:
a/b = c/d
thì:
ad = bc
""",
        "meaning": "Giúp so sánh các đại lượng theo một cách thống nhất.",
        "real_life": "Tỉ lệ bản đồ, pha nguyên liệu, tốc độ, quy mô mô hình."
    },

    (5, "toan-thuc-te"): {
        "definition": "Toán thực tế là việc sử dụng kiến thức toán học để giải quyết những vấn đề trong đời sống.",
        "concept": """
Đọc đề.
Xác định dữ kiện.
Chọn phép tính.
Kiểm tra kết quả.
""",
        "formulas": """
Tiền còn lại = tiền có - tiền đã dùng

Quãng đường = vận tốc × thời gian

Thời gian = quãng đường : vận tốc
""",
        "meaning": "Giúp học sinh nhận ra toán học không chỉ tồn tại trên giấy mà có thể giải quyết vấn đề thật.",
        "real_life": "Mua sắm, tính quãng đường, chia khẩu phần, lập kế hoạch thời gian và chi tiêu."
    },


    # =========================================================
    # LỚP 6
    # =========================================================

    (6, "so-tu-nhien"): {
        "definition": "Số tự nhiên là nền tảng của hệ thống số và được dùng để đếm, so sánh và thực hiện phép tính.",
        "concept": """
Tập hợp số tự nhiên.
Thứ tự.
Phép cộng, trừ, nhân, chia.
Lũy thừa.
Thứ tự thực hiện phép tính.
""",
        "formulas": """
a^n = a×a×...×a (n thừa số)

a^m × a^n = a^(m+n)

a^m : a^n = a^(m-n), a ≠ 0, m ≥ n
""",
        "meaning": "Tạo nền tảng cho đại số và các phép biến đổi toán học ở cấp cao hơn.",
        "real_life": "Tính toán số lượng, diện tích, dữ liệu và các quy mô lớn."
    },

    (6, "phan-so"): {
        "definition": "Phân số là số có dạng a/b với a và b là số nguyên, b khác 0.",
        "concept": """
Phân số bằng nhau.
Rút gọn.
Quy đồng.
Cộng trừ nhân chia phân số.
""",
        "formulas": """
a/b ± c/d = (ad ± bc)/bd

a/b × c/d = ac/bd

a/b : c/d = ad/bc
""",
        "meaning": "Cho phép xử lý những đại lượng được chia thành nhiều phần bằng nhau.",
        "real_life": "Tính tỉ lệ, khẩu phần, thời gian, vật liệu và các phần của một tổng thể."
    },

    (6, "hinh-hoc"): {
        "definition": "Hình học nghiên cứu điểm, đoạn thẳng, đường thẳng, góc và các hình phẳng.",
        "concept": """
Điểm và đường.
Đoạn thẳng.
Góc.
Tam giác.
Chu vi và diện tích.
""",
        "formulas": """
Hình chữ nhật:
S = ab

Hình vuông:
S = a²

Tam giác:
S = ah/2
""",
        "meaning": "Giúp mô hình hóa hình dạng và kích thước của vật thể.",
        "real_life": "Thiết kế, xây dựng, đo đạc và tính vật liệu."
    },

    (6, "du-lieu"): {
        "definition": "Dữ liệu là tập hợp thông tin được thu thập và tổ chức để phân tích.",
        "concept": """
Bảng dữ liệu.
Biểu đồ.
Thu thập dữ liệu.
Tần số đơn giản.
""",
        "formulas": """
Tổng số quan sát = tổng các tần số.
""",
        "meaning": "Giúp tổ chức thông tin và phát hiện đặc điểm của một tập dữ liệu.",
        "real_life": "Khảo sát lớp học, thống kê điểm, nhiệt độ hoặc kết quả thể thao."
    },

    (6, "tu-duy-logic"): {
        "definition": "Tư duy logic là khả năng sử dụng các điều kiện và lập luận để đi đến kết luận hợp lý.",
        "concept": """
Mệnh đề đơn giản.
Điều kiện.
Suy luận.
Tìm quy luật.
Loại trừ trường hợp sai.
""",
        "formulas": """
Nếu A đúng và A → B
thì B đúng.

Phản ví dụ có thể chứng minh một khẳng định tổng quát là sai.
""",
        "meaning": "Rèn khả năng suy luận thay vì chỉ tính toán.",
        "real_life": "Lập kế hoạch, tìm lỗi, giải câu đố, lập trình và ra quyết định."
    },


    # =========================================================
    # LỚP 7
    # =========================================================

    (7, "so-huu-ti"): {
        "definition": "Số hữu tỉ là số có thể biểu diễn dưới dạng a/b với a, b là số nguyên và b khác 0.",
        "concept": """
Biểu diễn số hữu tỉ.
So sánh số hữu tỉ.
Cộng trừ nhân chia.
Giá trị tuyệt đối.
""",
        "formulas": """
a/b ± c/d = (ad ± bc)/bd

|a| = a nếu a ≥ 0
|a| = -a nếu a < 0
""",
        "meaning": "Mở rộng hệ thống số để xử lý cả số âm và các phân số.",
        "real_life": "Nhiệt độ âm, độ cao dưới mực nước biển, tiền nợ và thay đổi giá trị."
    },

    (7, "dai-so"): {
        "definition": "Đại số sử dụng chữ và biểu thức để biểu diễn các đại lượng chưa biết hoặc tổng quát.",
        "concept": """
Biểu thức đại số.
Đơn thức.
Đa thức.
Giá trị biểu thức.
Quy tắc biến đổi.
""",
        "formulas": """
a(b+c) = ab + ac

(a+b)² = a² + 2ab + b²

(a-b)² = a² - 2ab + b²
""",
        "meaning": "Cho phép mô tả một quy luật cho nhiều trường hợp thay vì tính từng trường hợp riêng.",
        "real_life": "Tính chi phí, diện tích, doanh thu và các mô hình tổng quát."
    },

    (7, "hinh-hoc"): {
        "definition": "Hình học lớp 7 nghiên cứu quan hệ giữa góc, đường thẳng và các hình phẳng.",
        "concept": """
Góc.
Hai đường thẳng song song.
Tam giác.
Quan hệ giữa cạnh và góc.
""",
        "formulas": """
Tổng ba góc tam giác = 180°

Góc kề bù:
a + b = 180°

Góc đối đỉnh bằng nhau.
""",
        "meaning": "Giúp suy luận các kích thước hình học mà không cần đo trực tiếp.",
        "real_life": "Thiết kế, xây dựng, định hướng và đo đạc."
    },

    (7, "thong-ke"): {
        "definition": "Thống kê là quá trình thu thập, tổ chức, phân tích và diễn giải dữ liệu.",
        "concept": """
Thu thập dữ liệu.
Bảng tần số.
Biểu đồ.
Số trung bình.
Nhận xét dữ liệu.
""",
        "formulas": """
Số trung bình cộng:
x̄ = (x₁+x₂+...+xₙ)/n
""",
        "meaning": "Giúp biến nhiều dữ liệu thành thông tin dễ hiểu.",
        "real_life": "Phân tích điểm số, khảo sát, doanh số và dữ liệu thể thao."
    },

    (7, "ung-dung"): {
        "definition": "Toán ứng dụng là việc đưa mô hình toán học vào các tình huống thực tế.",
        "concept": """
Tỉ lệ.
Phần trăm.
Chi phí.
Năng suất.
Quãng đường.
""",
        "formulas": """
Phần trăm:
p% = p/100

Giá sau giảm p%:
Giá mới = Giá cũ × (1-p/100)
""",
        "meaning": "Giúp học sinh thấy toán học trực tiếp hỗ trợ các quyết định đời sống.",
        "real_life": "Mua hàng giảm giá, tính lãi, năng suất lao động và lập ngân sách."
    },


    # =========================================================
    # LỚP 8
    # =========================================================

    (8, "bieu-thuc"): {
        "definition": "Biểu thức đại số là biểu thức chứa số, chữ và các phép toán.",
        "concept": """
Đơn thức.
Đa thức.
Thu gọn.
Cộng trừ đa thức.
Nhân đa thức.
""",
        "formulas": """
a(b+c)=ab+ac

(a+b)(c+d)=ac+ad+bc+bd

(a+b)²=a²+2ab+b²
""",
        "meaning": "Giúp mô tả các mối quan hệ bằng công thức tổng quát.",
        "real_life": "Tính diện tích, chi phí và các mô hình biến đổi theo nhiều đại lượng."
    },

    (8, "phuong-trinh"): {
        "definition": "Phương trình là một đẳng thức chứa một hoặc nhiều ẩn cần tìm.",
        "concept": """
Ẩn.
Nghiệm.
Phương trình bậc nhất.
Biến đổi tương đương.
Giải bài toán bằng phương trình.
""",
        "formulas": """
ax+b=0, a≠0

x=-b/a

Nếu:
A=B
thì có thể cộng, trừ, nhân hoặc chia hai vế với cùng một số khác 0 để tạo phương trình tương đương.
""",
        "meaning": "Cho phép tìm đại lượng chưa biết từ những thông tin đã biết.",
        "real_life": "Tính tuổi, tìm giá sản phẩm, lập kế hoạch và giải bài toán chuyển động."
    },

    (8, "hinh-hoc"): {
        "definition": "Hình học lớp 8 nghiên cứu các quan hệ về diện tích, đồng dạng và các hình phẳng.",
        "concept": """
Tứ giác.
Đa giác.
Định lý Pythagore.
Diện tích.
Tam giác đồng dạng.
""",
        "formulas": """
Định lý Pythagore:
a²+b²=c²

Hình chữ nhật:
S=ab

Tam giác:
S=ah/2
""",
        "meaning": "Giúp tính khoảng cách và kích thước mà không cần đo trực tiếp.",
        "real_life": "Xây dựng, thiết kế mái nhà, đo khoảng cách và kiểm tra góc vuông."
    },

    (8, "thong-ke"): {
        "definition": "Thống kê giúp thu thập và phân tích dữ liệu để đưa ra nhận xét.",
        "concept": """
Bảng số liệu.
Tần số.
Tần số tương đối.
Biểu đồ.
Số trung bình.
""",
        "formulas": """
Tần số tương đối:
f = n/N

Phần trăm:
f% = n/N × 100%
""",
        "meaning": "Giúp đánh giá dữ liệu theo quy mô và tỉ lệ.",
        "real_life": "Khảo sát thị trường, kết quả học tập, dân số và dữ liệu xã hội."
    },

    (8, "logic"): {
        "definition": "Logic và suy luận nghiên cứu cách đưa ra kết luận dựa trên dữ kiện và quy tắc.",
        "concept": """
Điều kiện cần.
Điều kiện đủ.
Suy luận trực tiếp.
Phản chứng.
Phản ví dụ.
""",
        "formulas": """
Nếu A → B và A đúng thì B đúng.

Nếu A → B và B sai thì A sai.
""",
        "meaning": "Giúp kiểm tra tính đúng đắn của một lập luận.",
        "real_life": "Lập trình, phát hiện lỗi, giải quyết vấn đề và ra quyết định."
    },


    # =========================================================
    # LỚP 9
    # =========================================================

    (9, "ham-so"): {
        "definition": "Hàm số mô tả sự phụ thuộc của một đại lượng vào một đại lượng khác.",
        "concept": """
Biến độc lập.
Biến phụ thuộc.
Hàm số.
Bảng giá trị.
Đồ thị.
Hàm số bậc nhất.
""",
        "formulas": """
Hàm số bậc nhất:
y=ax+b, a≠0

Hệ số góc là a.

Nếu a>0: hàm số đồng biến.
Nếu a<0: hàm số nghịch biến.
""",
        "meaning": "Giúp mô tả sự thay đổi của một đại lượng theo đại lượng khác.",
        "real_life": "Quãng đường theo thời gian, tiền điện theo mức sử dụng, chi phí theo số lượng sản phẩm."
    },

    (9, "phuong-trinh"): {
        "definition": "Phương trình là một quan hệ bằng nhau chứa ẩn và cần tìm giá trị của ẩn để quan hệ đúng.",
        "concept": """
Phương trình bậc nhất.
Hệ phương trình.
Phương trình bậc hai.
Giải và kiểm tra nghiệm.
""",
        "formulas": """
ax+b=0:
x=-b/a

ax²+bx+c=0:
Δ=b²-4ac

Nếu Δ>0:
x₁=(-b+√Δ)/(2a)
x₂=(-b-√Δ)/(2a)

Nếu Δ=0:
x=-b/(2a)
""",
        "meaning": "Giúp tìm các đại lượng chưa biết từ mối quan hệ giữa chúng.",
        "real_life": "Tính giá, thời gian, kích thước, quãng đường và bài toán kinh tế."
    },

    (9, "hinh-hoc"): {
        "definition": "Hình học lớp 9 nghiên cứu sâu hơn về tam giác, đường tròn và quan hệ hình học.",
        "concept": """
Hệ thức lượng trong tam giác vuông.
Đường tròn.
Góc nội tiếp.
Tiếp tuyến.
Diện tích và chu vi đường tròn.
""",
        "formulas": """
Định lý Pythagore:
a²+b²=c²

Đường tròn:
C=2πR
S=πR²

Góc nội tiếp chắn nửa đường tròn = 90°.
""",
        "meaning": "Giúp tính khoảng cách, bán kính, diện tích và các đại lượng hình học không dễ đo trực tiếp.",
        "real_life": "Thiết kế bánh xe, đường cong, kiến trúc, xây dựng và đo đạc."
    },

    (9, "can-thuc"): {
        "definition": "Căn thức là biểu thức chứa căn bậc hai của một số hoặc một biểu thức.",
        "concept": """
Căn bậc hai.
Điều kiện xác định.
Rút gọn căn thức.
Đưa thừa số ra ngoài dấu căn.
Khử mẫu.
""",
        "formulas": """
√(a²)=|a|

√(ab)=√a×√b, với a,b≥0

√(a/b)=√a/√b, với a≥0,b>0

(a√b)(c√d)=ac√(bd)
""",
        "meaning": "Giúp biểu diễn chính xác những giá trị liên quan đến độ dài và hình học.",
        "real_life": "Tính đường chéo, khoảng cách, kích thước và các bài toán kỹ thuật."
    },

    (9, "toan-thuc-te"): {
        "definition": "Toán thực tế lớp 9 vận dụng đại số, hình học và hàm số để mô hình hóa các vấn đề đời sống.",
        "concept": """
Chuyển động.
Năng suất.
Kinh tế.
Hình học thực tế.
Hàm số.
Phương trình.
""",
        "formulas": """
s = vt

v = s/t

t = s/v

Năng suất = khối lượng công việc / thời gian

Lợi nhuận = doanh thu - chi phí
""",
        "meaning": "Giúp học sinh biến một tình huống đời sống thành mô hình toán học để giải quyết.",
        "real_life": "Tính thời gian đi đường, tiền điện, lợi nhuận, năng suất và chi phí xây dựng."
    },
}


def update_lessons():
    db = SessionLocal()

    try:
        lessons = db.query(Lesson).filter(Lesson.grade.between(1, 9)).all()

        print(f"Tim thay {len(lessons)} bai hoc Toan lop 1-9.")
        print()

        updated = 0
        skipped = 0

        for lesson in lessons:

            key = (lesson.grade, lesson.topic)

            if key not in LESSONS:
                print(
                    f"[BO QUA] Lop {lesson.grade} | "
                    f"{lesson.topic} | {lesson.title}"
                )
                skipped += 1
                continue

            data = LESSONS[key]

            lesson.definition = data["definition"].strip()
            lesson.concept = data["concept"].strip()
            lesson.formulas = to_formula_list(data["formulas"])
            lesson.meaning = data["meaning"].strip()
            lesson.real_life = data["real_life"].strip()

            # Không bắt buộc game ở bước này.
            # Game sẽ được thiết kế sau khi phần lesson hoàn chỉnh.

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

    except Exception as e:
        db.rollback()

        print()
        print("=" * 60)
        print("LOI KHI CAP NHAT")
        print("=" * 60)
        print(e)

        raise

    finally:
        db.close()


if __name__ == "__main__":
    update_lessons()