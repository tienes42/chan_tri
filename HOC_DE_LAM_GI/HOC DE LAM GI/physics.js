/* =========================================================
   PHYSICS PAGE
   Vật lý → Chọn lớp → Danh sách bài học
========================================================= */


/* =========================
   BACK TO INDEX
========================= */

const backButton = document.getElementById("backButton");

if (backButton) {
    backButton.addEventListener("click", function () {
        window.location.href = "index.html";
    });
}


/* =========================
   CLASS CARDS
========================= */

const classCards = document.querySelectorAll(".class-card");


/* =========================
   POPUP
========================= */

const physicsPopup = document.getElementById("mathPopup");
const physicsPopupClose = document.getElementById("mathPopupClose");
const physicsPopupIcon = document.getElementById("mathPopupIcon");
const physicsPopupTitle = document.getElementById("mathPopupTitle");
const physicsPopupText = document.getElementById("mathPopupText");
const physicsPopupButton = document.getElementById("mathPopupButton");

let selectedGrade = null;


/* =========================
   CLICK CLASS
========================= */

classCards.forEach(function (card) {

    card.addEventListener("click", function () {

        selectedGrade = card.dataset.grade;

        console.log(
            "Đã chọn Vật lý lớp:",
            selectedGrade
        );

        if (physicsPopupIcon) {
            physicsPopupIcon.textContent = "⚡";
        }

        if (physicsPopupTitle) {
            physicsPopupTitle.textContent =
                "Vật lý lớp " + selectedGrade;
        }

        if (physicsPopupText) {
            physicsPopupText.textContent =
                "Bạn đã chọn chương trình Vật lý lớp "
                + selectedGrade
                + ". Hãy bắt đầu khám phá những quy luật của thế giới!";
        }

        if (physicsPopupButton) {
            physicsPopupButton.textContent = "Khám phá";
        }

        if (physicsPopup) {
            physicsPopup.classList.add("show");
        }

    });

});


/* =========================
   CLOSE POPUP
========================= */

if (physicsPopupClose) {

    physicsPopupClose.addEventListener(
        "click",
        function () {

            physicsPopup.classList.remove("show");

        }
    );

}


/* =========================
   CLICK OUTSIDE POPUP
========================= */

if (physicsPopup) {

    physicsPopup.addEventListener(
        "click",
        function (event) {

            if (event.target === physicsPopup) {

                physicsPopup.classList.remove("show");

            }

        }
    );

}


/* =========================
   START LEARNING
========================= */

if (physicsPopupButton) {

    physicsPopupButton.addEventListener(
    "click",
    function () {

        if (selectedGrade === null) {
            return;
        }

        window.location.href =
            "physics-grade.html?grade=" +
            encodeURIComponent(selectedGrade);

    }
);

}


/* =========================
   QUICK TOOLS
========================= */

const calculatorButton =
    document.getElementById("calculatorButton");

const challengeButton =
    document.getElementById("challengeButton");

const progressButton =
    document.getElementById("progressButton");


/* =========================
   PHYSICS TOOLS
========================= */

if (calculatorButton) {

    calculatorButton.addEventListener(
        "click",
        function () {

            alert(
                "Công cụ Vật lý sẽ được xây dựng ở bước tiếp theo."
            );

        }
    );

}


if (challengeButton) {

    challengeButton.addEventListener(
        "click",
        function () {

            alert(
                "Hệ thống thử thách Vật lý sẽ được xây dựng ở phần NHIỆM VỤ."
            );

        }
    );

}


if (progressButton) {

    progressButton.addEventListener(
        "click",
        function () {

            alert(
                "Hệ thống phân tích tiến trình sẽ được xây dựng ở phần PHÂN TÍCH."
            );

        }
    );

}