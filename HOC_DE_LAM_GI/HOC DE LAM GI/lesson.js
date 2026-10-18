/* =========================================================
   LESSON.JS
   Dùng chung cho:
   - Math
   - Physics
   - Chemistry
   - Các môn khác

   API:
   GET /api/content/lessons/{id}
========================================================= */

const API_BASE = "http://127.0.0.1:8000/api";

const params = new URLSearchParams(window.location.search);

const lessonId = params.get("id");
const subject = params.get("subject") || "math";
const gradeFromUrl = params.get("grade");


/* =========================================================
   DOM
========================================================= */

const loading =
    document.getElementById("loading");

const errorBox =
    document.getElementById("error");

const lessonContent =
    document.getElementById("lessonContent");

const backButton =
    document.getElementById("backButton");

const lessonIcon =
    document.getElementById("lessonIcon");

const lessonGrade =
    document.getElementById("lessonGrade");

const lessonTitle =
    document.getElementById("lessonTitle");

const lessonDescription =
    document.getElementById("lessonDescription");

const definition =
    document.getElementById("definition");

const concept =
    document.getElementById("concept");

const formulas =
    document.getElementById("formulas");

const meaning =
    document.getElementById("meaning");

const realLife =
    document.getElementById("realLife");

const contextTitle =
    document.getElementById("contextTitle");

const context =
    document.getElementById("context");

const theory =
    document.getElementById("theory");

const example =
    document.getElementById("example");

const exampleAnswer =
    document.getElementById("exampleAnswer");

const question =
    document.getElementById("question");

const answers =
    document.getElementById("answers");

const application =
    document.getElementById("application");

const challenge =
    document.getElementById("challenge");

const challengeAnswer =
    document.getElementById("challengeAnswer");

const gameDescription =
    document.getElementById("gameDescription");

const gameButton =
    document.getElementById("gameButton");

const noGame =
    document.getElementById("noGame");


/* =========================================================
   SECTIONS
========================================================= */

const definitionSection =
    document.getElementById("definitionSection");

const contextSection =
    document.getElementById("contextSection");

const theorySection =
    document.getElementById("theorySection");

const conceptSection =
    document.getElementById("conceptSection");

const formulaSection =
    document.getElementById("formulaSection");

const exampleSection =
    document.getElementById("exampleSection");

const questionSection =
    document.getElementById("questionSection");

const meaningSection =
    document.getElementById("meaningSection");

const applicationSection =
    document.getElementById("applicationSection");

const realLifeSection =
    document.getElementById("realLifeSection");

const challengeSection =
    document.getElementById("challengeSection");


/* =========================================================
   SUBJECT NAME
========================================================= */

const subjectNames = {

    math: "Toán học",

    physics: "Vật lý",

    chemistry: "Hóa học",

    biology: "Sinh học",

    informatics: "Tin học",

    english: "Tiếng Anh"

};


/* =========================================================
   ESCAPE HTML
========================================================= */

function escapeHTML(value) {

    if (
        value === null ||
        value === undefined
    ) {
        return "";
    }

    return String(value)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
}


/* =========================================================
   SET TEXT
========================================================= */

function setText(element, value) {

    if (!element) {
        return;
    }

    const text =
        value === null ||
        value === undefined
            ? ""
            : String(value);

    element.innerHTML =
        escapeHTML(text)
            .replace(/\n/g, "<br>");
}


/* =========================================================
   SHOW / HIDE SECTION
========================================================= */

function setSectionVisible(section, visible) {

    if (!section) {
        return;
    }

    section.style.display =
        visible
            ? ""
            : "none";
}


/* =========================================================
   BACK
========================================================= */

if (backButton) {

    backButton.addEventListener(
        "click",
        function () {

            window.history.back();

        }
    );

}


/* =========================================================
   ERROR
========================================================= */

function showError(message) {

    if (loading) {

        loading.style.display =
            "none";
    }

    if (lessonContent) {

        lessonContent.classList.add(
            "hidden"
        );
    }

    if (errorBox) {

        errorBox.textContent =
            message;

        errorBox.style.display =
            "block";

    }

}


/* =========================================================
   FINISH LOADING
========================================================= */

function finishLoading() {

    if (loading) {

        loading.style.display =
            "none";
    }

    if (errorBox) {

        errorBox.style.display =
            "none";
    }

    if (lessonContent) {

        lessonContent.classList.remove(
            "hidden"
        );
    }

}


/* =========================================================
   RENDER FORMULAS
   Hỗ trợ:

   1. formulas = [
        {
            category: "...",
            items: [...]
        }
      ]

   2. formulas = [
        {
            name: "...",
            formula: "...",
            note: "..."
        }
      ]

   3. formula = "..."
========================================================= */

function renderFormulas(data, singleFormula) {

    if (!formulas) {
        return;
    }


    /*
     * Chemistry API hiện tại sử dụng:
     *
     * "formula": "C% = ..."
     *
     * trong khi Math/Physics cũ có thể dùng:
     *
     * "formulas": [...]
     */

    let formulaData =
        data;


    if (
        (!Array.isArray(formulaData) ||
            formulaData.length === 0) &&
        singleFormula
    ) {

        formulaData = [
            singleFormula
        ];

    }


    if (
        !Array.isArray(formulaData) ||
        formulaData.length === 0
    ) {

        formulas.innerHTML =
            `<p>Chưa có công thức.</p>`;

        setSectionVisible(
            formulaSection,
            false
        );

        return;
    }


    setSectionVisible(
        formulaSection,
        true
    );


    let html = "";


    formulaData.forEach(
        function (group) {

            /*
             * GROUP
             */

            if (
                group &&
                typeof group === "object" &&
                group.category &&
                Array.isArray(group.items)
            ) {

                html += `
                    <div class="formula-category">

                        <h3 class="formula-category-title">
                            ${escapeHTML(group.category)}
                        </h3>

                        <div class="formula-category-items">
                `;


                group.items.forEach(
                    function (item) {

                        if (
                            typeof item ===
                            "string"
                        ) {

                            html += `
                                <div class="formula-item">

                                    <div class="formula-expression">
                                        ${escapeHTML(item)}
                                    </div>

                                </div>
                            `;

                            return;
                        }


                        html += `
                            <div class="formula-item">

                                ${
                                    item.name
                                        ? `
                                            <div class="formula-name">
                                                ${escapeHTML(item.name)}
                                            </div>
                                          `
                                        : ""
                                }

                                ${
                                    item.formula
                                        ? `
                                            <div class="formula-expression">
                                                ${escapeHTML(item.formula)}
                                            </div>
                                          `
                                        : ""
                                }

                                ${
                                    item.note
                                        ? `
                                            <div class="formula-note">
                                                ${escapeHTML(item.note)}
                                            </div>
                                          `
                                        : ""
                                }

                            </div>
                        `;

                    }
                );


                html += `
                        </div>

                    </div>
                `;

                return;
            }


            /*
             * OBJECT ĐƠN
             */

            if (
                group &&
                typeof group === "object"
            ) {

                html += `
                    <div class="formula-item">

                        ${
                            group.name
                                ? `
                                    <div class="formula-name">
                                        ${escapeHTML(group.name)}
                                    </div>
                                  `
                                : ""
                        }

                        ${
                            group.formula
                                ? `
                                    <div class="formula-expression">
                                        ${escapeHTML(group.formula)}
                                    </div>
                                  `
                                : ""
                        }

                        ${
                            group.note
                                ? `
                                    <div class="formula-note">
                                        ${escapeHTML(group.note)}
                                    </div>
                                  `
                                : ""
                        }

                    </div>
                `;

                return;
            }


            /*
             * STRING
             */

            html += `
                <div class="formula-item">

                    <div class="formula-expression">
                        ${escapeHTML(group)}
                    </div>

                </div>
            `;

        }
    );


    formulas.innerHTML =
        html;
}


/* =========================================================
   RENDER ANSWERS
========================================================= */

function renderAnswers(answerList, correctIndex) {

    if (!answers) {
        return;
    }


    answers.innerHTML = "";


    if (
        !Array.isArray(answerList) ||
        answerList.length === 0
    ) {

        setSectionVisible(
            questionSection,
            false
        );

        return;
    }


    setSectionVisible(
        questionSection,
        true
    );


    answerList.forEach(
        function (answer, index) {

            const option =
                document.createElement("div");

            option.className =
                "answer-option";


            if (
                Number(index) ===
                Number(correctIndex)
            ) {

                option.classList.add(
                    "correct"
                );

            }


            option.innerHTML =
                escapeHTML(
                    answer
                );


            answers.appendChild(
                option
            );

        }
    );

}


/* =========================================================
   RENDER GAME
========================================================= */

function renderGame(lesson) {

    if (
        !gameDescription ||
        !gameButton ||
        !noGame
    ) {
        return;
    }


    if (
        !lesson.game_title &&
        !lesson.game_description &&
        !lesson.game_type
    ) {

        gameDescription.textContent =
            "";

        gameButton.style.display =
            "none";

        noGame.classList.remove(
            "hidden"
        );

        return;
    }


    gameDescription.textContent =
        lesson.game_description ||
        lesson.game_title ||
        "Hãy áp dụng kiến thức vừa học vào thử thách thực tế.";


    if (lesson.game_type) {

        gameButton.style.display =
            "inline-block";

        gameButton.textContent =
            "🚀 Bắt đầu trải nghiệm";


        gameButton.onclick =
            function () {

                window.location.href =
                    `games/${encodeURIComponent(
                        lesson.game_type
                    )}.html?lesson_id=${lesson.id}`;

            };


        noGame.classList.add(
            "hidden"
        );

    } else {

        gameButton.style.display =
            "none";

        noGame.classList.remove(
            "hidden"
        );

    }

}


/* =========================================================
   RENDER LESSON
========================================================= */

function renderLesson(lesson) {

    console.log(
        "Đang render lesson:",
        lesson
    );


    /* =====================================================
       HEADER
    ===================================================== */

    if (lessonIcon) {

        lessonIcon.textContent =
            lesson.icon ||
            "📚";

    }


    if (lessonGrade) {

        lessonGrade.textContent =
            lesson.grade
                ? `Lớp ${lesson.grade}`
                : "";

    }


    if (lessonTitle) {

        lessonTitle.textContent =
            lesson.title ||
            "Bài học";

    }


    if (lessonDescription) {

        lessonDescription.textContent =
            lesson.description ||
            "";

    }


    /* =====================================================
       1. DEFINITION
    ===================================================== */

    if (
        lesson.definition
    ) {

        setText(
            definition,
            lesson.definition
        );

        setSectionVisible(
            definitionSection,
            true
        );

    } else {

        setSectionVisible(
            definitionSection,
            false
        );

    }


    /* =====================================================
       2. CONTEXT
       Chemistry:
       context_title
       context
    ===================================================== */

    if (
        lesson.context ||
        lesson.context_title
    ) {

        setText(
            contextTitle,
            lesson.context_title ||
            "Bối cảnh thực tế"
        );

        setText(
            context,
            lesson.context ||
            ""
        );

        setSectionVisible(
            contextSection,
            true
        );

    } else {

        setSectionVisible(
            contextSection,
            false
        );

    }


    /* =====================================================
       3. THEORY
    ===================================================== */

    if (
        lesson.theory
    ) {

        setText(
            theory,
            lesson.theory
        );

        setSectionVisible(
            theorySection,
            true
        );

    } else {

        setSectionVisible(
            theorySection,
            false
        );

    }


    /* =====================================================
       4. CONCEPT
       Math / Physics cũ
    ===================================================== */

    if (
        lesson.concept
    ) {

        setText(
            concept,
            lesson.concept
        );

        setSectionVisible(
            conceptSection,
            true
        );

    } else {

        setSectionVisible(
            conceptSection,
            false
        );

    }


    /* =====================================================
       5. FORMULA
       Hỗ trợ cả:
       lesson.formulas
       lesson.formula
    ===================================================== */

    renderFormulas(
        lesson.formulas,
        lesson.formula
    );


    /* =====================================================
       6. EXAMPLE
    ===================================================== */

    if (
        lesson.example ||
        lesson.example_answer
    ) {

        setText(
            example,
            lesson.example ||
            ""
        );

        setText(
            exampleAnswer,
            lesson.example_answer ||
            ""
        );

        setSectionVisible(
            exampleSection,
            true
        );

    } else {

        setSectionVisible(
            exampleSection,
            false
        );

    }


    /* =====================================================
       7. QUESTION
    ===================================================== */

    if (
        lesson.question
    ) {

        setText(
            question,
            lesson.question
        );

        renderAnswers(
            lesson.answers,
            lesson.correct
        );

    } else {

        setSectionVisible(
            questionSection,
            false
        );

    }


    /* =====================================================
       8. MEANING
       Math / Physics
    ===================================================== */

    if (
        lesson.meaning
    ) {

        setText(
            meaning,
            lesson.meaning
        );

        setSectionVisible(
            meaningSection,
            true
        );

    } else {

        setSectionVisible(
            meaningSection,
            false
        );

    }


    /* =====================================================
       9. APPLICATION
       Chemistry
    ===================================================== */

    if (
        lesson.application
    ) {

        setText(
            application,
            lesson.application
        );

        setSectionVisible(
            applicationSection,
            true
        );

    } else {

        setSectionVisible(
            applicationSection,
            false
        );

    }


    /* =====================================================
       10. REAL LIFE
       Math / Physics cũ
    ===================================================== */

    if (
        lesson.real_life
    ) {

        setText(
            realLife,
            lesson.real_life
        );

        setSectionVisible(
            realLifeSection,
            true
        );

    } else {

        setSectionVisible(
            realLifeSection,
            false
        );

    }


    /* =====================================================
       11. CHALLENGE
    ===================================================== */

    if (
        lesson.challenge ||
        lesson.challenge_answer
    ) {

        setText(
            challenge,
            lesson.challenge ||
            ""
        );

        setText(
            challengeAnswer,
            lesson.challenge_answer ||
            ""
        );

        setSectionVisible(
            challengeSection,
            true
        );

    } else {

        setSectionVisible(
            challengeSection,
            false
        );

    }


    /* =====================================================
       12. GAME
    ===================================================== */

    renderGame(
        lesson
    );


    /* =====================================================
       FINISH
    ===================================================== */

    finishLoading();


    console.log(
        "Render bài học thành công."
    );

}


/* =========================================================
   LOAD LESSON
========================================================= */

async function loadLesson() {

    console.log(
        "ĐANG LOAD LESSON..."
    );

    console.log(
        "Lesson ID:",
        lessonId
    );

    console.log(
        "Subject:",
        subject
    );

    console.log(
        "Grade:",
        gradeFromUrl
    );


    /* =====================================================
       KIỂM TRA ID
    ===================================================== */

    if (!lessonId) {

        showError(
            "Không tìm thấy ID bài học. Hãy mở bài học từ danh sách bài học."
        );

        return;
    }


    /* =====================================================
       API
    ===================================================== */

    const url =
        `${API_BASE}/content/lessons/${encodeURIComponent(
            lessonId
        )}`;


    console.log(
        "Gọi API:",
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
                `Không thể tải bài học. HTTP ${response.status}`
            );

        }


        const lesson =
            await response.json();


        console.log(
            "LESSON API DATA:",
            lesson
        );


        if (
            !lesson ||
            lesson.id === undefined ||
            lesson.id === null
        ) {

            throw new Error(
                "API trả về bài học nhưng không có ID."
            );

        }


        renderLesson(
            lesson
        );


    } catch (error) {

        console.error(
            "LOAD LESSON ERROR:",
            error
        );


        showError(
            error.message ||
            "Không thể tải bài học."
        );

    }

}


/* =========================================================
   START
========================================================= */

loadLesson();