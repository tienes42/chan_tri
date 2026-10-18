/* =========================================================
   HỌC ĐỂ LÀM GÌ — CHEMISTRY GRADE
   Trang chọn chủ đề Hóa học lớp 6 → 12
   API hiện tại:
   GET http://127.0.0.1:8000/api/content/subjects/chemistry/lessons?grade=6
========================================================= */

const API_BASE = "http://127.0.0.1:8000/api";

const params = new URLSearchParams(window.location.search);
const grade = params.get("grade") || "6";

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

const topicPopup = $("topicPopup");
const popupClose = $("popupClose");
const popupIcon = $("popupIcon");
const popupLabel = $("popupLabel");
const popupTitle = $("popupTitle");
const popupDescription = $("popupDescription");
const popupLessons = $("popupLessons");
const popupXP = $("popupXP");
const popupStart = $("popupStart");

let lessons = [];
let topics = [];
let selectedTopic = null;

/* =========================================================
   GRADE DESCRIPTIONS
========================================================= */

const gradeDescriptions = {
    6: "Khám phá chất, vật liệu, hỗn hợp, dung dịch và những biến đổi hóa học quanh ta.",
    7: "Tìm hiểu nguyên tử, nguyên tố, phân tử, đơn chất, hợp chất và phản ứng hóa học.",
    8: "Làm quen với công thức hóa học, phương trình hóa học, mol, dung dịch và acid-base.",
    9: "Khám phá kim loại, phi kim, hydrocarbon và các vật liệu hóa học trong đời sống.",
    10: "Tìm hiểu cấu tạo nguyên tử, electron, bảng tuần hoàn, liên kết và phản ứng oxi hóa-khử.",
    11: "Đi sâu vào tốc độ phản ứng, cân bằng hóa học, sự điện li và hóa học vô cơ quan trọng.",
    12: "Khám phá hóa học hữu cơ, polymer, điện hóa học và vai trò của hóa học với môi trường."
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
   PROGRESS
========================================================= */

function getProgress() {
    const key = `hoc-de-lam-gi-chemistry-grade-${grade}`;
    const value = Number(localStorage.getItem(key)) || 0;

    return Math.min(100, Math.max(0, value));
}

function updateProgress() {
    const progress = getProgress();
    const total = lessons.length;
    const completed = Math.round(total * progress / 100);

    if (progressPercent) {
        progressPercent.textContent = `${progress}%`;
    }

    if (progressFill) {
        progressFill.style.width = `${progress}%`;
    }

    if (progressText) {
        progressText.textContent =
            `${completed} / ${total} bài học hoàn thành`;
    }

    if (xpCount) {
        xpCount.textContent = String(Math.round(progress * 10));
    }

    if (xpProgress) {
        xpProgress.style.width = `${progress}%`;
    }
}

function getTopicProgress(index) {
    const progress = getProgress();

    if (progress <= 0) {
        return 0;
    }

    if (index === 0) {
        return progress;
    }

    return Math.max(
        0,
        Math.min(100, progress - index * 12)
    );
}

/* =========================================================
   BUILD TOPICS
   Mỗi topic trong API hiện tại tương ứng một bài học.
========================================================= */

function buildTopics() {
    const map = new Map();

    lessons.forEach((lesson) => {

        const slug =
            lesson.topic ||
            `topic-${lesson.id}`;

        if (!map.has(slug)) {

            map.set(slug, {
                slug,
                name: lesson.title || slug,

                description:
                    lesson.description ||
                    "Khám phá kiến thức Hóa học và cách vận dụng vào thực tế.",

                icon:
                    lesson.icon ||
                    "🧪",

                lessons: 0
            });
        }

        map.get(slug).lessons++;
    });

    topics = [...map.values()];
}

/* =========================================================
   RENDER PAGE
========================================================= */

function renderPage() {

    const gradeNumber = Number(grade);

    if (gradeTitle) {
        gradeTitle.textContent =
            `HÓA HỌC LỚP ${grade}`;
    }

    if (gradeDescription) {

        gradeDescription.textContent =
            gradeDescriptions[gradeNumber] ||
            "Khám phá kiến thức Hóa học và ứng dụng trong đời sống.";
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
            Math.max(1, topics.length);
    }

    updateProgress();

    renderTopics();
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
                    color:#64748b
                "
            >
                <strong>
                    Chưa có dữ liệu bài học cho lớp
                    ${escapeHTML(grade)}.
                </strong>
            </div>
        `;

        return;
    }

    topicsGrid.innerHTML = "";

    topics.forEach((topic, index) => {

        const progress =
            getTopicProgress(index);

        const card =
            document.createElement("button");

        card.type = "button";

        card.className =
            "topic-card";

        card.dataset.topic =
            topic.slug;

        card.innerHTML = `
            <div class="topic-top">

                <div class="topic-icon">
                    ${escapeHTML(topic.icon)}
                </div>

                <span class="topic-number">
                    CHỦ ĐỀ ${String(index + 1).padStart(2, "0")}
                </span>

            </div>

            <h3>
                ${escapeHTML(topic.name)}
            </h3>

            <p>
                ${escapeHTML(topic.description)}
            </p>

            <div class="topic-progress">

                <div class="topic-progress-top">

                    <span>
                        ${topic.lessons} bài học
                    </span>

                    <span>
                        ${progress}%
                    </span>

                </div>

                <div class="topic-progress-bar">

                    <div
                        class="topic-progress-fill"
                        style="width:${progress}%"
                    ></div>

                </div>

            </div>

            <span class="topic-arrow">
                →
            </span>
        `;

        card.addEventListener(
            "click",
            () => openTopic(topic)
        );

        topicsGrid.appendChild(card);
    });
}

/* =========================================================
   OPEN TOPIC POPUP
========================================================= */

function openTopic(topic) {

    if (!topic) {
        return;
    }

    selectedTopic = topic;

    const index =
        topics.findIndex(
            (item) =>
                item.slug === topic.slug
        );

    const progress =
        getTopicProgress(index);

    if (popupIcon) {
        popupIcon.textContent =
            topic.icon;
    }

    if (popupLabel) {
        popupLabel.textContent =
            `HÓA HỌC LỚP ${grade}`;
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

        popupStart.innerHTML =
            progress >= 100
                ? "Ôn tập lại <span>→</span>"
                : progress > 0
                    ? "Tiếp tục học <span>→</span>"
                    : "Bắt đầu học <span>→</span>";
    }

    if (topicPopup) {

        topicPopup.classList.add("show");

        topicPopup.setAttribute(
            "aria-hidden",
            "false"
        );

        document.body.style.overflow =
            "hidden";
    }
}

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

    selectedTopic = null;
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
                    color:#64748b
                "
            >
                Đang tải bài học Hóa học lớp
                ${escapeHTML(grade)}...
            </div>
        `;
    }

    const url =
        `${API_BASE}/content/subjects/chemistry/lessons?grade=${encodeURIComponent(grade)}`;

    console.log(
        "HỌC ĐỂ LÀM GÌ - Chemistry Grade API"
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
            await fetch(url);

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

        lessons = data;

        console.log(
            "Đã tải:",
            lessons.length,
            "bài học"
        );

        console.log(
            "Danh sách bài Hóa học:",
            lessons
        );

        buildTopics();

        renderPage();

    } catch (error) {

        console.error(
            "LỖI LOAD CHEMISTRY LESSONS:",
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
                        color:#991b1b
                    "
                >

                    <h3 style="margin-bottom:8px">
                        Không thể tải bài học
                    </h3>

                    <p
                        style="
                            color:#64748b;
                            margin-bottom:16px
                        "
                    >
                        ${escapeHTML(error.message)}
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
                            font-weight:700
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
        () => {

            window.location.href =
                "chemistry.html";
        }
    );
}

/* =========================================================
   POPUP EVENTS
========================================================= */

if (popupClose) {

    popupClose.addEventListener(
        "click",
        closePopup
    );
}

if (topicPopup) {

    topicPopup.addEventListener(
        "click",
        (event) => {

            if (
                event.target ===
                topicPopup
            ) {
                closePopup();
            }
        }
    );
}

document.addEventListener(
    "keydown",
    (event) => {

        if (
            event.key === "Escape" &&
            topicPopup &&
            topicPopup.classList.contains("show")
        ) {
            closePopup();
        }
    }
);

/* =========================================================
   START LESSON
   Quan trọng:
   dùng lesson.id từ API,
   không dùng topic làm id.
========================================================= */

if (popupStart) {

    popupStart.addEventListener(
        "click",
        () => {

            if (
                !selectedTopic ||
                !selectedTopic.slug
            ) {
                return;
            }

            const topicLessons =
                lessons.filter(
                    (lesson) =>
                        lesson.topic ===
                        selectedTopic.slug
                );

            if (!topicLessons.length) {

                alert(
                    "Không tìm thấy bài học."
                );

                return;
            }

            const firstLesson =
                topicLessons[0];

            const lessonId =
                firstLesson.id;

            console.log(
                "Lesson được chọn:",
                firstLesson
            );

            console.log(
                "Lesson ID:",
                lessonId
            );

            /*
             * KIỂM TRA LỖI LESSON ID
             */

            if (
                lessonId === undefined ||
                lessonId === null ||
                lessonId === ""
            ) {

                console.error(
                    "LESSON KHÔNG CÓ ID:",
                    firstLesson
                );

                alert(
                    "Bài học này không có ID từ API."
                );

                return;
            }

            /*
             * TẠO URL ĐẾN TRANG LESSON
             */

            const lessonURL =
                "lesson.html" +
                "?id=" +
                encodeURIComponent(
                    lessonId
                ) +
                "&subject=chemistry" +
                "&grade=" +
                encodeURIComponent(
                    firstLesson.grade ||
                    grade
                ) +
                "&topic=" +
                encodeURIComponent(
                    firstLesson.topic ||
                    ""
                );

            console.log(
                "Mở lesson:",
                lessonURL
            );

            window.location.href =
                lessonURL;
        }
    );
}

/* =========================================================
   EXTRA BUTTONS
========================================================= */

const challengeButton =
    $("challengeButton");

if (challengeButton) {

    challengeButton.addEventListener(
        "click",
        () => {

            alert(
                "Phần thử thách thực tế sẽ kết nối với hệ thống nhiệm vụ và game ở bước tiếp theo."
            );
        }
    );
}

const calculatorButton =
    $("calculatorButton");

if (calculatorButton) {

    calculatorButton.addEventListener(
        "click",
        () => {

            alert(
                "Công cụ Hóa học sẽ được xây dựng sau khi hoàn thiện hệ thống bài học."
            );
        }
    );
}

const progressButton =
    $("progressButton");

if (progressButton) {

    progressButton.addEventListener(
        "click",
        () => {

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
    loadLessons
);