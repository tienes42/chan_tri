"""
Upgrade chemistry lesson content for HỌC ĐỂ LÀM GÌ.

Run from backend:
    python upgrade_chemistry.py

Creates/updates 42 Chemistry lessons:
- Grade 6: 6 introductory matter lessons
- Grade 7: 6 introductory chemistry/science lessons
- Grade 8: 6 core chemistry lessons
- Grade 9: 6 inorganic/organic basics
- Grade 10: 6 atomic structure, periodic table, bonding
- Grade 11: 6 reaction speed, equilibrium, inorganic/organic basics
- Grade 12: 6 advanced organic + electrochemistry/polymer basics

The script is idempotent: running it again updates the same lessons by
(subject_id, grade, topic), without creating duplicates.
"""

from database.database import SessionLocal
from models.lesson import Lesson
from models.subject import Subject
from sqlalchemy import select


def L(
    grade,
    topic,
    title,
    icon,
    description,
    context_title,
    context,
    theory,
    formula,
    example,
    example_answer,
    question,
    answers,
    correct,
    application,
    challenge,
    challenge_answer=""
):
   
    return {
        "grade": grade,
        "topic": topic,
        "title": title,
        "icon": icon,
        "description": description,
        "context_title": context_title,
        "context": context,
        "theory": theory,
        "formula": formula,
        "example": example,
        "example_answer": example_answer,
        "question": question,
        "answers": answers,
        "correct": correct,
        "application": application,
        "challenge": challenge,
        "challenge_answer": challenge_answer,
    }


LESSONS = [
# =========================
# GRADE 6
# =========================
L(6, "chat-va-vat-lieu", "Chất và vật liệu", "🧪",
  "Phân biệt chất, vật thể và vật liệu; nhận biết vật liệu quanh ta.",
  "Từ chiếc cốc đến chiếc bàn",
  "Mọi vật quanh ta được tạo nên từ một hay nhiều chất. Một chiếc cốc có thể làm bằng thủy tinh, nhựa hoặc kim loại.",
  "Chất là vật liệu có thành phần và tính chất xác định. Vật thể là đồ vật cụ thể. Tính chất vật lý có thể quan sát/đo mà không tạo chất mới; tính chất hóa học liên quan khả năng tạo chất mới.",
  "Khối lượng riêng: ρ = m/V\nNhiệt độ nóng chảy, sôi là các đại lượng đặc trưng của chất.",
  "Một vật có khối lượng 200 g và thể tích 100 cm³. Tính khối lượng riêng.",
  "ρ = 200/100 = 2 g/cm³.",
  "Đâu là tính chất hóa học?\nA. Nước đông đặc ở 0°C\nB. Sắt bị gỉ\nC. Đồng dẫn điện\nD. Nhôm có màu bạc",
  ["Nước đông đặc ở 0°C", "Sắt bị gỉ", "Đồng dẫn điện", "Nhôm có màu bạc"], 1,
  "Chọn vật liệu làm nồi, dây điện, chai nhựa dựa trên tính chất của chúng.",
  "Vì sao dây điện thường có lõi đồng và lớp vỏ nhựa?",
  "Đồng dẫn điện tốt; nhựa cách điện và giúp bảo vệ người dùng."
),
L(6, "trang-thai-chat", "Ba trạng thái của chất", "💧",
  "Hiểu chất rắn, lỏng, khí và sự chuyển thể.",
  "Nước trong đời sống",
  "Nước đá, nước lỏng và hơi nước đều là H2O nhưng có trạng thái vật chất khác nhau.",
  "Chất rắn có hình dạng và thể tích xác định; chất lỏng có thể tích xác định nhưng nhận hình dạng bình; chất khí không có hình dạng và thể tích xác định. Nóng chảy, đông đặc, bay hơi, ngưng tụ là các quá trình chuyển thể.",
  "Nóng chảy: rắn → lỏng\nĐông đặc: lỏng → rắn\nBay hơi: lỏng → khí\nNgưng tụ: khí → lỏng",
  "Khi nước sôi, quá trình nào xảy ra?",
  "Nước lỏng chuyển thành hơi nước; đây là hóa hơi.",
  "Hiện tượng nào là ngưng tụ?\nA. Nước đá tan\nB. Mồ hôi bay hơi\nC. Hơi nước gặp lạnh tạo giọt nước\nD. Nước đóng băng",
  ["Nước đá tan", "Mồ hôi bay hơi", "Hơi nước gặp lạnh tạo giọt nước", "Nước đóng băng"], 2,
  "Sấy quần áo, chưng cất nước và làm lạnh thực phẩm đều dựa trên chuyển thể.",
  "Tại sao nắp nồi có giọt nước khi nấu canh?",
  "Hơi nước gặp nắp lạnh hơn nên ngưng tụ thành giọt."
),
L(6, "hon-hop", "Hỗn hợp và chất tinh khiết", "⚗️",
  "Phân biệt chất tinh khiết và hỗn hợp; nhận biết hỗn hợp đồng nhất và không đồng nhất.",
  "Nước muối",
  "Nước muối chứa nước và muối. Khi muối tan hoàn toàn, hỗn hợp nhìn đồng nhất nhưng vẫn gồm nhiều chất.",
  "Chất tinh khiết có thành phần xác định. Hỗn hợp gồm từ hai chất trở lên. Có thể tách hỗn hợp dựa trên sự khác nhau về tính chất vật lý.",
  "Cô cạn dung dịch muối → thu muối rắn\nLọc → tách chất rắn không tan khỏi chất lỏng\nChiết → tách hai chất lỏng không trộn lẫn",
  "Muốn tách cát khỏi nước, dùng phương pháp nào?",
  "Lọc.",
  "Muốn thu lại muối từ nước biển, phương pháp phù hợp là?\nA. Lọc\nB. Cô cạn\nC. Nam châm\nD. Chiết",
  ["Lọc", "Cô cạn", "Nam châm", "Chiết"], 1,
  "Xử lý nước, sản xuất muối và phân loại vật liệu đều dùng phương pháp tách hỗn hợp.",
  "Một hỗn hợp gồm mạt sắt, cát và muối. Hãy nêu thứ tự tách.",
  "Dùng nam châm tách sắt; thêm nước hòa tan muối; lọc lấy cát; cô cạn dung dịch để thu muối."
),
L(6, "dung-dich", "Dung dịch", "🥤",
  "Hiểu dung môi, chất tan, dung dịch và nồng độ đơn giản.",
  "Pha nước chanh",
  "Khi đường tan trong nước, nước là dung môi, đường là chất tan và hỗn hợp thu được là dung dịch.",
  "Dung dịch là hỗn hợp đồng nhất của chất tan và dung môi. Độ tan cho biết lượng chất có thể tan trong một lượng dung môi ở điều kiện xác định.",
  "C% = m_chất_tan / m_dung_dịch × 100%\nS = m_chất_tan / m_nước × 100 (g chất tan/100 g nước)",
  "Hòa tan 10 g muối vào 90 g nước. Tính nồng độ phần trăm.",
  "m dung dịch = 100 g; C% = 10%.",
  "Dung dịch 5% khối lượng nghĩa là gì?\nA. 5 g chất tan trong 100 g dung dịch\nB. 5 g nước trong 100 g dung dịch\nC. 5 mol chất tan\nD. 5 g chất tan trong 1 g nước",
  ["5 g chất tan trong 100 g dung dịch", "5 g nước trong 100 g dung dịch", "5 mol chất tan", "5 g chất tan trong 1 g nước"], 0,
  "Pha nước muối sinh lý, đồ uống và hóa chất phòng thí nghiệm cần tính lượng chất tan phù hợp.",
  "Muốn pha 200 g dung dịch đường 8%, cần bao nhiêu gam đường?",
  "m đường = 200 × 8% = 16 g; nước = 184 g."
),
L(6, "bien-doi-vat-ly", "Biến đổi vật lý và hóa học", "🔄",
  "Nhận biết khi nào chỉ thay đổi trạng thái và khi nào tạo chất mới.",
  "Đốt giấy và làm tan đá",
  "Đá tan thành nước không tạo chất mới; giấy cháy tạo tro và khí mới.",
  "Biến đổi vật lý không tạo chất mới. Biến đổi hóa học tạo ra một hay nhiều chất mới. Dấu hiệu thường gặp: có khí, kết tủa, đổi màu, phát sáng hoặc tỏa/thu nhiệt.",
  "Không có công thức tính tổng quát; cần theo dõi chất trước và sau biến đổi.",
  "Đốt một mẩu giấy là biến đổi gì?",
  "Biến đổi hóa học vì tạo ra các chất mới.",
  "Hiện tượng nào là biến đổi vật lý?\nA. Sắt bị gỉ\nB. Giấy cháy\nC. Nước đá tan\nD. Thức ăn ôi thiu",
  ["Sắt bị gỉ", "Giấy cháy", "Nước đá tan", "Thức ăn ôi thiu"], 2,
  "Nhận biết biến đổi giúp sử dụng vật liệu, bảo quản thực phẩm và xử lý chất thải an toàn.",
  "Muối tan trong nước rồi cô cạn lại thu được muối. Vì sao đây không phải phản ứng hóa học?",
  "Không tạo chất mới; muối chỉ chuyển từ trạng thái rắn sang phân tán trong dung dịch rồi thu hồi lại."
),
L(6, "an-toan-hoa-hoc", "An toàn khi sử dụng hóa chất", "🛡️",
  "Hình thành thói quen an toàn khi tiếp xúc và sử dụng hóa chất.",
  "Phòng thí nghiệm an toàn",
  "Hóa chất cần được nhận diện bằng nhãn, ký hiệu nguy hiểm và hướng dẫn sử dụng.",
  "Không nếm hóa chất; không ngửi trực tiếp; dùng kính bảo hộ khi cần; đọc nhãn; báo ngay khi có sự cố. Khi pha loãng acid, luôn thêm acid vào nước từ từ, không làm ngược lại.",
  "Nguyên tắc ghi nhớ: Đọc nhãn → bảo hộ → thao tác đúng → xử lý chất thải đúng.",
  "Nếu hóa chất bắn vào mắt, việc đầu tiên nên làm là gì?",
  "Rửa mắt ngay bằng nhiều nước sạch và báo người phụ trách/y tế.",
  "Hành động nào an toàn nhất?\nA. Nếm thử để nhận biết\nB. Ngửi sát miệng chai\nC. Đọc nhãn và dùng bảo hộ phù hợp\nD. Trộn hai hóa chất bất kỳ",
  ["Nếm thử để nhận biết", "Ngửi sát miệng chai", "Đọc nhãn và dùng bảo hộ phù hợp", "Trộn hai hóa chất bất kỳ"], 2,
  "Kỹ năng an toàn là nền tảng cho mọi thí nghiệm và ứng dụng hóa chất trong đời sống.",
  "Tại sao không được tự ý trộn chất tẩy rửa gia dụng?",
  "Có thể tạo khí hoặc sản phẩm nguy hiểm do xảy ra phản ứng hóa học không kiểm soát."
),

# =========================
# GRADE 7
# =========================
L(7, "nguyen-tu", "Nguyên tử", "⚛️",
  "Làm quen với cấu tạo nguyên tử và các hạt cơ bản.",
  "Mô hình nguyên tử",
  "Nguyên tử rất nhỏ nhưng cấu tạo từ các hạt mang điện và không mang điện.",
  "Nguyên tử gồm hạt nhân và lớp electron. Hạt nhân chứa proton mang điện dương và neutron không mang điện. Electron mang điện âm chuyển động tạo thành vỏ nguyên tử.",
  "Nguyên tử trung hòa: số proton = số electron\nĐiện tích hạt nhân = +Z",
  "Một nguyên tử có 8 proton. Có bao nhiêu electron nếu nguyên tử trung hòa?",
  "8 electron.",
  "Hạt nào mang điện âm?\nA. Proton\nB. Neutron\nC. Electron\nD. Hạt nhân",
  ["Proton", "Neutron", "Electron", "Hạt nhân"], 2,
  "Mô hình nguyên tử là nền tảng để hiểu nguyên tố, liên kết và phản ứng hóa học.",
  "Một nguyên tử có 11 proton và 12 neutron. Số electron của nguyên tử trung hòa là bao nhiêu?",
  "11 electron."
),
L(7, "nguyen-to-hoa-hoc", "Nguyên tố hóa học", "🔬",
  "Hiểu khái niệm nguyên tố và ký hiệu hóa học.",
  "Ký hiệu hóa học",
  "Fe, O, H, C... là những ký hiệu ngắn gọn giúp biểu diễn nguyên tố.",
  "Nguyên tố hóa học là tập hợp các nguyên tử có cùng số proton. Ký hiệu hóa học thường gồm một hoặc hai chữ cái, chữ đầu viết hoa.",
  "Số hiệu nguyên tử Z = số proton = số electron (đối với nguyên tử trung hòa)",
  "Nguyên tố có Z = 8 là nguyên tố nào?",
  "Oxygen (O).",
  "Ký hiệu nào là của sodium?\nA. S\nB. Na\nC. N\nD. So",
  ["S", "Na", "N", "So"], 1,
  "Ký hiệu nguyên tố được dùng để đọc thành phần phân bón, thuốc, thực phẩm và vật liệu.",
  "Vì sao Na không phải ký hiệu N?",
  "N là nitrogen; Na là sodium, lấy từ tên Latin natrium."
),
L(7, "phan-tu", "Phân tử", "🧩",
  "Hiểu phân tử và cách biểu diễn chất bằng công thức hóa học.",
  "Từ nguyên tử đến phân tử",
  "Một phân tử có thể gồm một hay nhiều nguyên tử liên kết với nhau.",
  "Phân tử là hạt đại diện cho chất, gồm các nguyên tử liên kết. Công thức hóa học cho biết loại nguyên tố và số nguyên tử tương ứng.",
  "H2O: 2 H và 1 O\nCO2: 1 C và 2 O\nO2: 2 O",
  "Trong 3CO2 có tổng cộng bao nhiêu nguyên tử?",
  "3 phân tử CO2 chứa 3 C và 6 O, tổng 9 nguyên tử.",
  "Hệ số 2 trong 2H2O cho biết gì?\nA. 2 nguyên tử H\nB. 2 phân tử H2O\nC. 2 nguyên tử O\nD. 4 phân tử",
  ["2 nguyên tử H", "2 phân tử H2O", "2 nguyên tử O", "4 phân tử"], 1,
  "Công thức hóa học giúp ghi nhãn, tính toán thành phần và mô tả phản ứng.",
  "Trong Ca(OH)2 có bao nhiêu nguyên tử O?",
  "Có 2 nguyên tử O."
),
L(7, "don-chat-hop-chat", "Đơn chất và hợp chất", "🧱",
  "Phân biệt chất tạo bởi một nguyên tố và chất tạo bởi nhiều nguyên tố.",
  "O2 và H2O",
  "O2 chỉ chứa oxygen; H2O chứa hydrogen và oxygen.",
  "Đơn chất tạo bởi một nguyên tố. Hợp chất tạo bởi từ hai nguyên tố trở lên. Hợp chất có tính chất khác với các nguyên tố tạo nên nó.",
  "Đơn chất: O2, Fe, Cu\nHợp chất: H2O, CO2, NaCl",
  "NaCl là đơn chất hay hợp chất?",
  "Hợp chất vì có Na và Cl.",
  "Chất nào là đơn chất?\nA. H2O\nB. CO2\nC. O2\nD. NaCl",
  ["H2O", "CO2", "O2", "NaCl"], 2,
  "Phân biệt đơn chất và hợp chất giúp đọc thành phần vật liệu và hóa chất.",
  "Tại sao nước có tính chất khác hydrogen và oxygen?",
  "Khi tạo hợp chất, các nguyên tố liên kết thành chất mới có cấu trúc và tính chất mới."
),
L(7, "phan-ung-hoa-hoc", "Dấu hiệu phản ứng hóa học", "💥",
  "Nhận biết chất tham gia, sản phẩm và dấu hiệu phản ứng.",
  "Giấm và baking soda",
  "Khi giấm tác dụng với baking soda, khí CO2 thoát ra tạo bọt.",
  "Phản ứng hóa học là quá trình biến đổi chất này thành chất khác. Chất ban đầu là chất tham gia; chất tạo thành là sản phẩm.",
  "Sơ đồ tổng quát: chất tham gia → sản phẩm\nKhối lượng được bảo toàn trong hệ kín.",
  "Cho giấm vào baking soda thấy sủi bọt. Dấu hiệu nào cho thấy có phản ứng?",
  "Có khí mới sinh ra.",
  "Trong phản ứng hóa học, chất mới được tạo thành gọi là gì?\nA. Dung môi\nB. Sản phẩm\nC. Chất chỉ thị\nD. Hỗn hợp",
  ["Dung môi", "Sản phẩm", "Chất chỉ thị", "Hỗn hợp"], 1,
  "Phản ứng hóa học được dùng để nấu ăn, xử lý nước, sản xuất vật liệu và năng lượng.",
  "Tại sao sủi bọt chưa đủ để kết luận mọi trường hợp đều là phản ứng hóa học?",
  "Có thể có khí thoát ra do biến đổi vật lý; cần xét chất mới và nguyên nhân tạo khí."
),
L(
    7,
    "bao-toan-khoi-luong",
    "Định luật bảo toàn khối lượng",
    "⚖️",

    "Hiểu tổng khối lượng được bảo toàn trong phản ứng hóa học.",

    "Cân trước và sau phản ứng",

    "Trong hệ kín, khối lượng tổng trước phản ứng bằng khối lượng tổng sau phản ứng.",

    "Định luật bảo toàn khối lượng: tổng khối lượng các chất tham gia bằng tổng khối lượng các sản phẩm.",

    "m_chất tham gia = m_sản phẩm",

    "Phản ứng tạo 12 g sản phẩm từ một chất có khối lượng 5 g. Chất còn lại có khối lượng bao nhiêu?",

    "12 - 5 = 7 g.",

    "Trong hệ kín, 10 g A phản ứng vừa đủ với 6 g B. Khối lượng sản phẩm là?\nA. 4 g\nB. 6 g\nC. 10 g\nD. 16 g",

    ["4 g", "6 g", "10 g", "16 g"],

    3,

    "Định luật giúp kiểm tra số liệu thí nghiệm và tính lượng chất trong sản xuất.",

    "Nếu phản ứng diễn ra trong cốc mở và có khí bay ra, cân lại thấy khối lượng giảm. Có vi phạm định luật không?",

    "Không. Hệ không kín nên một phần sản phẩm khí thoát ra khỏi hệ."
),

# =========================
# GRADE 8
# =========================
L(8, "cong-thuc-hoa-hoc", "Công thức hóa học", "🧾",
  "Đọc, viết công thức và tính thành phần nguyên tố.",
  "Từ tên chất đến công thức",
  "Công thức hóa học là ngôn ngữ cô đọng để biểu diễn thành phần chất.",
  "Chỉ số cho biết số nguyên tử của mỗi nguyên tố trong một đơn vị công thức. Hệ số cho biết số đơn vị công thức/phân tử.",
  "Khối lượng mol: M = Σ n_i A_i\n% nguyên tố = (n_i A_i / M) × 100%",
  "Tính phần trăm khối lượng oxygen trong H2O. Cho H=1, O=16.",
  "M(H2O)=18; %O = 16/18×100% ≈ 88,89%.",
  "Trong CO2, oxygen chiếm khoảng bao nhiêu % khối lượng? C=12, O=16.",
  ["27,27%", "72,73%", "50%", "88,89%"], 1,
  "Tính thành phần giúp kiểm tra phân bón, nhiên liệu, thuốc và nguyên liệu.",
  "Tính % carbon trong CO2.",
  "M=44; %C=12/44×100%≈27,27%."
),
L(
    8,
    "phuong-trinh-hoa-hoc",
    "Phương trình hóa học",
    "⚗️",

    "Biểu diễn phản ứng hóa học bằng công thức và hệ số.",

    "Cân bằng phương trình hóa học",

    "Phương trình hóa học biểu diễn chất tham gia, sản phẩm và tỉ lệ giữa các chất trong phản ứng.",

    "Khi lập phương trình hóa học cần viết đúng công thức hóa học và cân bằng số nguyên tử của mỗi nguyên tố ở hai vế.",

    "Ví dụ: 2H₂ + O₂ → 2H₂O",

    "Cân bằng phương trình: H₂ + O₂ → H₂O.",

    "2H₂ + O₂ → 2H₂O.",

    "Phương trình nào đã được cân bằng?\nA. H₂ + O₂ → H₂O\nB. 2H₂ + O₂ → 2H₂O\nC. H₂ + 2O₂ → H₂O\nD. 2H₂ + 2O₂ → H₂O",

    [
        "H₂ + O₂ → H₂O",
        "2H₂ + O₂ → 2H₂O",
        "H₂ + 2O₂ → H₂O",
        "2H₂ + 2O₂ → H₂O"
    ],

    1,

    "Phương trình là cơ sở để tính lượng chất trong phản ứng và thiết kế quy trình sản xuất.",

    "Vì sao không được tự ý thay đổi chỉ số trong công thức hóa học khi cân bằng phương trình?",

    "Vì thay đổi chỉ số sẽ làm thay đổi chất; khi cân bằng chỉ được thay đổi hệ số trước công thức."
),
L(8, "mol-va-khoi-luong-mol", "Mol và khối lượng mol", "🧪",
  "Tính số mol, khối lượng và số hạt.",
  "Đếm những hạt cực nhỏ",
  "Mol là đơn vị lượng chất, giúp chuyển đổi giữa khối lượng và số hạt.",
  "Mol là đơn vị đo lượng chất. Một mol chứa khoảng 6,022×10^23 hạt. Khối lượng mol cho biết khối lượng của một mol chất.",
  "n = m/M\nN = n·N_A\nN_A ≈ 6,022×10^23 mol^-1",
  "Có 0,5 mol H2O. Tính khối lượng, biết M(H2O)=18 g/mol.",
  "m = 0,5×18 = 9 g.",
  "2 mol CO2 có bao nhiêu phân tử?",
  ["6,022×10^23", "1,2044×10^24", "2×10^23", "3,011×10^23"], 1,
  "Tính mol là nền tảng của mọi bài toán định lượng hóa học.",
  "36 g H2O tương ứng bao nhiêu mol?",
  "n=36/18=2 mol."
),
L(8, "dung-dich-nong-do", "Nồng độ dung dịch", "🥛",
  "Tính nồng độ phần trăm và nồng độ mol.",
  "Pha dung dịch đúng nồng độ",
  "Nồng độ cho biết mức độ đậm đặc của chất tan trong dung dịch.",
  "Nồng độ dung dịch cho biết lượng chất tan có trong một lượng dung dịch xác định.",
  "C% = m_ct/m_dd×100%\nC_M = n/V (mol/L)",
  "Hòa tan 0,5 mol NaCl vào 2 L dung dịch. Tính CM.",
  "CM = 0,5/2 = 0,25 M.",
  "1 mol chất tan trong 2 L dung dịch có CM bằng?\nA. 0,2 M\nB. 0,5 M\nC. 1 M\nD. 2 M",
  ["0,2 M", "0,5 M", "1 M", "2 M"], 1,
  "Pha thuốc, phân bón và dung dịch thí nghiệm cần kiểm soát nồng độ.",
  "Muốn pha 500 mL dung dịch NaCl 0,2 M cần bao nhiêu mol NaCl?",
  "n = C·V = 0,2×0,5 = 0,1 mol."
),
L(8, "axit-bazo-muoi", "Acid, base và muối", "⚗️",
  "Nhận biết acid, base, muối và phản ứng trung hòa.",
  "pH quanh ta",
  "Chanh chứa acid; nước xà phòng có tính base; muối ăn là NaCl.",
  "Acid thường tạo H+ trong nước; base tạo OH− theo cách mô tả phổ thông. Phản ứng acid + base thường tạo muối và nước.",
  "pH = −log[H+]\nHCl + NaOH → NaCl + H2O",
  "Dung dịch HCl có [H+] = 10^-3 M. Tính pH.",
  "pH = 3.",
  "Sản phẩm của phản ứng trung hòa HCl + NaOH là?\nA. NaCl và H2O\nB. H2 và Cl2\nC. Na và H2O\nD. NaOH và HCl",
  ["NaCl và H2O", "H2 và Cl2", "Na và H2O", "NaOH và HCl"], 0,
  "Trung hòa được dùng xử lý nước thải, điều chỉnh đất và sản xuất nhiều sản phẩm.",
  "Tại sao thuốc kháng acid có thể làm giảm cảm giác ợ nóng?",
  "Chất có tính base/antacid trung hòa một phần acid dạ dày."
),
L(8, "oxi-hoa-khu", "Oxi hóa và sự cháy", "🔥",
  "Hiểu sự cháy, oxi hóa và điều kiện để phản ứng cháy xảy ra.",
  "Ngọn lửa cần gì?",
  "Cháy cần chất cháy, oxygen và nhiệt độ thích hợp.",
  "Oxi hóa là quá trình chất tác dụng với oxygen hoặc mất electron theo ngữ cảnh. Phản ứng cháy thường tỏa nhiều nhiệt và phát sáng.",
  "Hydro cháy: 2H2 + O2 → 2H2O\nCarbon cháy: C + O2 → CO2",
  "Đốt 2 mol H2 vừa đủ cần bao nhiêu mol O2?",
  "Theo PTHH: 2 mol H2 cần 1 mol O2.",
  "Yếu tố nào không thuộc 'tam giác cháy'?\nA. Chất cháy\nB. Oxygen\nC. Nhiệt\nD. Muối ăn",
  ["Chất cháy", "Oxygen", "Nhiệt", "Muối ăn"], 3,
  "Đốt nhiên liệu tạo năng lượng; hiểu tam giác cháy giúp phòng cháy chữa cháy.",
  "Tại sao phủ kín ngọn nến có thể làm nến tắt?",
  "Lượng oxygen cung cấp cho vùng cháy giảm."
),

# =========================
# GRADE 9
# =========================
L(9, "kim-loai", "Kim loại và tính chất", "🔩",
  "Khám phá tính chất vật lý, hóa học của kim loại.",
  "Vì sao kim loại được dùng làm dây điện?",
  "Kim loại có tính dẫn điện, dẫn nhiệt, ánh kim và thường có tính dẻo.",
  "Kim loại có thể phản ứng với oxygen, acid hoặc muối tùy kim loại. Dãy hoạt động hóa học giúp dự đoán một số phản ứng thế.",
  "Zn + 2HCl → ZnCl2 + H2\n2Mg + O2 → 2MgO",
  "Cho Zn tác dụng HCl dư, khí nào sinh ra?",
  "Hydrogen H2.",
  "Kim loại nào phản ứng với HCl tạo H2?\nA. Cu\nB. Ag\nC. Zn\nD. Au",
  ["Cu", "Ag", "Zn", "Au"], 2,
  "Kim loại được dùng trong xây dựng, điện, giao thông và chế tạo máy.",
  "Vì sao đồng được dùng làm dây điện nhưng sắt thường không được dùng cho dây dẫn trong nhà?",
  "Đồng dẫn điện tốt và ít bị ăn mòn hơn trong điều kiện thông thường."
),
L(9, "day-hoat-dong-kim-loai", "Dãy hoạt động hóa học của kim loại", "📋",
  "Dùng dãy hoạt động để dự đoán phản ứng thế.",
  "Kim loại nào đẩy được kim loại nào?",
  "Kim loại hoạt động mạnh hơn có thể đẩy kim loại yếu hơn ra khỏi dung dịch muối trong điều kiện thích hợp.",
  "Kim loại hoạt động mạnh hơn có thể đẩy kim loại yếu hơn ra khỏi hợp chất của nó trong một số phản ứng thế.",
  "Zn + CuSO4 → ZnSO4 + Cu\nZn + 2HCl → ZnCl2 + H2",
  "Nhúng Zn vào CuSO4. Hiện tượng và sản phẩm?",
  "Zn tan dần, Cu bám ra; tạo ZnSO4 và Cu.",
  "Phản ứng nào xảy ra?\nA. Cu + ZnSO4\nB. Zn + CuSO4\nC. Ag + MgSO4\nD. Au + HCl",
  ["Cu + ZnSO4", "Zn + CuSO4", "Ag + MgSO4", "Au + HCl"], 1,
  "Mạ kim loại, luyện kim và xử lý bề mặt dựa trên tính chất phản ứng của kim loại.",
  "Vì sao không nên dùng vật chứa bằng kim loại hoạt động mạnh cho một số dung dịch muối?",
  "Kim loại có thể phản ứng với ion kim loại trong dung dịch, làm hỏng vật chứa hoặc tạo tạp chất."
),
L(9, "phi-kim", "Phi kim và hợp chất của phi kim", "🌫️",
  "Tìm hiểu oxygen, carbon, sulfur, chlorine và một số hợp chất.",
  "Không khí và vật liệu",
  "Phi kim có nhiều tính chất khác kim loại; nhiều phi kim tồn tại dạng khí ở điều kiện thường.",
  "C + O2 → CO2\nS + O2 → SO2\nCl2 + 2Na → 2NaCl",
  "CO2, SO2 và các oxide của phi kim có nhiều ứng dụng và ảnh hưởng đến môi trường.\nC + O2 → CO2\nS + O2 → SO2",
  "Carbon cháy hoàn toàn tạo chất gì?",
  "CO2.",
  "Khí nào cần cho sự cháy?\nA. N2\nB. O2\nC. CO2\nD. He",
  ["N2", "O2", "CO2", "He"], 1,
  "Phi kim và hợp chất của chúng dùng trong xử lý nước, vật liệu, phân bón và công nghiệp.",
  "Tại sao CO2 thường dùng trong một số bình chữa cháy?",
  "CO2 không duy trì sự cháy và có thể cách ly oxygen quanh vùng cháy."
),
L(9, "acid-bazo-muoi", "Acid, base và muối trong đời sống", "🧴",
  "Mở rộng phản ứng của acid, base và muối.",
  "Từ giấm đến chất tẩy rửa",
  "Acid và base xuất hiện trong thực phẩm, vệ sinh và xử lý môi trường.",
  "Acid + kim loại → muối + H2 (với kim loại thích hợp)\nAcid + base → muối + H2O\nAcid + carbonate → muối + CO2 + H2O",
  "HCl + CaCO3 → CaCl2 + CO2 + H2O\nHCl + NaOH → NaCl + H2O",
  "HCl + CaCO3 → CaCl2 + CO2 + H2O. Nếu 0,1 mol CaCO3 phản ứng hết thì n(CO2) bằng bao nhiêu?",
  "0,1 mol CO2.",
  "Chất nào phản ứng với acid tạo CO2?\nA. NaCl\nB. CaCO3\nC. Cu\nD. H2O",
  ["NaCl", "CaCO3", "Cu", "H2O"], 1,
  "Khử cặn, xử lý đất, sản xuất vật liệu và vệ sinh đều có ứng dụng acid-base.",
  "Vì sao không nên đổ acid mạnh lên đá vôi trong không gian kín?",
  "Phản ứng có thể sinh CO2 nhanh, gây áp suất/nguy cơ ngạt và bắn hóa chất."
),
L(9, "hydrocarbon", "Hydrocarbon", "⛽",
  "Làm quen methane, ethylene và các hydrocarbon phổ biến.",
  "Nhiên liệu hóa thạch",
  "Hydrocarbon chỉ gồm carbon và hydrogen; nhiều chất là nhiên liệu.",
  "Methane: CH4\nEthylene: C2H4\nCháy methane: CH4 + 2O2 → CO2 + 2H2O",
  "CH4 + 2O2 → CO2 + 2H2O\nC2H4 + 3O2 → 2CO2 + 2H2O",
  "Đốt 1 mol CH4 hoàn toàn cần bao nhiêu mol O2?",
  "2 mol O2.",
  "Công thức của methane là?\nA. CH4\nB. C2H6\nC. CO2\nD. CH3OH",
  ["CH4", "C2H6", "CO2", "CH3OH"], 0,
  "Hydrocarbon dùng làm nhiên liệu và nguyên liệu cho công nghiệp hóa dầu.",
  "Vì sao đốt nhiên liệu hóa thạch cần thông gió tốt?",
  "Thiếu oxygen có thể tạo CO độc; đồng thời CO2 tích tụ gây nguy cơ ngạt."
),
L(9, "polime-vat-lieu", "Polymer và vật liệu polymer", "🧵",
  "Hiểu khái niệm polymer, monomer và một số ứng dụng.",
  "Nhựa quanh ta",
  "Nhiều loại nhựa, cao su và sợi là polymer có phân tử rất lớn.",
  "Polymer được tạo từ các đơn vị lặp lại gọi là mắt xích; monomer là phân tử nhỏ dùng để tạo polymer.\nVí dụ: ethylene → polyethylene (PE).",
  "Ethylene → polyethylene (PE)\nMonomer → polymer thông qua quá trình trùng hợp.",
  "n mắt xích có thể tạo phân tử polymer có khối lượng xấp xỉ n lần khối lượng mắt xích trong mô hình đơn giản.",
  "PE được dùng làm túi, màng và chai nhựa vì tính bền và nhẹ.",
  "PE thuộc nhóm nào?\nA. Polymer\nB. Muối\nC. Kim loại\nD. Acid",
  ["Polymer", "Muối", "Kim loại", "Acid"], 0,
  "Polymer có mặt trong bao bì, sợi, cao su, thiết bị y tế và vật liệu xây dựng.",
  "Vì sao cần giảm đồ nhựa dùng một lần?",
  "Nhiều polymer khó phân hủy tự nhiên và có thể tạo rác lâu dài."
),

# =========================
# GRADE 10
# =========================
L(10, "cau-tao-nguyen-tu", "Cấu tạo nguyên tử và đồng vị", "⚛️",
  "Hệ thống hóa proton, neutron, electron, số hiệu nguyên tử và đồng vị.",
  "Nguyên tử không phải hạt đặc",
  "Nguyên tử có hạt nhân rất nhỏ chứa proton, neutron và lớp electron.",
  "Z = số proton\nA = Z + N\nĐồng vị: cùng Z, khác N.",
  "Nguyên tử 23Na có Z=11, N=12.",
  "Nguyên tử 35Cl có Z=17. Số neutron là bao nhiêu?",
  "N = 35 - 17 = 18.",
  "Hai đồng vị của cùng nguyên tố có đặc điểm nào giống nhau?\nA. Số neutron\nB. Số proton\nC. Số khối\nD. Khối lượng",
  ["Số neutron", "Số proton", "Số khối", "Khối lượng"], 1,
  "Đồng vị được ứng dụng trong y học hạt nhân, khảo cổ và nghiên cứu vật chất.",
  "Một đồng vị có A=40, Z=20. Hãy xác định p, e, n của nguyên tử trung hòa.",
  "p=20, e=20, n=20."
),
L(10, "cau-hinh-electron", "Cấu hình electron", "🔵",
  "Hiểu sự phân bố electron và electron hóa trị.",
  "Electron quyết định tính chất hóa học",
  "Các electron phân bố theo lớp và phân lớp năng lượng; electron lớp ngoài cùng có vai trò lớn trong liên kết.",
  "Sức chứa lớp theo mô hình đơn giản: 2n² electron tối đa ở lớp n.\nPhân lớp: s, p, d, f.",
  "Na (Z=11): 1s² 2s² 2p⁶ 3s¹.",
  "Nguyên tử O (Z=8) có bao nhiêu electron lớp ngoài cùng?",
  "6 electron.",
  "Cấu hình 1s²2s²2p⁶3s¹ là của nguyên tố nào?\nA. Na\nB. Mg\nC. Ne\nD. K",
  ["Na", "Mg", "Ne", "K"], 0,
  "Cấu hình electron giúp dự đoán xu hướng tạo ion và liên kết.",
  "Vì sao các nguyên tố cùng nhóm thường có tính chất hóa học gần giống nhau?",
  "Chúng thường có số electron hóa trị tương tự."
),
L(10, "bang-tuan-hoan", "Bảng tuần hoàn", "🧭",
  "Đọc chu kỳ, nhóm và xu hướng tính chất trong bảng tuần hoàn.",
  "Bản đồ các nguyên tố",
  "Bảng tuần hoàn sắp xếp nguyên tố theo số hiệu nguyên tử và cấu hình electron.",
  "Chu kỳ liên quan số lớp electron; nhóm chính liên quan số electron hóa trị.\nBán kính nguyên tử thường giảm từ trái sang phải, tăng từ trên xuống dưới.",
  "Na thuộc nhóm 1, chu kỳ 3.",
  "Nguyên tố Z=17 nằm ở đâu?",
  "Cl, chu kỳ 3, nhóm 17.",
  "Nguyên tố nào cùng nhóm với Cl?\nA. Na\nB. F\nC. Mg\nD. Ne",
  ["Na", "F", "Mg", "Ne"], 1,
  "Bảng tuần hoàn giúp dự đoán tính chất và lựa chọn nguyên tố trong vật liệu, dược phẩm.",
  "Trong chu kỳ 3, nguyên tố nào có bán kính lớn hơn: Na hay Cl?",
  "Na, vì bán kính giảm dần từ trái sang phải trong cùng chu kỳ."
),
L(10, "lien-ket-hoa-hoc", "Liên kết hóa học", "🔗",
  "Phân biệt liên kết ion, cộng hóa trị và kim loại.",
  "Vì sao nguyên tử liên kết?",
  "Nguyên tử liên kết để đạt trạng thái năng lượng bền hơn; electron có thể được nhường, nhận hoặc dùng chung.",
  "Ion: lực hút giữa ion trái dấu.\nCộng hóa trị: dùng chung cặp electron.\nKim loại: mạng ion dương và electron delocalized theo mô hình.",
  "NaCl: liên kết ion\nH2: cộng hóa trị không cực\nHCl: cộng hóa trị phân cực",
  "NaCl thuộc loại liên kết chính nào?",
  "Liên kết ion.",
  "Liên kết trong H2 chủ yếu là?\nA. Ion\nB. Cộng hóa trị không cực\nC. Kim loại\nD. Hydrogen",
  ["Ion", "Cộng hóa trị không cực", "Kim loại", "Hydrogen"], 1,
  "Hiểu liên kết giúp giải thích độ tan, nhiệt độ nóng chảy và tính dẫn điện của chất.",
  "Tại sao NaCl rắn không dẫn điện tốt nhưng NaCl nóng chảy dẫn điện?",
  "Ion trong chất rắn bị giữ trong mạng; khi nóng chảy, ion chuyển động tự do hơn."
),
L(10, "phan-ung-oxy-hoa-khu", "Phản ứng oxi hóa - khử", "⚡",
  "Nhận biết sự oxi hóa, khử và số oxi hóa.",
  "Electron chuyển đi đâu?",
  "Trong phản ứng oxi hóa-khử có sự thay đổi số oxi hóa và thường gắn với trao đổi electron.",
  "Oxi hóa: tăng số oxi hóa/mất e.\nKhử: giảm số oxi hóa/nhận e.\nChất oxi hóa bị khử; chất khử bị oxi hóa.",
  "Zn → Zn²⁺ + 2e\nCu²⁺ + 2e → Cu",
  "Trong Zn + Cu²⁺ → Zn²⁺ + Cu, Zn bị oxi hóa hay khử?",
  "Zn bị oxi hóa.",
  "Chất nhận electron là chất gì?\nA. Chất khử\nB. Chất oxi hóa\nC. Dung môi\nD. Muối",
  ["Chất khử", "Chất oxi hóa", "Dung môi", "Muối"], 1,
  "Phản ứng redox là cơ sở của pin điện hóa, luyện kim và nhiều quá trình sinh học.",
  "Trong phản ứng trên, chất oxi hóa là gì?",
  "Cu²⁺ vì nó nhận electron và bị khử thành Cu."
),
L(10, "nang-luong-hoa-hoc", "Năng lượng trong phản ứng", "🔥",
  "Hiểu phản ứng tỏa nhiệt, thu nhiệt và biến thiên enthalpy cơ bản.",
  "Phản ứng nóng hay lạnh?",
  "Phản ứng hóa học có thể giải phóng hoặc hấp thụ năng lượng.",
  "Phản ứng tỏa nhiệt: ΔH < 0\nPhản ứng thu nhiệt: ΔH > 0\nTheo quy ước: ΔH = H_sản phẩm − H_chất tham gia.",
  "Nếu ΔH = −100 kJ/mol, phản ứng tỏa 100 kJ cho mỗi mol phản ứng theo phương trình.",
  "Một phản ứng có ΔH = +50 kJ/mol là tỏa hay thu nhiệt?",
  "Thu nhiệt.",
  "Dấu của ΔH với phản ứng tỏa nhiệt là?\nA. Dương\nB. Âm\nC. Bằng 1\nD. Không xác định",
  ["Dương", "Âm", "Bằng 1", "Không xác định"], 1,
  "Hiểu năng lượng giúp thiết kế nhiên liệu, vật liệu cách nhiệt và quy trình công nghiệp.",
  "Tại sao túi chườm nóng có thể nóng lên do phản ứng?",
  "Một số phản ứng tỏa nhiệt giải phóng năng lượng dưới dạng nhiệt."
),

# =========================
# GRADE 11
# =========================
L(11, "toc-do-phan-ung", "Tốc độ phản ứng", "⏱️",
  "Hiểu tốc độ phản ứng và các yếu tố ảnh hưởng.",
  "Vì sao bột phản ứng nhanh hơn cục?",
  "Diện tích bề mặt, nhiệt độ, nồng độ và chất xúc tác có thể làm thay đổi tốc độ phản ứng.",
  "Tốc độ trung bình có thể biểu diễn: v = ΔC/Δt (theo độ lớn thay đổi nồng độ).\nTăng nhiệt độ thường làm tăng tốc độ phản ứng.",
  "CaCO3 dạng bột phản ứng với acid nhanh hơn cùng khối lượng dạng cục.",
  "Yếu tố nào làm tăng tốc độ phản ứng giữa CaCO3 và HCl?\nA. Giảm nhiệt độ\nB. Nghiền nhỏ CaCO3\nC. Giảm nồng độ acid\nD. Làm lạnh",
  "Nghiền nhỏ làm tăng diện tích tiếp xúc.",
  "Chất xúc tác làm gì?\nA. Bị tiêu hao hoàn toàn\nB. Thay đổi tốc độ phản ứng mà không bị tiêu hao theo cách lý tưởng\nC. Luôn làm phản ứng dừng\nD. Tạo thêm chất ban đầu",
  ["Bị tiêu hao hoàn toàn", "Thay đổi tốc độ phản ứng mà không bị tiêu hao theo cách lý tưởng", "Luôn làm phản ứng dừng", "Tạo thêm chất ban đầu"], 1,
  "Xúc tác được dùng trong sản xuất phân bón, nhiên liệu, polymer và xử lý khí thải.",
  "Tại sao bảo quản thực phẩm trong tủ lạnh giúp chậm hỏng?",
  "Nhiệt độ thấp làm chậm nhiều phản ứng hóa học và hoạt động vi sinh."
),
L(11, "can-bang-hoa-hoc", "Cân bằng hóa học", "⚖️",
  "Hiểu phản ứng thuận nghịch và trạng thái cân bằng.",
  "Cân bằng động",
  "Ở cân bằng, phản ứng thuận và nghịch vẫn diễn ra nhưng tốc độ bằng nhau.",
  "aA + bB ⇌ cC + dD\nTại cân bằng: v_thuận = v_nghịch.",
  "N2 + 3H2 ⇌ 2NH3 là một phản ứng thuận nghịch.",
  "Tăng nồng độ H2 trong hệ Haber có xu hướng làm cân bằng chuyển về phía nào?",
  "Về phía tạo NH3 để chống lại thay đổi.",
  "Khi hệ đạt cân bằng, nồng độ các chất có nhất thiết bằng nhau không?\nA. Có\nB. Không",
  ["Có", "Không"], 1,
  "Cân bằng hóa học rất quan trọng trong sản xuất ammonia, sulfuric acid và nhiều hóa chất.",
  "Nếu lấy bớt NH3 khỏi hệ cân bằng Haber, hệ có xu hướng thế nào?",
  "Cân bằng chuyển về phải, tạo thêm NH3."
),
L(11, "su-dien-li", "Sự điện li", "💧",
  "Hiểu chất điện li, ion và dung dịch dẫn điện.",
  "Vì sao dung dịch muối dẫn điện?",
  "Khi tan trong nước, nhiều acid, base và muối phân li thành ion có thể chuyển động.",
  "NaCl → Na+ + Cl−\nHCl → H+ + Cl− (mô hình đơn giản)\nNaOH → Na+ + OH−",
  "NaCl → Na+ + Cl−\nHCl → H+ + Cl−\nNaOH → Na+ + OH−",
  "Dung dịch nào có nhiều ion hơn về mặt mô hình: NaCl hay đường glucose ở cùng nồng độ mol?",
  "NaCl tạo ion; glucose không điện li đáng kể.",
  "Chất nào là chất điện li mạnh?\nA. NaCl\nB. C6H12O6\nC. C2H5OH\nD. N2",
  ["NaCl", "C6H12O6", "C2H5OH", "N2"], 0,
  "Điện li là nền tảng của pin, điện phân, xử lý nước và hóa sinh.",
  "Vì sao nước cất dẫn điện kém hơn nước muối?",
  "Nước muối chứa nhiều ion chuyển động tự do hơn."
),
L(11, "nitrogen-ammonia", "Nitrogen và ammonia", "🌱",
  "Tìm hiểu nitrogen, ammonia và vai trò của chúng.",
  "Từ không khí đến phân bón",
  "Nitrogen chiếm phần lớn khí quyển; ammonia là nguyên liệu quan trọng cho phân đạm.",
  "N2 + 3H2 ⇌ 2NH3\nNH3 + H2O ⇌ NH4+ + OH−",
  "Từ 1 mol N2 theo PTHH có thể tạo tối đa 2 mol NH3 nếu H2 đủ.",
  "2 mol N2 phản ứng hoàn toàn theo tỉ lệ phương trình thì tạo tối đa bao nhiêu mol NH3?",
  "4 mol NH3.",
  "Ammonia được dùng nhiều để sản xuất?\nA. Phân đạm\nB. Thủy tinh\nC. Sắt nguyên chất\nD. Muối ăn",
  ["Phân đạm", "Thủy tinh", "Sắt nguyên chất", "Muối ăn"], 0,
  "Ammonia và muối ammonium đóng vai trò lớn trong nông nghiệp.",
  "Vì sao cần sử dụng phân đạm đúng liều?",
  "Dư thừa nitrogen có thể gây ô nhiễm nước, phú dưỡng và ảnh hưởng hệ sinh thái."
),
L(11, "sulfuric-acid", "Sulfur và sulfuric acid", "🧴",
  "Khám phá sulfur, SO2 và H2SO4.",
  "Acid công nghiệp quan trọng",
  "Sulfuric acid là một trong những hóa chất công nghiệp quan trọng nhất.",
  "S + O2 → SO2\n2SO2 + O2 ⇌ 2SO3\nSO3 + H2O → H2SO4",
  "H2SO4 đặc có tính háo nước mạnh và có thể gây bỏng hóa học.",
  "Trong quá trình tạo SO3 từ SO2, oxygen đóng vai trò gì?",
  "Là chất oxi hóa trong phản ứng.",
  "H2SO4 thuộc nhóm nào?\nA. Acid mạnh\nB. Base mạnh\nC. Muối\nD. Oxide",
  ["Acid mạnh", "Base mạnh", "Muối", "Oxide"], 0,
  "H2SO4 dùng trong phân bón, ắc quy, xử lý dầu mỏ và nhiều quy trình công nghiệp.",
  "Tại sao phải cực kỳ cẩn thận khi pha loãng H2SO4 đặc?",
  "Quá trình tỏa nhiều nhiệt; nếu thao tác sai có thể làm sôi bắn dung dịch."
),
L(11, "hydrocarbon-huu-co", "Đại cương hóa hữu cơ và hydrocarbon", "🧬",
  "Nắm khái niệm carbon, đồng đẳng, đồng phân và hydrocarbon.",
  "Thế giới phân tử carbon",
  "Carbon có khả năng tạo chuỗi và vòng, tạo nên số lượng hợp chất hữu cơ rất lớn.",
  "Alkane: CnH2n+2\nAlkene: CnH2n\nAlkyne: CnH2n−2 (mạch hở, đơn chức theo mô hình cơ bản)",
  "Ethene C2H4 có một liên kết đôi; ethane C2H6 chỉ có liên kết đơn.",
  "Công thức của propane là?",
  "C3H8.",
  "Công thức chung alkane mạch hở là?\nA. CnH2n\nB. CnH2n+2\nC. CnH2n−2\nD. CnHn",
  ["CnH2n", "CnH2n+2", "CnH2n−2", "CnHn"], 1,
  "Hydrocarbon là nguyên liệu cho nhiên liệu và công nghiệp hóa dầu.",
  "Một alkane có 5 carbon có công thức phân tử gì?",
  "C5H12."
),

# =========================
# GRADE 12
# =========================
L(12, "este-lipit", "Este và lipid", "🧴",
  "Hiểu cấu tạo, phản ứng thủy phân và ứng dụng của ester, lipid.",
  "Mùi hương và chất béo",
  "Nhiều ester tạo mùi thơm; triglyceride là thành phần chính của chất béo.",
  "Phản ứng ester hóa: RCOOH + R'OH ⇌ RCOOR' + H2O\nXà phòng hóa chất béo tạo glycerol và muối acid béo.",
  "Ví dụ: CH3COOH + C2H5OH ⇌ CH3COOC2H5 + H2O",
  "Ethanol phản ứng với acetic acid tạo ester nào?",
  "Ethyl acetate: CH3COOC2H5.",
  "Phản ứng xà phòng hóa chất béo cần chất gì thường gặp?\nA. NaOH/KOH\nB. NaCl\nC. O2\nD. N2",
  ["NaOH/KOH", "NaCl", "O2", "N2"], 0,
  "Ester dùng làm hương liệu, dung môi; chất béo là nguồn năng lượng và nguyên liệu sản xuất xà phòng.",
  "Vì sao xà phòng giúp rửa dầu mỡ bằng nước?",
  "Phân tử xà phòng có phần ưa nước và phần ưa dầu, giúp tạo micelle cuốn dầu mỡ."
),
L(12, "carbohydrate", "Carbohydrate", "🍚",
  "Tìm hiểu glucose, fructose, sucrose, starch và cellulose.",
  "Năng lượng từ thực phẩm",
  "Carbohydrate là nhóm chất quan trọng trong dinh dưỡng và vật liệu sinh học.",
  "Glucose: C6H12O6\nSucrose: C12H22O11\nTinh bột và cellulose có mắt xích liên quan C6H10O5.",
  "Glucose tham gia hô hấp tế bào: C6H12O6 + 6O2 → 6CO2 + 6H2O + năng lượng.",
  "Một phân tử glucose có bao nhiêu nguyên tử oxygen?",
  "6 nguyên tử O.",
  "Chất nào là polysaccharide?\nA. Glucose\nB. Fructose\nC. Tinh bột\nD. Sucrose",
  ["Glucose", "Fructose", "Tinh bột", "Sucrose"], 2,
  "Carbohydrate cung cấp năng lượng, tạo vật liệu thực vật và được dùng trong công nghiệp thực phẩm.",
  "Tại sao nhai cơm lâu có thể thấy vị ngọt hơn?",
  "Enzyme amylase phân giải một phần tinh bột thành đường đơn/oligosaccharide có vị ngọt."
),
L(12, "amin-amino-acid-protein", "Amino acid, peptide và protein", "🧬",
  "Hiểu cấu tạo amino acid, liên kết peptide và vai trò protein.",
  "Protein xây dựng cơ thể",
  "Protein là polymer sinh học tạo bởi các amino acid liên kết với nhau.",
  "Amino acid có dạng tổng quát H2N–CHR–COOH.\nLiên kết peptide hình thành giữa –COOH và –NH2, giải phóng H2O.",
  "Hai amino acid có thể tạo dipeptide và một phân tử H2O trong phản ứng ngưng tụ.",
  "Protein được cấu tạo từ đơn vị cơ bản nào?",
  "Amino acid.",
  "Liên kết giữa hai amino acid được gọi là?\nA. Ion\nB. Peptide\nC. Kim loại\nD. Ester",
  ["Ion", "Peptide", "Kim loại", "Ester"], 1,
  "Protein là enzyme, vật liệu cấu trúc, hormone và kháng thể trong cơ thể.",
  "Tại sao đun nóng quá mức có thể làm thay đổi tính chất của protein?",
  "Nhiệt có thể làm biến tính cấu trúc không gian của protein."
),
L(12, "polymer", "Polymer và vật liệu polymer", "♻️",
  "Tổng hợp phản ứng trùng hợp, trùng ngưng và ứng dụng polymer.",
  "Vật liệu của thời đại",
  "Polymer tạo nên nhựa, sợi, cao su và nhiều vật liệu kỹ thuật.",
  "nCH2=CH2 → (–CH2–CH2–)n\nPolyethylene (PE) là polymer của ethylene.",
  "Từ ethylene có thể tạo PE bằng phản ứng trùng hợp.",
  "Monomer của PE là gì?",
  "Ethylene C2H4.",
  "Polymer nào được tạo từ ethylene?\nA. PE\nB. PVC\nC. Nylon-6,6\nD. Teflon",
  ["PE", "PVC", "Nylon-6,6", "Teflon"], 0,
  "Polymer dùng trong bao bì, sợi, y tế, điện tử và vật liệu xây dựng.",
  "Tại sao tái chế và thiết kế polymer dễ thu hồi lại quan trọng?",
  "Giúp giảm rác thải, tiết kiệm nguyên liệu và giảm tác động môi trường."
),
L(12, "dien-hoa", "Điện hóa học và pin", "🔋",
  "Hiểu pin galvanic, điện cực và quá trình oxi hóa-khử.",
  "Hóa học tạo ra dòng điện",
  "Pin biến năng lượng hóa học thành điện năng nhờ phản ứng oxi hóa-khử tự phát.",
  "Anode: xảy ra oxi hóa\nCathode: xảy ra khử\nE°cell = E°cathode − E°anode",
  "Pin Zn–Cu: Zn → Zn²⁺ + 2e; Cu²⁺ + 2e → Cu.",
  "Nếu E°Cu²⁺/Cu = +0,34 V và E°Zn²⁺/Zn = −0,76 V, E°pin bằng?",
  "E° = 0,34 − (−0,76) = 1,10 V.",
  "Trong pin galvanic, oxi hóa xảy ra ở đâu?\nA. Cathode\nB. Anode\nC. Cầu muối\nD. Vỏ pin",
  ["Cathode", "Anode", "Cầu muối", "Vỏ pin"], 1,
  "Pin và acquy cung cấp năng lượng cho điện thoại, xe điện và thiết bị điện.",
  "Vì sao pin cần hai điện cực có thế khử khác nhau?",
  "Chênh lệch thế điện cực tạo động lực cho electron chuyển qua mạch ngoài."
),
L(12, "hoa-hoc-moi-truong", "Hóa học và môi trường", "🌱",
  "Vận dụng kiến thức hóa học để hiểu ô nhiễm và phát triển bền vững.",
  "Hóa học xanh",
  "Hóa học vừa tạo ra vật liệu hữu ích vừa có thể gây ô nhiễm nếu chất thải không được kiểm soát.",
  "Một số khí gây ô nhiễm: CO, SO2, NOx. Phú dưỡng liên quan dư thừa hợp chất nitrogen/phosphorus.\nNguyên tắc hóa học xanh: giảm chất thải, tăng hiệu suất nguyên tử, dùng dung môi an toàn hơn.",
  "SO2 và NOx có thể góp phần tạo mưa acid; CO gây độc do cản trở vận chuyển oxygen trong máu.",
  "Biện pháp nào phù hợp với hóa học xanh?",
  "Giảm chất thải và thay thế chất/quy trình nguy hiểm bằng lựa chọn an toàn hơn.",
  "Khí nào góp phần gây mưa acid?\nA. SO2\nB. He\nC. Ne\nD. O2",
  ["SO2", "He", "Ne", "O2"], 0,
  "Xử lý khí thải, nước thải, tái chế và thiết kế vật liệu bền vững đều cần hóa học.",
  "Vì sao không thể chỉ giải quyết ô nhiễm bằng cách 'đem chất thải đi nơi khác'?",
  "Chất ô nhiễm vẫn tồn tại và có thể chuyển sang đất, nước hoặc không khí; cần giảm và xử lý từ nguồn."
),
]


def main():
    db = SessionLocal()
    try:
        subject = db.scalar(
            select(Subject).where(Subject.slug == "chemistry")
        )

        if subject is None:
            raise RuntimeError(
                "Không tìm thấy subject 'chemistry'. "
                "Hãy chạy seed/init_db trước."
            )

        print(f"[OK] Tìm thấy subject Hóa học, ID = {subject.id}")
        created = 0
        updated = 0

        for data in LESSONS:
            lesson = db.scalar(
                select(Lesson).where(
                    Lesson.subject_id == subject.id,
                    Lesson.grade == data["grade"],
                    Lesson.topic == data["topic"],
                )
            )

            if lesson is None:
                lesson = Lesson(subject_id=subject.id, **data)
                db.add(lesson)
                created += 1
                action = "CREATE"
            else:
                for key, value in data.items():
                    setattr(lesson, key, value)
                updated += 1
                action = "UPDATE"

            print(
                f"[{action}] Lớp {data['grade']} | "
                f"{data['topic']} | {data['title']}"
            )



        db.commit()

        print("\n" + "=" * 60)
        print(f"ĐÃ XỬ LÝ: {len(LESSONS)} BÀI HÓA HỌC")
        print(f"TẠO MỚI: {created}")
        print(f"CẬP NHẬT: {updated}")
        print("=" * 60)

    finally:
        db.close()


if __name__ == "__main__":
    main()
