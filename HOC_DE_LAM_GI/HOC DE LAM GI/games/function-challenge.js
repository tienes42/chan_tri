const API_BASE = "http://127.0.0.1:8000/api";

const GAME_ID = 1;
const USER_ID = 1;

let sessionId = null;

let score = 0;
let questionIndex = 0;

const questions = [
{
a: 2,
b: 3,
y: 7,
options: [-2, 0, 1, 2, 4],
answer: 2
},
{
a: 3,
b: 1,
y: 10,
options: [1, 2, 3, 4, 5],
answer: 3
},
{
a: 2,
b: 5,
y: 11,
options: [1, 2, 3, 4, 5],
answer: 3
},
{
a: 4,
b: 2,
y: 14,
options: [1, 2, 3, 4, 5],
answer: 3
},
{
a: 5,
b: 0,
y: 20,
options: [2, 3, 4, 5, 6],
answer: 4
}
];

let currentQuestion = null;
let questionStartTime = null;

// =========================
// TẠO SESSION
// =========================

async function createSession() {


try {

    const response = await fetch(
        `${API_BASE}/games/sessions`,
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                user_id: USER_ID,
                game_id: GAME_ID
            })
        }
    );

    if (!response.ok) {
        throw new Error("Không thể tạo game session");
    }

    const data = await response.json();

    sessionId = data.id;

    console.log("Game session:", sessionId);

    loadQuestion();

} catch (error) {

    console.error(error);

    document.getElementById("message").textContent =
        "Không thể kết nối với backend.";

}


}

// =========================
// GHI EVENT
// =========================

async function recordEvent(action, eventData = {}) {

if (!sessionId) return;

try {

    await fetch(
        `${API_BASE}/games/sessions/${sessionId}/events`,
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                action: action,
                event_data: JSON.stringify(eventData)
            })
        }
    );

} catch (error) {

    console.error("Không ghi được event:", error);

}


}

// =========================
// LOAD CÂU HỎI
// =========================

function loadQuestion() {


if (questionIndex >= questions.length) {

    finishGame();

    return;
}

currentQuestion = questions[questionIndex];

questionStartTime = Date.now();

document.getElementById("functionText").textContent =
    `y = ${currentQuestion.a}x + ${currentQuestion.b}`;

document.getElementById("targetY").textContent =
    currentQuestion.y;

document.getElementById("questionNumber").textContent =
    questionIndex + 1;

document.getElementById("message").textContent = "";

const optionsContainer =
    document.getElementById("options");

optionsContainer.innerHTML = "";

currentQuestion.options.forEach(x => {

    const button = document.createElement("button");

    button.className = "option";

    button.textContent = `x = ${x}`;

    button.onclick = () => chooseAnswer(x, button);

    optionsContainer.appendChild(button);

});

recordEvent(
    "change_parameter",
    {
        question: questionIndex + 1,
        a: currentQuestion.a,
        b: currentQuestion.b,
        target_y: currentQuestion.y
    }
);


}

// =========================
// CHỌN ĐÁP ÁN
// =========================

function chooseAnswer(x, button) {


const elapsed =
    Date.now() - questionStartTime;

const expected =
    currentQuestion.answer;

const buttons =
    document.querySelectorAll(".option");

buttons.forEach(btn => {
    btn.disabled = true;
});

// =========================
// ĐÚNG
// =========================

if (x === expected) {

    score += 20;

    document.getElementById("score").textContent =
        score;

    document.getElementById("message").textContent =
        "✅ Chính xác!";

    recordEvent(
        "success",
        {
            question: questionIndex + 1,
            selected_x: x,
            correct_x: expected,
            time_ms: elapsed
        }
    );

}

// =========================
// SAI
// =========================

else {

    document.getElementById("message").textContent =
        "❌ Chưa đúng. Hãy thử lại!";

    recordEvent(
        "wrong_answer",
        {
            question: questionIndex + 1,
            selected_x: x,
            correct_x: expected,
            time_ms: elapsed
        }
    );

    setTimeout(() => {

        buttons.forEach(btn => {
            btn.disabled = false;
        });

        recordEvent(
            "retry",
            {
                question: questionIndex + 1
            }
        );

    }, 700);

    return;
}

// Sang câu tiếp theo
setTimeout(() => {

    questionIndex++;

    loadQuestion();

}, 900);


}

// =========================
// KẾT THÚC GAME
// =========================

async function finishGame() {


document.getElementById("gameCard").style.display =
    "none";

document.getElementById("finishCard").style.display =
    "block";

document.getElementById("finalScore").textContent =
    score;

let message = "";

if (score === 100) {
    message = "Xuất sắc! Bạn nắm rất chắc cách tính hàm số.";
}
else if (score >= 60) {
    message = "Khá tốt! Bạn đã hiểu được cách tìm x.";
}
else {
    message = "Hãy luyện tập thêm về hàm số.";
}

document.getElementById("finishMessage").textContent =
    message;

if (!sessionId) return;

try {

    await fetch(
        `${API_BASE}/games/sessions/${sessionId}/finish?score=${score}`,
        {
            method: "POST"
        }
    );

    console.log("Game finished:", score);

} catch (error) {

    console.error(
        "Không thể kết thúc session:",
        error
    );

}


}

// =========================
// QUAY LẠI
// =========================

function goBack() {


window.location.href =
    "../lesson.html?subject=math&grade=10&topic=ham-so";


}

// =========================
// START
// =========================

createSession();
