
/* =========================================================
   MATH GRADE PAGE
   HỌC ĐỂ LÀM GÌ
   API VERSION
========================================================= */


/* =========================================================
   GET GRADE
========================================================= */

const urlParams =
    new URLSearchParams(window.location.search);

const grade =
    urlParams.get("grade") || "10";

const API_BASE =
    "http://127.0.0.1:8000/api";


/* =========================================================
   ELEMENTS
========================================================= */

const gradeTitle =
    document.getElementById("gradeTitle");

const gradeDescription =
    document.getElementById("gradeDescription");

const topicsGrid =
    document.getElementById("topicsGrid");

const topicCount =
    document.getElementById("topicCount");

const lessonCount =
    document.getElementById("lessonCount");

const challengeCount =
    document.getElementById("challengeCount");

const progressPercent =
    document.getElementById("progressPercent");

const progressFill =
    document.getElementById("progressFill");

const progressText =
    document.getElementById("progressText");

const xpCount =
    document.getElementById("xpCount");


/* =========================================================
   TOPIC POPUP ELEMENTS
========================================================= */

const topicPopup =
    document.getElementById("topicPopup");

const popupClose =
    document.getElementById("popupClose");

const popupIcon =
    document.getElementById("popupIcon");

const popupLabel =
    document.getElementById("popupLabel");

const popupTitle =
    document.getElementById("popupTitle");

const popupDescription =
    document.getElementById("popupDescription");

const popupLessons =
    document.getElementById("popupLessons");

const popupXP =
    document.getElementById("popupXP");

const popupStart =
    document.getElementById("popupStart");


/* =========================================================
   GRADE INFORMATION
========================================================= */

const gradeDescriptions = {

    1: "Làm quen với những con số, phép tính và hình dạng đầu tiên.",

    2: "Phát triển khả năng tính toán và tư duy logic.",

    3: "Mở rộng khả năng tính toán và giải quyết vấn đề.",

    4: "Xây dựng nền tảng vững chắc về số học và hình học.",

    5: "Hoàn thiện nền tảng toán học tiểu học.",

    6: "Bước vào thế giới toán học THCS.",

    7: "Khám phá đại số và hình học thông qua tư duy logic.",

    8: "Phát triển tư duy đại số và khả năng giải quyết vấn đề.",

    9: "Chuẩn bị nền tảng toán học cho bậc THPT.",

    10: "Xây dựng nền tảng tư duy toán học và khám phá cách Toán được sử dụng để giải quyết vấn đề.",

    11: "Tiến sâu vào giải tích, hình học và xác suất.",

    12: "Chinh phục những kiến thức trọng tâm và vận dụng Toán vào giải quyết vấn đề."

};


/* =========================================================
   ICON MAP
========================================================= */

const topicIcons = {

    "so-hoc": "🔢",
    "so-tu-nhien": "🔢",
    "so-huu-ti": "🔢",
    "so-thap-phan": "🔢",
    "so-phuc": "🔢",

    "phep-cong": "➕",
    "phep-tru": "➖",
    "phep-nhan": "✖️",
    "phep-chia": "➗",

    "phan-so": "➗",

    "dai-luong": "📏",
    "do-luong": "📏",

    "hinh-hoc": "📐",

    "du-lieu": "📊",
    "bieu-do": "📊",
    "thong-ke": "📊",

    "ti-so": "🎯",
    "toan-thuc-te": "🎯",
    "ung-dung": "🎯",

    "tu-duy-logic": "🧠",
    "logic": "🧠",

    "bieu-thuc": "🔣",
    "phuong-trinh": "📈",
    "can-thuc": "√",

    "ham-so": "📈",

    "menh-de": "🔣",
    "tap-hop": "🧩",
    "vecto": "➡️",

    "dai-so": "📈",
    "gioi-han": "∞",
    "dao-ham": "∫",
    "nguyen-ham": "∫",

    "xac-suat": "🎲",

    "on-tap-thpt": "🏆"

};


/* =========================================================
   FALLBACK DESCRIPTIONS
========================================================= */

const topicDescriptions = {

    "menh-de":
        "Làm quen với ngôn ngữ và tư duy logic của Toán học.",

    "tap-hop":
        "Khám phá tập hợp, phép toán trên tập hợp và ứng dụng.",

    "ham-so":
        "Hiểu hàm số và cách mô tả sự thay đổi.",

    "vecto":
        "Khám phá vectơ và các ứng dụng hình học.",

    "hinh-hoc":
        "Khám phá các kiến thức hình học và ứng dụng.",

    "thong-ke":
        "Thu thập, biểu diễn và phân tích dữ liệu.",

    "so-hoc":
        "Làm việc với các số và phép tính.",

    "phep-cong":
        "Khám phá phép cộng qua những tình huống gần gũi.",

    "phep-tru":
        "Hiểu cách lấy bớt và tìm phần còn lại.",

    "phep-nhan":
        "Khám phá phép nhân và ứng dụng.",

    "phep-chia":
        "Hiểu và vận dụng phép chia.",

    "phan-so":
        "Khám phá và thực hiện các phép toán với phân số.",

    "dai-luong":
        "Làm việc với các đại lượng và đơn vị đo.",

    "do-luong":
        "Làm quen với độ dài, thời gian và đơn vị.",

    "du-lieu":
        "Thu thập và biểu diễn dữ liệu.",

    "bieu-do":
        "Đọc và phân tích dữ liệu bằng biểu đồ.",

    "xac-suat":
        "Khám phá xác suất và các bài toán thực tế.",

    "toan-thuc-te":
        "Vận dụng Toán học để giải quyết các vấn đề thực tế."

};


/* =========================================================
   DATA
========================================================= */

let lessons = [];

let topics = [];

let selectedTopic = null;


/* =========================================================
   PROGRESS STORAGE
========================================================= */

const storageKey =
    "hoc-de-lam-gi-math-grade-" + grade;

let progress =
    Number(
        localStorage.getItem(storageKey)
    ) || 0;

progress =
    Math.min(
        100,
        Math.max(
            0,
            progress
        )
    );


/* =========================================================
   LOAD LESSONS FROM API
========================================================= */

async function loadLessons() {

    try {

        console.log(
            "Đang tải dữ liệu Toán lớp",
            grade
        );

        const url =
            `${API_BASE}/content/subjects/math/lessons?grade=${encodeURIComponent(grade)}`;

        console.log(
            "API:",
            url
        );

        const response =
            await fetch(url);

        if (!response.ok) {

            throw new Error(
                `HTTP ${response.status}`
            );

        }

        lessons =
            await response.json();

        console.log(
            "Đã tải:",
            lessons.length,
            "bài học"
        );

        if (!Array.isArray(lessons)) {

            throw new Error(
                "API không trả về danh sách bài học"
            );

        }

        buildTopics();

        renderPage();

    }

    catch (error) {

        console.error(
            "LỖI LOAD LESSONS:",
            error
        );

        if (topicsGrid) {

            topicsGrid.innerHTML = `

                <div style="
                    grid-column:1/-1;
                    text-align:center;
                    padding:40px;
                ">

                    <h3>
                        Không thể tải dữ liệu bài học
                    </h3>

                    <p>
                        ${error.message}
                    </p>

                    <button
                        onclick="location.reload()"
                        style="
                            margin-top:15px;
                            padding:10px 20px;
                            cursor:pointer;
                        "
                    >
                        Thử lại
                    </button>

                </div>

            `;

        }

    }

}


/* =========================================================
   BUILD TOPICS FROM API
========================================================= */

function buildTopics() {

    const topicMap = new Map();


    lessons.forEach(
        function (lesson) {

            if (!topicMap.has(lesson.topic)) {

                topicMap.set(
                    lesson.topic,
                    {
                        slug: lesson.topic,

                        name: lesson.title,

                        description:
                            lesson.description ||
                            topicDescriptions[lesson.topic] ||
                            "Khám phá kiến thức Toán học.",

                        icon:
                            lesson.icon ||
                            topicIcons[lesson.topic] ||
                            "📚",

                        lessons: 0

                    }
                );

            }

            topicMap.get(
                lesson.topic
            ).lessons++;

        }
    );


    topics =
        Array.from(
            topicMap.values()
        );


    console.log(
        "Các chủ đề:",
        topics
    );

}


/* =========================================================
   RENDER PAGE
========================================================= */

function renderPage() {

    const gradeNumber =
        Number(grade);


    /* =========================
       HEADER
    ========================= */

    if (gradeTitle) {

        gradeTitle.textContent =
            `TOÁN LỚP ${grade}`;

    }


    if (gradeDescription) {

        gradeDescription.textContent =
            gradeDescriptions[gradeNumber] ||
            "Khám phá Toán học qua kiến thức và thực hành.";

    }


    /* =========================
       STATISTICS
    ========================= */

    const totalLessons =
        lessons.length;


    if (topicCount) {

        topicCount.textContent =
            topics.length;

    }


    if (lessonCount) {

        lessonCount.textContent =
            totalLessons;

    }


    if (challengeCount) {

        challengeCount.textContent =
            Math.max(
                1,
                Math.ceil(
                    topics.length / 2
                )
            );

    }


    /* =========================
       PROGRESS
    ========================= */

    updateProgress(
        totalLessons
    );


    /* =========================
       XP
    ========================= */

    if (xpCount) {

        xpCount.textContent =
            Math.round(
                progress * 10
            );

    }


    /* =========================
       TOPICS
    ========================= */

    renderTopics();

}


/* =========================================================
   UPDATE PROGRESS
========================================================= */

function updateProgress(
    totalLessons
) {

    if (progressPercent) {

        progressPercent.textContent =
            progress + "%";

    }


    if (progressFill) {

        progressFill.style.width =
            progress + "%";

    }


    const completedLessons =
        Math.round(
            totalLessons *
            progress /
            100
        );


    if (progressText) {

        progressText.textContent =
            completedLessons +
            " / " +
            totalLessons +
            " bài học hoàn thành";

    }

}


/* =========================================================
   TOPIC PROGRESS
========================================================= */

function getTopicProgress(
    index
) {

    if (progress <= 0) {

        return 0;

    }


    if (index === 0) {

        return progress;

    }


    return Math.max(
        0,
        Math.min(
            100,
            progress - index * 12
        )
    );

}


/* =========================================================
   RENDER TOPICS
========================================================= */

function renderTopics() {

    if (!topicsGrid) {
        return;
    }


    topicsGrid.innerHTML = "";


    topics.forEach(
        function (topic, index) {

            const topicProgress =
                getTopicProgress(index);


            const card =
                document.createElement("button");


            card.type =
                "button";


            card.className =
                "topic-card";


            card.dataset.topic =
                topic.slug;


            card.innerHTML = `

                <div class="topic-top">

                    <div class="topic-icon">
                        ${topic.icon}
                    </div>

                    <span class="topic-number">
                        CHỦ ĐỀ
                        ${String(index + 1).padStart(2, "0")}
                    </span>

                </div>

                <h3>
                    ${topic.name}
                </h3>

                <p>
                    ${topic.description}
                </p>

                <div class="topic-progress">

                    <div class="topic-progress-top">

                        <span>
                            ${topic.lessons} bài học
                        </span>

                        <span>
                            ${topicProgress}%
                        </span>

                    </div>

                    <div class="topic-progress-bar">

                        <div
                            class="topic-progress-fill"
                            style="width:${topicProgress}%">
                        </div>

                    </div>

                </div>

                <span class="topic-arrow">
                    →
                </span>

            `;


            card.addEventListener(
                "click",
                function () {

                    openTopic(
                        topic
                    );

                }
            );


            topicsGrid.appendChild(
                card
            );

        }
    );

}


/* =========================================================
   OPEN TOPIC
========================================================= */

function openTopic(topic) {

    if (!topic) {
        return;
    }


    selectedTopic =
        topic;


    if (popupIcon) {

        popupIcon.textContent =
            topic.icon;

    }


    if (popupLabel) {

        popupLabel.textContent =
            `TOÁN LỚP ${grade}`;

    }


    if (popupTitle) {

        popupTitle.textContent =
            topic.name;

    }


    if (popupDescription) {

        popupDescription.textContent =
            topic.description;

    }


    if (popupLessons) {

        popupLessons.textContent =
            topic.lessons;

    }


    if (popupXP) {

        popupXP.textContent =
            topic.lessons * 10;

    }


    const topicIndex =
        topics.findIndex(
            function (item) {

                return item.slug ===
                    topic.slug;

            }
        );


    const topicProgress =
        getTopicProgress(
            topicIndex
        );


    if (popupStart) {

        if (topicProgress >= 100) {

            popupStart.innerHTML =
                "Ôn tập lại <span>→</span>";

        }

        else if (topicProgress > 0) {

            popupStart.innerHTML =
                "Tiếp tục học <span>→</span>";

        }

        else {

            popupStart.innerHTML =
                "Bắt đầu học <span>→</span>";

        }

    }


    if (topicPopup) {

        topicPopup.classList.add(
            "show"
        );

        document.body.classList.add(
            "popup-open"
        );

    }

}


/* =========================================================
   CLOSE POPUP
========================================================= */

function closeTopicPopup() {

    if (topicPopup) {

        topicPopup.classList.remove(
            "show"
        );

    }


    document.body.classList.remove(
        "popup-open"
    );


    selectedTopic = null;

}


/* =========================================================
   CLOSE BUTTON
========================================================= */

if (popupClose) {

    popupClose.addEventListener(
        "click",
        closeTopicPopup
    );

}


/* =========================================================
   CLICK OUTSIDE
========================================================= */

if (topicPopup) {

    topicPopup.addEventListener(
        "click",
        function (event) {

            if (
                event.target ===
                topicPopup
            ) {

                closeTopicPopup();

            }

        }
    );

}


/* =========================================================
   ESC
========================================================= */

document.addEventListener(
    "keydown",
    function (event) {

        if (
            event.key === "Escape" &&
            topicPopup &&
            topicPopup.classList.contains("show")
        ) {

            closeTopicPopup();

        }

    }
);


/* =========================================================
   START TOPIC
========================================================= */

if (popupStart) {

    popupStart.addEventListener(
        "click",
        function () {

            if (
                !selectedTopic ||
                !selectedTopic.slug
            ) {

                return;

            }


            const topicLessons = lessons.filter(
    function (lesson) {
        return lesson.topic === selectedTopic.slug;
    }
);

if (topicLessons.length === 0) {
    alert("Không tìm thấy bài học.");
    return;
}

const firstLesson = topicLessons[0];

const lessonURL =
    "lesson.html" +
    "?id=" +
    encodeURIComponent(firstLesson.id) +
    "&subject=math" +
    "&grade=" +
    encodeURIComponent(grade) +
    "&topic=" +
    encodeURIComponent(selectedTopic.slug);

window.location.href = lessonURL;
        }
    );

}


/* =========================================================
   BACK BUTTON
========================================================= */

const backButton =
    document.getElementById("backButton");


if (backButton) {

    backButton.addEventListener(
        "click",
        function () {

            window.location.href =
                "math.html";

        }
    );

}


/* =========================================================
   REAL LIFE CHALLENGE
========================================================= */

const challengeButton =
    document.getElementById("challengeButton");


if (challengeButton) {

    challengeButton.addEventListener(
        "click",
        function () {

            alert(
                "Khu vực Thử thách thực tế sẽ được xây dựng trong hệ thống HỌC ĐỂ LÀM GÌ."
            );

        }
    );

}


/* =========================================================
   CALCULATOR
========================================================= */

const calculatorButton =
    document.getElementById("calculatorButton");


if (calculatorButton) {

    calculatorButton.addEventListener(
        "click",
        function () {

            alert(
                "Máy tính Toán học sẽ được xây dựng thành công cụ riêng."
            );

        }
    );

}


/* =========================================================
   PROGRESS BUTTON
========================================================= */

const progressButton =
    document.getElementById("progressButton");


if (progressButton) {

    progressButton.addEventListener(
        "click",
        function () {

            alert(
                "Trang phân tích năng lực sẽ được xây dựng sau hệ thống bài học."
            );

        }
    );

}


/* =========================================================
   INIT
========================================================= */

document.addEventListener(
    "DOMContentLoaded",
    function () {

        loadLessons();

    }
);


/* =========================================================
   DEBUG
========================================================= */

console.log(
    "HỌC ĐỂ LÀM GÌ - Math Grade API",
    grade
);

