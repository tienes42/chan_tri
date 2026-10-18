/* =========================================================
   HỌC ĐỂ LÀM GÌ — PHYSICS GRADE
   Trang chọn chủ đề Vật lý lớp 6 → 12
========================================================= */

const API_BASE = "http://127.0.0.1:8000/api";

const params = new URLSearchParams(window.location.search);
const grade = params.get("grade") || "10";

const $ = (id) => document.getElementById(id);


/* =========================================================
   ELEMENTS
========================================================= */

const gradeTitle = $("gradeTitle");
const gradeDescription = $("gradeDescription");

const topicsGrid = $("topicsGrid");

const topicCount = $("topicCount");
const lessonCount = $("lessonCount");
const challengeCount = $("challengeCount");

const progressPercent = $("progressPercent");
const progressFill = $("progressFill");
const progressText = $("progressText");

const xpCount = $("xpCount");
const xpProgress = $("xpProgress");


/* =========================================================
   POPUP
========================================================= */

const topicPopup = $("topicPopup");
const popupClose = $("popupClose");

const popupIcon = $("popupIcon");
const popupLabel = $("popupLabel");
const popupTitle = $("popupTitle");
const popupDescription = $("popupDescription");

const popupLessons = $("popupLessons");
const popupXP = $("popupXP");

const popupStart = $("popupStart");


/* =========================================================
   DATA
========================================================= */

let lessons = [];
let topics = [];
let selectedTopic = null;


/* =========================================================
   GRADE DESCRIPTIONS
========================================================= */

const gradeDescriptions = {

    6:
        "Đo lường, khối lượng, lực, chuyển động và nhiệt độ — nền tảng để hiểu thế giới vật chất.",

    7:
        "Khám phá tốc độ, âm thanh, ánh sáng, nam châm và các hiện tượng quang học.",

    8:
        "Tìm hiểu khối lượng riêng, áp suất, lực đẩy Archimedes, công, nhiệt và điện.",

    9:
        "Vận dụng điện học, quang học và điện từ học để giải thích nhiều hiện tượng thực tế.",

    10:
        "Khám phá chuyển động, gia tốc, các định luật Newton, động lượng và năng lượng.",

    11:
        "Đi sâu vào dao động, sóng, điện trường, dòng điện, từ trường và cảm ứng điện từ.",

    12:
        "Tiếp cận điện trường, dòng điện xoay chiều, mạch RLC, lượng tử và vật lý hạt nhân."

};


/* =========================================================
   TOPIC ICONS
========================================================= */

const topicIcons = {

    "do-dai": "📏",

    "khoi-luong": "⚖️",

    "luc": "💪",

    "toc-do": "🏃",

    "nhiet-do": "🌡️",

    "luc-ma-sat": "🛞",

    "toc-do-chuyen-dong": "🚗",

    "am-thanh": "🔊",

    "anh-sang": "💡",

    "guong-phang": "🪞",

    "nam-cham": "🧲",

    "anh-sang-mau": "🌈",

    "khoi-luong-rieng": "🧊",

    "ap-suat": "🎈",

    "luc-day-archimedes": "🚢",

    "cong-suat": "⚙️",

    "nhiet-nang": "🔥",

    "dien": "🔌",

    "dien-tro": "〽️",

    "doan-mach-noi-tiep": "🔗",

    "doan-mach-song-song": "🔀",

    "cong-va-cong-suat-dien": "⚡",

    "dien-tu": "🧲",

    "quang-hoc": "🔭",

    "chuyen-dong-thang": "🚀",

    "gia-toc": "📈",

    "dinh-luat-newton": "⚖️",

    "dong-luong": "💥",

    "nang-luong": "🔋",

    "dong-luc-hoc-chat-long": "🌊",

    "dao-dong": "〰️",

    "song-co": "🌊",

    "dien-truong": "⚡",

    "dong-dien": "🔌",

    "tu-truong": "🧲",

    "cam-ung-dien-tu": "🌀",

    "dien-truong-cuong-do": "⚡",

    "dien-the": "🔋",

    "mach-xoay-chieu": "〽️",

    "mach-rlc": "🔌",

    "hat-nhan": "☢️",

    "quang-dien": "☀️",

    "thuyet-tuong-doi": "🌌"

};


/* =========================================================
   TOPIC DESCRIPTIONS
========================================================= */

const topicDescriptions = {

    "do-dai":
        "Đo độ dài bằng dụng cụ thích hợp và biết cách đọc, ghi kết quả đo.",

    "khoi-luong":
        "Hiểu khối lượng và cách sử dụng cân để đo khối lượng.",

    "luc":
        "Nhận biết lực, tác dụng của lực và biểu diễn lực.",

    "toc-do":
        "Mô tả mức độ nhanh chậm của chuyển động bằng tốc độ.",

    "nhiet-do":
        "Đo và so sánh nhiệt độ, hiểu sự thay đổi nhiệt độ.",

    "luc-ma-sat":
        "Hiểu lực ma sát và vai trò của nó trong đời sống.",

    "toc-do-chuyen-dong":
        "Tính và phân tích tốc độ của các chuyển động.",

    "am-thanh":
        "Khám phá nguồn âm, độ cao, độ to và sự truyền âm.",

    "anh-sang":
        "Tìm hiểu sự truyền ánh sáng và các hiện tượng ánh sáng.",

    "guong-phang":
        "Khám phá ảnh của vật qua gương phẳng.",

    "nam-cham":
        "Tìm hiểu nam châm và tác dụng của từ trường.",

    "anh-sang-mau":
        "Giải thích màu sắc và sự phân tách ánh sáng.",

    "khoi-luong-rieng":
        "Tính khối lượng riêng và ứng dụng để nhận biết vật liệu.",

    "ap-suat":
        "Hiểu áp suất và cách áp suất thay đổi trong các tình huống thực tế.",

    "luc-day-archimedes":
        "Khám phá lực đẩy của chất lỏng và điều kiện vật nổi, chìm.",

    "cong-suat":
        "Tính công và công suất trong các quá trình cơ học.",

    "nhiet-nang":
        "Hiểu nhiệt năng và các cách truyền nhiệt.",

    "dien":
        "Làm quen với dòng điện, nguồn điện và mạch điện.",

    "dien-tro":
        "Tìm hiểu điện trở và định luật Ohm.",

    "doan-mach-noi-tiep":
        "Phân tích cường độ dòng điện và hiệu điện thế trong mạch nối tiếp.",

    "doan-mach-song-song":
        "Phân tích mạch điện mắc song song và các đại lượng đặc trưng.",

    "cong-va-cong-suat-dien":
        "Tính điện năng, công suất điện và ứng dụng trong gia đình.",

    "dien-tu":
        "Khám phá mối liên hệ giữa dòng điện và từ trường.",

    "quang-hoc":
        "Vận dụng kiến thức ánh sáng, thấu kính và tạo ảnh.",

    "chuyen-dong-thang":
        "Mô tả vị trí, quãng đường, vận tốc trong chuyển động thẳng.",

    "gia-toc":
        "Phân tích sự thay đổi vận tốc theo thời gian.",

    "dinh-luat-newton":
        "Dùng ba định luật Newton để giải thích và dự đoán chuyển động.",

    "dong-luong":
        "Hiểu động lượng và định luật bảo toàn động lượng.",

    "nang-luong":
        "Tìm hiểu công, động năng, thế năng và bảo toàn năng lượng.",

    "dong-luc-hoc-chat-long":
        "Khám phá áp suất và chuyển động của chất lưu.",

    "dao-dong":
        "Mô tả dao động điều hòa bằng các đại lượng đặc trưng.",

    "song-co":
        "Tìm hiểu sự truyền sóng và các hiện tượng giao thoa, phản xạ.",

    "dien-truong":
        "Khám phá điện trường và lực điện tác dụng lên điện tích.",

    "dong-dien":
        "Hiểu bản chất dòng điện không đổi và các định luật mạch điện.",

    "tu-truong":
        "Tìm hiểu từ trường và lực từ tác dụng lên dòng điện.",

    "cam-ung-dien-tu":
        "Khám phá hiện tượng cảm ứng điện từ và suất điện động cảm ứng.",

    "dien-truong-cuong-do":
        "Tính cường độ điện trường và phân tích điện trường.",

    "dien-the":
        "Hiểu điện thế, hiệu điện thế và mối liên hệ với công của lực điện.",

    "mach-xoay-chieu":
        "Phân tích dòng điện xoay chiều và các đại lượng hiệu dụng.",

    "mach-rlc":
        "Tìm hiểu mạch RLC và hiện tượng cộng hưởng.",

    "hat-nhan":
        "Khám phá cấu tạo hạt nhân, phóng xạ và năng lượng hạt nhân.",

    "quang-dien":
        "Tìm hiểu lượng tử ánh sáng và hiện tượng quang điện.",

    "thuyet-tuong-doi":
        "Làm quen với một số ý tưởng nền tảng của vật lý hiện đại."

};


/* =========================================================
   ESCAPE HTML
========================================================= */

function escapeHTML(value) {

    return String(value ?? "")

        .replaceAll("&", "&amp;")

        .replaceAll("<", "&lt;")

        .replaceAll(">", "&gt;")

        .replaceAll('"', "&quot;")

        .replaceAll("'", "&#039;");

}


/* =========================================================
   GET PROGRESS
========================================================= */

function getProgress() {

    const key =
        `hoc-de-lam-gi-physics-grade-${grade}`;

    const value =
        Number(
            localStorage.getItem(key)
        ) || 0;

    return Math.min(
        100,
        Math.max(
            0,
            value
        )
    );

}


/* =========================================================
   UPDATE PROGRESS
========================================================= */

function updateProgress() {

    const progress =
        getProgress();

    const total =
        lessons.length;

    const completed =
        Math.round(
            total *
            progress /
            100
        );


    if (progressPercent) {

        progressPercent.textContent =
            `${progress}%`;

    }


    if (progressFill) {

        progressFill.style.width =
            `${progress}%`;

    }


    if (progressText) {

        progressText.textContent =
            `${completed} / ${total} bài học hoàn thành`;

    }


    if (xpCount) {

        xpCount.textContent =
            String(
                Math.round(
                    progress * 10
                )
            );

    }


    if (xpProgress) {

        xpProgress.style.width =
            `${progress}%`;

    }

}


/* =========================================================
   BUILD TOPICS
========================================================= */

function buildTopics() {

    const map =
        new Map();


    lessons.forEach(
        function (lesson) {

            const slug =
                lesson.topic ||
                `topic-${lesson.id}`;


            if (!map.has(slug)) {

                map.set(
                    slug,
                    {

                        slug: slug,

                        name:
                            lesson.title ||
                            slug,

                        description:
                            lesson.description ||
                            topicDescriptions[slug] ||
                            "Khám phá kiến thức Vật lý và cách vận dụng vào thực tế.",

                        icon:
                            lesson.icon ||
                            topicIcons[slug] ||
                            "⚡",

                        lessons: 0

                    }
                );

            }


            map.get(slug).lessons++;

        }
    );


    topics =
        [...map.values()];

}


/* =========================================================
   RENDER PAGE
========================================================= */

function renderPage() {

    const gradeNumber =
        Number(grade);


    if (gradeTitle) {

        gradeTitle.textContent =
            `VẬT LÝ LỚP ${grade}`;

    }


    if (gradeDescription) {

        gradeDescription.textContent =
            gradeDescriptions[gradeNumber] ||
            "Khám phá các quy luật vật lý và ứng dụng trong đời sống.";

    }


    if (topicCount) {

        topicCount.textContent =
            topics.length;

    }


    if (lessonCount) {

        lessonCount.textContent =
            lessons.length;

    }


    if (challengeCount) {

        challengeCount.textContent =
            Math.max(
                1,
                topics.length
            );

    }


    updateProgress();

    renderTopics();

}


/* =========================================================
   TOPIC PROGRESS
========================================================= */

function getTopicProgress(index) {

    const progress =
        getProgress();


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
            progress -
            index * 12
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


    if (!topics.length) {

        topicsGrid.innerHTML = `

            <div
                style="
                    grid-column:1/-1;
                    padding:50px;
                    text-align:center;
                    color:#64748b;
                "
            >

                <strong>
                    Chưa có dữ liệu bài học
                    cho lớp ${escapeHTML(grade)}.
                </strong>

            </div>

        `;

        return;

    }


    topicsGrid.innerHTML = "";


    topics.forEach(
        function (topic, index) {

            const progress =
                getTopicProgress(index);


            const card =
                document.createElement(
                    "button"
                );


            card.type =
                "button";


            card.className =
                "topic-card";


            card.dataset.topic =
                topic.slug;


            card.innerHTML = `

                <div class="topic-top">

                    <div class="topic-icon">

                        ${escapeHTML(
                            topic.icon
                        )}

                    </div>


                    <span class="topic-number">

                        CHỦ ĐỀ
                        ${String(
                            index + 1
                        ).padStart(
                            2,
                            "0"
                        )}

                    </span>

                </div>


                <h3>

                    ${escapeHTML(
                        topic.name
                    )}

                </h3>


                <p>

                    ${escapeHTML(
                        topic.description
                    )}

                </p>


                <div class="topic-progress">

                    <div class="topic-progress-top">

                        <span>

                            ${topic.lessons}
                            bài học

                        </span>


                        <span>

                            ${progress}%

                        </span>

                    </div>


                    <div class="topic-progress-bar">

                        <div
                            class="topic-progress-fill"
                            style="
                                width:${progress}%
                            "
                        ></div>

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


    const index =
        topics.findIndex(
            function (item) {

                return (
                    item.slug ===
                    topic.slug
                );

            }
        );


    const progress =
        getTopicProgress(
            index
        );


    if (popupIcon) {

        popupIcon.textContent =
            topic.icon;

    }


    if (popupLabel) {

        popupLabel.textContent =
            `VẬT LÝ LỚP ${grade}`;

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


    if (popupStart) {

        if (progress >= 100) {

            popupStart.innerHTML =
                "Ôn tập lại <span>→</span>";

        }

        else if (progress > 0) {

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


        topicPopup.setAttribute(
            "aria-hidden",
            "false"
        );


        document.body.style.overflow =
            "hidden";

    }

}


/* =========================================================
   CLOSE POPUP
========================================================= */

function closePopup() {

    if (topicPopup) {

        topicPopup.classList.remove(
            "show"
        );


        topicPopup.setAttribute(
            "aria-hidden",
            "true"
        );

    }


    document.body.style.overflow =
        "";


    selectedTopic =
        null;

}


/* =========================================================
   LOAD LESSONS
========================================================= */

async function loadLessons() {

    if (topicsGrid) {

        topicsGrid.innerHTML = `

            <div
                style="
                    grid-column:1/-1;
                    padding:50px;
                    text-align:center;
                    color:#64748b;
                "
            >

                Đang tải bài học
                Vật lý lớp
                ${escapeHTML(grade)}...

            </div>

        `;

    }


    const url =
        `${API_BASE}/content/subjects/physics/lessons?grade=${encodeURIComponent(
            grade
        )}`;


    console.log(
        "HỌC ĐỂ LÀM GÌ - Physics Grade API"
    );


    console.log(
        "Grade:",
        grade
    );


    console.log(
        "API:",
        url
    );


    try {

        const response =
            await fetch(
                url
            );


        console.log(
            "API STATUS:",
            response.status
        );


        if (!response.ok) {

            throw new Error(
                `HTTP ${response.status}`
            );

        }


        const data =
            await response.json();


        if (!Array.isArray(data)) {

            throw new Error(
                "API không trả về danh sách bài học."
            );

        }


        lessons =
            data;


        console.log(
            "Đã tải:",
            lessons.length,
            "bài học"
        );


        buildTopics();


        console.log(
            "Các chủ đề Vật lý:",
            topics
        );


        renderPage();

    }

    catch (error) {

        console.error(
            "LỖI LOAD LESSONS:",
            error
        );


        if (topicsGrid) {

            topicsGrid.innerHTML = `

                <div
                    style="
                        grid-column:1/-1;
                        padding:45px 25px;
                        text-align:center;
                        border:1px solid #fecaca;
                        border-radius:20px;
                        background:#fff;
                        color:#991b1b;
                    "
                >

                    <h3
                        style="
                            margin-bottom:8px;
                        "
                    >

                        Không thể tải bài học

                    </h3>


                    <p
                        style="
                            color:#64748b;
                            margin-bottom:16px;
                        "
                    >

                        ${escapeHTML(
                            error.message
                        )}

                    </p>


                    <button
                        type="button"
                        id="retryLessons"
                        style="
                            border:0;
                            padding:11px 18px;
                            border-radius:10px;
                            color:white;
                            background:#0284c7;
                            cursor:pointer;
                            font-weight:700;
                        "
                    >

                        Thử lại

                    </button>

                </div>

            `;


            const retryButton =
                $("retryLessons");


            if (retryButton) {

                retryButton.addEventListener(
                    "click",
                    loadLessons
                );

            }

        }

    }

}


/* =========================================================
   BACK BUTTON
========================================================= */

const backButton =
    $("backButton");


if (backButton) {

    backButton.addEventListener(
        "click",
        function () {

            window.location.href =
                "physics.html";

        }
    );

}


/* =========================================================
   CLOSE POPUP BUTTON
========================================================= */

if (popupClose) {

    popupClose.addEventListener(
        "click",
        closePopup
    );

}


/* =========================================================
   CLICK OUTSIDE POPUP
========================================================= */

if (topicPopup) {

    topicPopup.addEventListener(
        "click",
        function (event) {

            if (
                event.target ===
                topicPopup
            ) {

                closePopup();

            }

        }
    );

}


/* =========================================================
   ESC KEY
========================================================= */

document.addEventListener(
    "keydown",
    function (event) {

        if (
            event.key === "Escape" &&
            topicPopup &&
            topicPopup.classList.contains(
                "show"
            )
        ) {

            closePopup();

        }

    }
);


/* =========================================================
   START LESSON
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


            const topicLessons =
                lessons.filter(
                    function (lesson) {

                        return (
                            lesson.topic ===
                            selectedTopic.slug
                        );

                    }
                );


            if (
                topicLessons.length === 0
            ) {

                alert(
                    "Không tìm thấy bài học."
                );

                return;

            }


            const firstLesson =
                topicLessons[0];


            const lessonURL =
                "lesson.html" +
                "?id=" +
                encodeURIComponent(
                    firstLesson.id
                ) +
                "&subject=physics" +
                "&grade=" +
                encodeURIComponent(
                    grade
                ) +
                "&topic=" +
                encodeURIComponent(
                    selectedTopic.slug
                );


            console.log(
                "Mở bài học:",
                lessonURL
            );


            window.location.href =
                lessonURL;

        }
    );

}


/* =========================================================
   CHALLENGE
========================================================= */

const challengeButton =
    $("challengeButton");


if (challengeButton) {

    challengeButton.addEventListener(
        "click",
        function () {

            alert(
                "Phần thử thách thực tế sẽ kết nối với hệ thống nhiệm vụ và game ở bước tiếp theo."
            );

        }
    );

}


/* =========================================================
   CALCULATOR
========================================================= */

const calculatorButton =
    $("calculatorButton");


if (calculatorButton) {

    calculatorButton.addEventListener(
        "click",
        function () {

            alert(
                "Công cụ Vật lý sẽ được xây dựng sau khi hoàn thiện hệ thống bài học."
            );

        }
    );

}


/* =========================================================
   PROGRESS
========================================================= */

const progressButton =
    $("progressButton");


if (progressButton) {

    progressButton.addEventListener(
        "click",
        function () {

            alert(
                "Trang phân tích tiến trình sẽ được kết nối sau khi hoàn thiện hệ thống học và game."
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