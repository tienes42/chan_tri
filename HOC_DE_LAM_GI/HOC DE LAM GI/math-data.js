/* =========================================================
   MATH GRADE PAGE
   PostgreSQL -> FastAPI -> Frontend
========================================================= */

const API_BASE = "http://127.0.0.1:8000/api";

/* =========================
   GET GRADE
========================= */

const params = new URLSearchParams(window.location.search);

const grade = params.get("grade") || "10";


/* =========================
   ELEMENTS
========================= */

const backButton =
    document.getElementById("backButton");

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

const xpCount =
    document.getElementById("xpCount");

const challengeCount =
    document.getElementById("challengeCount");

const progressPercent =
    document.getElementById("progressPercent");

const progressFill =
    document.getElementById("progressFill");

const progressText =
    document.getElementById("progressText");

const challengeButton =
    document.getElementById("challengeButton");

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


/* =========================
   TOPIC ICONS
========================= */

const topicIcons = {
    "menh-de": "💡",
    "tap-hop": "⭕",
    "ham-so": "📈",
    "vecto": "➡️",
    "hinh-hoc": "📐",
    "thong-ke": "📊"
};


/* =========================
   TOPIC NAMES
========================= */

const topicNames = {
    "menh-de": "Mệnh đề",
    "tap-hop": "Tập hợp",
    "ham-so": "Hàm số",
    "vecto": "Vectơ",
    "hinh-hoc": "Hình học tọa độ",
    "thong-ke": "Thống kê"
};


/* =========================
   CURRENT DATA
========================= */

let lessons = [];
let selectedTopic = null;


/* =========================
   BACK BUTTON
========================= */

if (backButton) {

    backButton.addEventListener(
        "click",
        function () {

            window.location.href =
                "math.html";

        }
    );

}


/* =========================
   LOAD LESSONS
========================= */

async function loadLessons() {

    try {

        topicsGrid.innerHTML = `
            <div style="
                grid-column: 1 / -1;
                text-align: center;
                padding: 40px;
            ">
                Đang tải bài học...
            </div>
        `;

        const response = await fetch(
            `${API_BASE}/content/subjects/math/lessons?grade=${grade}`
        );

        if (!response.ok) {

            throw new Error(
                `API error: ${response.status}`
            );

        }

        lessons = await response.json();

        renderPage();

    } catch (error) {

        console.error(
            "Không thể tải dữ liệu:",
            error
        );

        topicsGrid.innerHTML = `
            <div style="
                grid-column: 1 / -1;
                text-align: center;
                padding: 40px;
                color: #d00;
            ">
                Không thể kết nối tới máy chủ.
                <br><br>
                Hãy kiểm tra FastAPI đang chạy.
            </div>
        `;

    }

}


/* =========================
   GROUP TOPICS
========================= */

function groupTopics() {

    const groups = {};

    lessons.forEach(lesson => {

        if (!groups[lesson.topic]) {

            groups[lesson.topic] = [];

        }

        groups[lesson.topic].push(lesson);

    });

    return groups;

}


/* =========================
   RENDER PAGE
========================= */

function renderPage() {

    gradeTitle.textContent =
        `TOÁN LỚP ${grade}`;

    gradeDescription.textContent =
        `Khám phá những kiến thức toán học lớp ${grade}
         và biến chúng thành công cụ giải quyết
         vấn đề trong cuộc sống.`;

    const topics =
        groupTopics();

    const topicKeys =
        Object.keys(topics);

    /* =========================
       STATS
    ========================= */

    topicCount.textContent =
        topicKeys.length;

    lessonCount.textContent =
        lessons.length;

    const totalXP =
        lessons.length * 10;

    xpCount.textContent =
        totalXP;

    const challenges =
        lessons.filter(
            lesson =>
                lesson.challenge &&
                lesson.challenge.trim() !== ""
        ).length;

    challengeCount.textContent =
        challenges;

    progressPercent.textContent =
        "0%";

    progressFill.style.width =
        "0%";

    progressText.textContent =
        `0 / ${lessons.length} bài học hoàn thành`;


    /* =========================
       TOPICS
    ========================= */

    topicsGrid.innerHTML = "";

    topicKeys.forEach(topic => {

        const topicLessons =
            topics[topic];

        const firstLesson =
            topicLessons[0];

        createTopicCard(
            topic,
            topicLessons,
            firstLesson
        );

    });

}


/* =========================
   CREATE TOPIC CARD
========================= */

function createTopicCard(
    topic,
    topicLessons,
    firstLesson
) {

    const card =
        document.createElement("div");

    card.className =
        "topic-card";

    const icon =
        topicIcons[topic] ||
        firstLesson.icon ||
        "📚";

    const title =
        topicNames[topic] ||
        firstLesson.title ||
        topic;

    const description =
        firstLesson.description ||
        "Khám phá chủ đề này.";

    card.innerHTML = `

        <div class="topic-icon">
            ${icon}
        </div>

        <div class="topic-info">

            <span class="topic-number">
                CHỦ ĐỀ ${Object.keys(groupTopics()).indexOf(topic) + 1}
            </span>

            <h3>
                ${title}
            </h3>

            <p>
                ${description}
            </p>

            <div class="topic-meta">

                <span>
                    📚 ${topicLessons.length} bài học
                </span>

                <span>
                    ⭐ ${topicLessons.length * 10} XP
                </span>

            </div>

        </div>

        <div class="topic-arrow">
            →
        </div>
    `;

    card.addEventListener(
        "click",
        function () {

            openTopic(
                topic,
                topicLessons,
                firstLesson
            );

        }
    );

    topicsGrid.appendChild(card);

}


/* =========================
   OPEN TOPIC
========================= */

function openTopic(
    topic,
    topicLessons,
    firstLesson
) {

    selectedTopic = topic;

    popupIcon.textContent =
        topicIcons[topic] ||
        firstLesson.icon ||
        "📚";

    popupLabel.textContent =
        `CHỦ ĐỀ · LỚP ${grade}`;

    popupTitle.textContent =
        topicNames[topic] ||
        firstLesson.title ||
        topic;

    popupDescription.textContent =
        firstLesson.description ||
        "Khám phá kiến thức và luyện tập thông qua các bài học.";

    popupLessons.textContent =
        topicLessons.length;

    popupXP.textContent =
        topicLessons.length * 10;

    topicPopup.classList.add(
        "active"
    );

}


/* =========================
   CLOSE POPUP
========================= */

if (popupClose) {

    popupClose.addEventListener(
        "click",
        function () {

            topicPopup.classList.remove(
                "active"
            );

        }
    );

}


if (topicPopup) {

    topicPopup.addEventListener(
        "click",
        function (event) {

            if (
                event.target === topicPopup
            ) {

                topicPopup.classList.remove(
                    "active"
                );

            }

        }
    );

}


/* =========================
   START TOPIC
========================= */

if (popupStart) {

    popupStart.addEventListener(
        "click",
        function () {

            if (!selectedTopic) {
                return;
            }

            const topicLessons =
                groupTopics()[selectedTopic];

            if (
                !topicLessons ||
                topicLessons.length === 0
            ) {
                return;
            }

            /*
             * Mở bài đầu tiên của chủ đề.
             * Sau đó lesson.html sẽ lấy dữ liệu
             * trực tiếp từ PostgreSQL thông qua API.
             */

            const firstLesson =
                topicLessons[0];

            window.location.href =
                `lesson.html?id=${firstLesson.id}`;

        }
    );

}


/* =========================
   REAL LIFE CHALLENGE
========================= */

if (challengeButton) {

    challengeButton.addEventListener(
        "click",
        function () {

            const lessonWithChallenge =
                lessons.find(
                    lesson =>
                        lesson.challenge &&
                        lesson.challenge.trim() !== ""
                );

            if (!lessonWithChallenge) {

                alert(
                    "Chưa có thử thách thực tế."
                );

                return;

            }

            window.location.href =
                `lesson.html?id=${lessonWithChallenge.id}`;

        }
    );

}


/* =========================
   CALCULATOR
========================= */

const calculatorButton =
    document.getElementById(
        "calculatorButton"
    );

if (calculatorButton) {

    calculatorButton.addEventListener(
        "click",
        function () {

            window.location.href =
                "calculator.html";

        }
    );

}


/* =========================
   PROGRESS
========================= */

const progressButton =
    document.getElementById(
        "progressButton"
    );

if (progressButton) {

    progressButton.addEventListener(
        "click",
        function () {

            window.location.href =
                "progress.html";

        }
    );

}


/* =========================
   START
========================= */

loadLessons();