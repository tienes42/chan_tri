/* =========================================================
   CHEMISTRY PAGE
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


const chemistryPopup =
    document.getElementById("mathPopup");


const chemistryPopupClose =
    document.getElementById("mathPopupClose");


const chemistryPopupIcon =
    document.getElementById("mathPopupIcon");


const chemistryPopupTitle =
    document.getElementById("mathPopupTitle");


const chemistryPopupText =
    document.getElementById("mathPopupText");


const chemistryPopupButton =
    document.getElementById("mathPopupButton");


let selectedGrade = null;



/* =========================
   CLICK CLASS
========================= */

classCards.forEach(function (card) {

    card.addEventListener("click", function () {


        selectedGrade =
            card.dataset.grade;


        chemistryPopupIcon.textContent =
            "🧪";


        chemistryPopupTitle.textContent =
            "Hóa học lớp " + selectedGrade;


        chemistryPopupText.textContent =
            "Bạn đã chọn chương trình Hóa học lớp "
            + selectedGrade
            + ". Hãy sẵn sàng khám phá thế giới của nguyên tử, phân tử và các phản ứng hóa học!";


        chemistryPopupButton.textContent =
            "Khám phá";


        chemistryPopup.classList.add("show");

    });

});



/* =========================
   CLOSE POPUP
========================= */

chemistryPopupClose.addEventListener(
    "click",
    function () {

        chemistryPopup.classList.remove("show");

    }
);



/* =========================
   CLICK OUTSIDE
========================= */

chemistryPopup.addEventListener(
    "click",
    function (event) {

        if (event.target === chemistryPopup) {

            chemistryPopup.classList.remove("show");

        }

    }
);



/* =========================
   START LEARNING
========================= */

chemistryPopupButton.addEventListener(
    "click",
    function () {


        if (selectedGrade !== null) {


            /*
                Sau này sẽ chuyển tới:

                chemistry-knowledge.html?grade=10
            */


            window.location.href =
                "chemistry-knowledge.html?grade="
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



/* =========================
   CHEMISTRY TOOLS
========================= */

calculatorButton.addEventListener(
    "click",
    function () {

        alert(
            "Công cụ Hóa học sẽ được xây dựng ở bước tiếp theo."
        );

    }
);



/* =========================
   CHALLENGE
========================= */

challengeButton.addEventListener(
    "click",
    function () {

        alert(
            "Hệ thống thử thách Hóa học sẽ được xây dựng ở phần NHIỆM VỤ."
        );

    }
);



/* =========================
   PROGRESS
========================= */

progressButton.addEventListener(
    "click",
    function () {

        alert(
            "Hệ thống phân tích tiến trình sẽ được xây dựng ở phần PHÂN TÍCH."
        );

    }
);
