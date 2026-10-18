/* =========================================================
   MATH PAGE
========================================================= */


/* =========================
   BACK TO INDEX
========================= */

const backButton =
    document.getElementById("backButton");

backButton.addEventListener("click", function () {

    window.location.href = "index.html";

});


/* =========================
   CLASS CARDS
========================= */

const classCards =
    document.querySelectorAll(".class-card");


const mathPopup =
    document.getElementById("mathPopup");


const mathPopupClose =
    document.getElementById("mathPopupClose");


const mathPopupIcon =
    document.getElementById("mathPopupIcon");


const mathPopupTitle =
    document.getElementById("mathPopupTitle");


const mathPopupText =
    document.getElementById("mathPopupText");


const mathPopupButton =
    document.getElementById("mathPopupButton");


let selectedGrade = null;


/* =========================
   CLICK CLASS
========================= */

classCards.forEach(function (card) {

    card.addEventListener("click", function () {

        selectedGrade =
            card.dataset.grade;


        mathPopupIcon.textContent = "📚";


        mathPopupTitle.textContent =
            "Toán lớp " + selectedGrade;


        mathPopupText.textContent =
            "Bạn đã chọn chương trình Toán lớp "
            + selectedGrade
            + ". Hãy sẵn sàng khám phá kiến thức!";


        mathPopupButton.textContent =
            "Khám phá";


        mathPopup.classList.add("show");

    });

});


/* =========================
   CLOSE POPUP
========================= */

mathPopupClose.addEventListener(
    "click",
    function () {

        mathPopup.classList.remove("show");

    }
);


/* =========================
   CLICK OUTSIDE
========================= */

mathPopup.addEventListener(
    "click",
    function (event) {

        if (event.target === mathPopup) {

            mathPopup.classList.remove("show");

        }

    }
);


/* =========================
   START LEARNING
========================= */

mathPopupButton.addEventListener(
    "click",
    function () {

        if (selectedGrade !== null) {

            window.location.href =
                "math-grade.html?grade="
                + selectedGrade;

        }

    }
);

/* =========================
   QUICK TOOLS
========================= */

const calculatorButton =
    document.getElementById(
        "calculatorButton"
    );


const challengeButton =
    document.getElementById(
        "challengeButton"
    );


const progressButton =
    document.getElementById(
        "progressButton"
    );


calculatorButton.addEventListener(
    "click",
    function () {

        alert(
            "Máy tính Toán học sẽ được xây dựng ở bước tiếp theo."
        );

    }
);


challengeButton.addEventListener(
    "click",
    function () {

        alert(
            "Hệ thống thử thách sẽ được xây dựng ở phần NHIỆM VỤ."
        );

    }
);


progressButton.addEventListener(
    "click",
    function () {

        alert(
            "Hệ thống phân tích tiến trình sẽ được xây dựng ở phần PHÂN TÍCH."
        );

    }
);