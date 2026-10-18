/* =========================================================
   GAME 01 - ÔNG CHỦ TẬP SỰ
   HỌC ĐỂ LÀM GÌ

   Toán 10 - Hàm số
   Chủ đề:
   Giá bán -> Nhu cầu -> Doanh thu -> Lợi nhuận

   Có:
   - 5 ngày kinh doanh
   - Sự kiện thị trường
   - Quyết định đặc biệt
   - Giá bán
   - Nhập hàng
   - Quảng cáo
   - Đối thủ cạnh tranh
   - Khách hàng animation
   - Điểm
   - Achievement
   - Ghi dữ liệu hành vi về backend
========================================================= */


/* =========================================================
   CONFIG
========================================================= */

const API_BASE =
    "http://127.0.0.1:8000/api";

const GAME_ID = 1;

const params =
    new URLSearchParams(
        window.location.search
    );

const LESSON_ID =
    params.get("lesson_id") ||
    params.get("lessonId") ||
    null;

const USER_ID =
    Number(
        localStorage.getItem("user_id")
    ) || 1;


/* =========================================================
   GAME STATE
========================================================= */

const state = {

    day: 1,

    maxDays: 5,

    money: 2000000,

    startingMoney: 2000000,

    stock: 40,

    price: 20,

    restock: 0,

    totalProfit: 0,

    totalRevenue: 0,

    totalSold: 0,

    totalCustomers: 0,

    score: 0,

    noStockout: true,

    adaptiveDecisions: 0,

    decisions: [],

    dayStartTime: Date.now(),

    sessionId: null,

    currentEvent: null,

    dayRunning: false,

    gameFinished: false,

    specialChoice: null,

    demandMultiplier: 1,

    dailySpecialCost: 0

};


/* =========================================================
   EVENTS
========================================================= */

const EVENTS = [

    {
        id: "sunny",

        icon: "☀️",

        title: "Trời nắng nóng!",

        description:
            "Khách hàng có xu hướng mua nước nhiều hơn.",

        baseDemand: 95,

        sensitivity: 3.2
    },

    {
        id: "normal",

        icon: "🌤️",

        title: "Một ngày bình thường",

        description:
            "Lượng khách ở mức ổn định.",

        baseDemand: 80,

        sensitivity: 3
    },

    {
        id: "competitor",

        icon: "🏪",

        title: "Đối thủ giảm giá!",

        description:
            "Cửa hàng bên cạnh đang bán rẻ hơn. Bạn phải cân nhắc chiến lược.",

        baseDemand: 90,

        sensitivity: 3.7
    },

    {
        id: "rain",

        icon: "🌧️",

        title: "Trời mưa",

        description:
            "Ít khách đi lại hơn, nhu cầu giảm.",

        baseDemand: 60,

        sensitivity: 2.6
    },

    {
        id: "viral",

        icon: "🔥",

        title: "Sản phẩm đang hot!",

        description:
            "Mọi người đang săn sản phẩm của bạn.",

        baseDemand: 110,

        sensitivity: 3.5
    }

];


/* =========================================================
   DOM
========================================================= */

const dayDisplay =
    document.getElementById(
        "dayDisplay"
    );

const moneyDisplay =
    document.getElementById(
        "moneyDisplay"
    );

const stockDisplay =
    document.getElementById(
        "stockDisplay"
    );

const profitDisplay =
    document.getElementById(
        "profitDisplay"
    );

const priceSlider =
    document.getElementById(
        "priceSlider"
    );

const priceValue =
    document.getElementById(
        "priceValue"
    );

const restockValue =
    document.getElementById(
        "restockValue"
    );

const restockDisplay =
    document.getElementById(
        "restockDisplay"
    );

const restockMinus =
    document.getElementById(
        "restockMinus"
    );

const restockPlus =
    document.getElementById(
        "restockPlus"
    );

const openShopButton =
    document.getElementById(
        "openShopButton"
    );

const eventIcon =
    document.getElementById(
        "eventIcon"
    );

const eventTitle =
    document.getElementById(
        "eventTitle"
    );

const eventDescription =
    document.getElementById(
        "eventDescription"
    );

const activityFeed =
    document.getElementById(
        "activityFeed"
    );

const customersLayer =
    document.getElementById(
        "customersLayer"
    );

const missionProgress =
    document.getElementById(
        "missionProgress"
    );

const missionText =
    document.getElementById(
        "missionText"
    );


/* =========================================================
   RESULT DOM
========================================================= */

const resultOverlay =
    document.getElementById(
        "resultOverlay"
    );

const resultIcon =
    document.getElementById(
        "resultIcon"
    );

const resultTitle =
    document.getElementById(
        "resultTitle"
    );

const resultMessage =
    document.getElementById(
        "resultMessage"
    );

const resultDemand =
    document.getElementById(
        "resultDemand"
    );

const resultSold =
    document.getElementById(
        "resultSold"
    );

const resultRevenue =
    document.getElementById(
        "resultRevenue"
    );

const resultDailyProfit =
    document.getElementById(
        "resultDailyProfit"
    );

const nextDayButton =
    document.getElementById(
        "nextDayButton"
    );


/* =========================================================
   FINAL DOM
========================================================= */

const finalOverlay =
    document.getElementById(
        "finalOverlay"
    );

const finalProfit =
    document.getElementById(
        "finalProfit"
    );

const finalCustomers =
    document.getElementById(
        "finalCustomers"
    );

const finalSold =
    document.getElementById(
        "finalSold"
    );

const finalScore =
    document.getElementById(
        "finalScore"
    );

const finalMoney =
    document.getElementById(
        "finalMoney"
    );

const achievementProfit =
    document.getElementById(
        "achievementProfit"
    );

const achievementStock =
    document.getElementById(
        "achievementStock"
    );

const achievementStrategy =
    document.getElementById(
        "achievementStrategy"
    );


/* =========================================================
   FORMAT MONEY
========================================================= */

function money(value) {

    return (
        Math.round(value)
            .toLocaleString("vi-VN")
        + "đ"
    );

}


/* =========================================================
   UPDATE HUD
========================================================= */

function updateHUD() {

    dayDisplay.textContent =
        `${state.day} / ${state.maxDays}`;

    moneyDisplay.textContent =
        money(state.money);

    stockDisplay.textContent =
        state.stock;

    profitDisplay.textContent =
        money(state.totalProfit);


    const progress =
        Math.max(
            0,
            Math.min(
                100,
                (
                    state.totalProfit /
                    500000
                ) * 100
            )
        );


    missionProgress.style.width =
        progress + "%";


    missionText.textContent =
        `${money(
            Math.max(
                0,
                state.totalProfit
            )
        )} / 500.000đ`;

}


/* =========================================================
   ACTIVITY FEED
========================================================= */

function addFeed(message) {

    if (!activityFeed) {
        return;
    }


    const item =
        document.createElement("div");

    item.className =
        "feed-item";


    const time =
        new Date().toLocaleTimeString(
            "vi-VN",
            {
                hour: "2-digit",
                minute: "2-digit"
            }
        );


    item.innerHTML =
        `<span class="feed-time">${time}</span>${message}`;


    activityFeed.prepend(
        item
    );


    while (
        activityFeed.children.length > 15
    ) {

        activityFeed.removeChild(
            activityFeed.lastChild
        );

    }

}


/* =========================================================
   SELECT EVENT
========================================================= */

function selectEvent() {

    let event;


    /*
       Ngày 1:
       Cho người chơi làm quen.
    */

    if (state.day === 1) {

        event = EVENTS[1];

    }


    /*
       Ngày 2:
       Cho thấy tác động của thời tiết.
    */

    else if (state.day === 2) {

        event = EVENTS[0];

    }


    /*
       Ngày 3-5:
       Random các sự kiện.
    */

    else {

        const available =
            EVENTS.slice(1);

        event =
            available[
                Math.floor(
                    Math.random() *
                    available.length
                )
            ];

    }


    state.currentEvent =
        event;


    state.specialChoice =
        null;

    state.demandMultiplier =
        1;

    state.dailySpecialCost =
        0;


    eventIcon.textContent =
        event.icon;

    eventTitle.textContent =
        event.title;

    eventDescription.textContent =
        event.description;


    renderEventChoices();

}


/* =========================================================
   RENDER EVENT CHOICES
========================================================= */

function renderEventChoices() {

    let choiceBox =
        document.getElementById(
            "eventChoices"
        );


    /*
       Nếu HTML chưa có eventChoices
       thì tự tạo.
    */

    if (!choiceBox) {

        choiceBox =
            document.createElement("div");

        choiceBox.id =
            "eventChoices";

        choiceBox.style.marginTop =
            "10px";


        if (
            eventDescription &&
            eventDescription.parentElement
        ) {

            eventDescription.parentElement.appendChild(
                choiceBox
            );

        }

    }


    if (!choiceBox) {
        return;
    }


    choiceBox.innerHTML = "";


    const event =
        state.currentEvent;


    if (!event) {
        return;
    }


    /* =========================
       NORMAL
    ========================= */

    if (
        event.id === "normal"
    ) {

        addChoiceButton(
            choiceBox,
            "📢 Quảng cáo nhẹ (-30.000đ)",
            "advertise"
        );

        addChoiceButton(
            choiceBox,
            "💰 Không quảng cáo",
            "normal"
        );

    }


    /* =========================
       SUNNY
    ========================= */

    else if (
        event.id === "sunny"
    ) {

        addChoiceButton(
            choiceBox,
            "🧊 Chuẩn bị thêm hàng (-20.000đ)",
            "extra_stock"
        );

        addChoiceButton(
            choiceBox,
            "💰 Giữ nguyên kế hoạch",
            "normal"
        );

    }


    /* =========================
       COMPETITOR
    ========================= */

    else if (
        event.id === "competitor"
    ) {

        addChoiceButton(
            choiceBox,
            "📉 Giảm giá 2.000đ",
            "lower_price"
        );

        addChoiceButton(
            choiceBox,
            "🧠 Giữ giá",
            "keep_price"
        );

    }


    /* =========================
       RAIN
    ========================= */

    else if (
        event.id === "rain"
    ) {

        addChoiceButton(
            choiceBox,
            "📢 Quảng cáo online (-40.000đ)",
            "advertise"
        );

        addChoiceButton(
            choiceBox,
            "☂️ Chấp nhận ít khách",
            "normal"
        );

    }


    /* =========================
       VIRAL
    ========================= */

    else if (
        event.id === "viral"
    ) {

        addChoiceButton(
            choiceBox,
            "🔥 Tận dụng cơ hội",
            "viral_push"
        );

        addChoiceButton(
            choiceBox,
            "😐 Kinh doanh bình thường",
            "normal"
        );

    }

}


/* =========================================================
   CREATE CHOICE BUTTON
========================================================= */

function addChoiceButton(
    container,
    text,
    choice
) {

    const button =
        document.createElement("button");


    button.type =
        "button";


    button.textContent =
        text;


    button.style.marginRight =
        "8px";

    button.style.marginTop =
        "6px";

    button.style.padding =
        "8px 12px";

    button.style.borderRadius =
        "9px";

    button.style.border =
        "1px solid #d7bd8c";

    button.style.background =
        "#fffaf0";

    button.style.cursor =
        "pointer";


    button.addEventListener(
        "click",
        function () {

            chooseSpecialEvent(
                choice,
                button,
                container
            );

        }
    );


    container.appendChild(
        button
    );

}


/* =========================================================
   SPECIAL EVENT DECISION
========================================================= */

async function chooseSpecialEvent(
    choice,
    selectedButton,
    container
) {

    if (
        state.dayRunning
    ) {
        return;
    }


    /*
       Không cho chọn nhiều lần.
    */

    const buttons =
        container.querySelectorAll(
            "button"
        );


    buttons.forEach(
        button => {

            button.disabled =
                true;

        }
    );


    state.specialChoice =
        choice;

    state.demandMultiplier =
        1;

    state.dailySpecialCost =
        0;


    const moneyBefore =
        state.money;


    /* =====================================================
       QUẢNG CÁO
    ===================================================== */

    if (
        choice === "advertise"
    ) {

        const cost =
            state.currentEvent.id === "rain"
                ? 40000
                : 30000;


        if (
            state.money >= cost
        ) {

            state.money -=
                cost;

            state.dailySpecialCost +=
                cost;

            state.demandMultiplier =
                1.20;


            addFeed(
                `📢 Quảng cáo thành công! Nhu cầu dự kiến tăng 20%. (-${money(cost)})`
            );

        }

        else {

            addFeed(
                "💸 Bạn không đủ tiền chạy quảng cáo."
            );

            state.specialChoice =
                "normal";

        }

    }


    /* =====================================================
       EXTRA STOCK
    ===================================================== */

    else if (
        choice === "extra_stock"
    ) {

        const cost = 20000;


        if (
            state.money >= cost
        ) {

            state.money -=
                cost;

            state.stock +=
                5;

            state.dailySpecialCost +=
                cost;


            addFeed(
                "🧊 Bạn chuẩn bị thêm 5 sản phẩm cho ngày nắng."
            );

        }

        else {

            addFeed(
                "💸 Không đủ tiền chuẩn bị hàng thêm."
            );

            state.specialChoice =
                "normal";

        }

    }


    /* =====================================================
       LOWER PRICE
    ===================================================== */

    else if (
        choice === "lower_price"
    ) {

        const oldPrice =
            state.price;


        state.price =
            Math.max(
                10,
                state.price - 2
            );


        priceSlider.value =
            state.price;


        updatePrice();


        state.demandMultiplier =
            1.08;


        addFeed(
            `📉 Bạn giảm giá từ ${money(
                oldPrice * 1000
            )} xuống ${money(
                state.price * 1000
            )}.`
        );

    }


    /* =====================================================
       KEEP PRICE
    ===================================================== */

    else if (
        choice === "keep_price"
    ) {

        state.demandMultiplier =
            0.94;


        addFeed(
            "🧠 Bạn giữ giá và chấp nhận cạnh tranh."
        );

    }


    /* =====================================================
       VIRAL
    ===================================================== */

    else if (
        choice === "viral_push"
    ) {

        state.demandMultiplier =
            1.25;


        addFeed(
            "🔥 Bạn tận dụng cơn sốt sản phẩm! Nhu cầu tăng mạnh."
        );

    }


    /*
       Quyết định bình thường
    */

    else if (
        choice === "normal"
    ) {

        state.demandMultiplier =
            1;


        addFeed(
            "💰 Bạn giữ nguyên chiến lược."
        );

    }


    await recordEvent(
        "special_event_decision",
        {

            day:
                state.day,

            event:
                state.currentEvent.id,

            choice:
                state.specialChoice,

            price:
                state.price,

            money_before:
                moneyBefore,

            money_after:
                state.money,

            special_cost:
                state.dailySpecialCost,

            demand_multiplier:
                state.demandMultiplier

        }
    );


    updateHUD();


    selectedButton.style.background =
        "#dff2e3";

    selectedButton.style.borderColor =
        "#64a96d";

}


/* =========================================================
   PRICE UI
========================================================= */

function updatePrice() {

    state.price =
        Number(
            priceSlider.value
        );


    priceValue.textContent =
        money(
            state.price * 1000
        );

}


/* =========================================================
   RESTOCK UI
========================================================= */

function updateRestockDisplay() {

    restockValue.textContent =
        state.restock;


    restockDisplay.textContent =
        `${state.restock} sản phẩm`;

}


/* =========================================================
   PRICE SLIDER
========================================================= */

priceSlider.addEventListener(
    "input",
    function () {

        if (
            state.dayRunning
        ) {
            return;
        }


        updatePrice();

    }
);


/* =========================================================
   RESTOCK -
========================================================= */

restockMinus.addEventListener(
    "click",
    function () {

        if (
            state.dayRunning
        ) {
            return;
        }


        if (
            state.restock > 0
        ) {

            state.restock--;

            updateRestockDisplay();

        }

    }
);


/* =========================================================
   RESTOCK +
========================================================= */

restockPlus.addEventListener(
    "click",
    function () {

        if (
            state.dayRunning
        ) {
            return;
        }


        const nextCost =
            8000;


        if (
            state.money <
            nextCost
        ) {

            addFeed(
                "💸 Không đủ tiền để nhập thêm hàng."
            );

            return;

        }


        if (
            state.restock >= 60
        ) {

            addFeed(
                "📦 Xe chở hàng hôm nay chỉ cung cấp tối đa 60 sản phẩm."
            );

            return;

        }


        state.restock++;

        updateRestockDisplay();

    }
);


/* =========================================================
   API - CREATE SESSION
========================================================= */

async function createGameSession() {

    try {

        const response =
            await fetch(
                `${API_BASE}/games/sessions`,
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({

                        game_id:
                            GAME_ID,

                        user_id:
                            USER_ID

                    })

                }
            );


        if (
            !response.ok
        ) {

            const errorText =
                await response.text();


            throw new Error(
                `HTTP ${response.status}: ${errorText}`
            );

        }


        const data =
            await response.json();


        state.sessionId =
            data.id ||
            data.session_id;


        console.log(
            "Game session:",
            state.sessionId
        );


        addFeed(
            "🎮 Đã kết nối phiên chơi."
        );


    } catch (error) {

        console.warn(
            "Không tạo được session:",
            error
        );


        addFeed(
            "⚠️ Không kết nối được máy chủ. Game vẫn có thể chơi offline."
        );

    }

}


/* =========================================================
   API - RECORD EVENT
========================================================= */

async function recordEvent(
    action,
    eventData
) {

    if (
        !state.sessionId
    ) {
        return;
    }


    try {

        const response =
            await fetch(
                `${API_BASE}/games/sessions/${state.sessionId}/events`,
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({

                        action:
                            action,

                        event_data:
                            JSON.stringify(
                                eventData
                            )

                    })

                }
            );


        if (
            !response.ok
        ) {

            const errorText =
                await response.text();


            console.warn(
                "API event lỗi:",
                response.status,
                errorText
            );

        }

    } catch (error) {

        console.warn(
            "Không ghi được event:",
            error
        );

    }

}


/* =========================================================
   API - FINISH GAME
========================================================= */

async function finishGame() {

    if (
        !state.sessionId
    ) {
        return;
    }


    try {

        const response =
            await fetch(
                `${API_BASE}/games/sessions/${state.sessionId}/finish?score=${state.score}`,
                {
                    method: "POST"
                }
            );


        if (
            !response.ok
        ) {

            console.warn(
                "Finish game lỗi:",
                response.status
            );

        }

    } catch (error) {

        console.warn(
            "Không thể kết thúc session:",
            error
        );

    }

}


/* =========================================================
   OPEN SHOP
========================================================= */

openShopButton.addEventListener(
    "click",
    openShop
);


/* =========================================================
   OPEN SHOP FUNCTION
========================================================= */

async function openShop() {

    if (
        state.dayRunning
    ) {
        return;
    }


    state.dayRunning =
        true;


    openShopButton.disabled =
        true;

    priceSlider.disabled =
        true;

    restockMinus.disabled =
        true;

    restockPlus.disabled =
        true;


    const decisionTime =
        Date.now() -
        state.dayStartTime;


    /*
       Chi phí nhập hàng.
    */

    const restockCost =
        state.restock * 8000;


    /*
       Kiểm tra tiền.
    */

    if (
        restockCost >
        state.money
    ) {

        addFeed(
            "❌ Bạn không đủ tiền để nhập số hàng này."
        );


        state.dayRunning =
            false;


        openShopButton.disabled =
            false;

        priceSlider.disabled =
            false;

        restockMinus.disabled =
            false;

        restockPlus.disabled =
            false;


        return;

    }


    const moneyBeforeBusiness =
        state.money;


    /*
       Trừ tiền nhập hàng.
    */

    state.money -=
        restockCost;


    /*
       Thêm hàng vào kho.
    */

    state.stock +=
        state.restock;


    /*
       Ghi quyết định kinh doanh.
    */

    const decision = {

        day:
            state.day,

        event:
            state.currentEvent.id,

        price:
            state.price,

        restock:
            state.restock,

        special_choice:
            state.specialChoice,

        decision_time_ms:
            decisionTime

    };


    state.decisions.push(
        decision
    );


    await recordEvent(
        "business_decision",
        decision
    );


    addFeed(
        `💰 Bạn nhập ${state.restock} sản phẩm, tốn ${money(
            restockCost
        )}.`
    );


    /*
       =====================================================
       HÀM SỐ NHU CẦU
       
       Q = a - bP

       P = giá bán
       Q = nhu cầu
       =====================================================
    */

    const event =
        state.currentEvent;


    let demand =
        event.baseDemand -
        event.sensitivity *
        state.price;


    /*
       Tác động từ lựa chọn đặc biệt.
    */

    demand =
        demand *
        state.demandMultiplier;


    /*
       Nhu cầu không âm.
    */

    demand =
        Math.max(
            0,
            Math.round(
                demand
            )
        );


    /*
       Nếu giá quá cao:
       khách giảm mạnh.
    */

    if (
        state.price >= 27
    ) {

        demand =
            Math.round(
                demand * 0.75
            );

    }


    /*
       Nếu giá rất thấp:
       nhu cầu tăng.
    */

    if (
        state.price <= 13
    ) {

        demand =
            Math.round(
                demand * 1.08
            );

    }


    /*
       Số lượng bán không vượt kho.
    */

    const sold =
        Math.min(
            demand,
            state.stock
        );


    /*
       Kiểm tra hết hàng.
    */

    if (
        sold === state.stock &&
        demand > state.stock
    ) {

        state.noStockout =
            false;


        addFeed(
            "⚠️ Cửa hàng hết hàng! Bạn đã bỏ lỡ khách."
        );

    }


    /*
       Doanh thu.
    */

    const revenue =
        sold *
        state.price *
        1000;


    /*
       Lợi nhuận ngày.
       
       Doanh thu
       - nhập hàng
       
       Chi phí quảng cáo / chiến lược
       đã được trừ trực tiếp khỏi tiền.
    */

    const dailyProfit =
        revenue -
        restockCost;


    /*
       Cập nhật tiền.
    */

    state.money +=
        revenue;


    /*
       Cập nhật thống kê.
    */

    state.totalRevenue +=
        revenue;


    state.totalProfit +=
        dailyProfit;


    state.totalSold +=
        sold;


    state.totalCustomers +=
        sold;


    /*
       =====================================================
       CHẤM ĐIỂM
       =====================================================
    */

    let dayScore = 0;


    /*
       Có lãi.
    */

    if (
        dailyProfit > 0
    ) {

        dayScore +=
            100;

    }


    /*
       Giá hợp lý.
    */

    if (
        state.price >= 17 &&
        state.price <= 23
    ) {

        dayScore +=
            50;

    }


    /*
       Đáp ứng đủ nhu cầu.
    */

    if (
        sold === demand
    ) {

        dayScore +=
            50;

    }


    /*
       Giá quá cực đoan.
    */

    if (
        state.price <= 13 ||
        state.price >= 27
    ) {

        dayScore -=
            20;

    }


    /*
       Lợi nhuận cao.
    */

    if (
        dailyProfit >= 150000
    ) {

        dayScore +=
            50;

    }


    state.score +=
        Math.max(
            0,
            dayScore
        );


    /*
       =====================================================
       KHẢ NĂNG THÍCH NGHI
       =====================================================
    */

    if (
        state.day > 1 &&
        state.decisions.length >= 2
    ) {

        const previous =
            state.decisions[
                state.decisions.length - 2
            ];


        if (
            previous.event !==
                decision.event &&
            previous.price !==
                decision.price
        ) {

            state.adaptiveDecisions++;

        }

    }


    /*
       =====================================================
       GHI KẾT QUẢ NGÀY
       =====================================================
    */

    await recordEvent(
        "day_result",
        {

            day:
                state.day,

            event:
                event.id,

            price:
                state.price,

            restock:
                state.restock,

            special_choice:
                state.specialChoice,

            demand_multiplier:
                state.demandMultiplier,

            demand:
                demand,

            sold:
                sold,

            stock_remaining:
                state.stock - sold,

            revenue:
                revenue,

            restock_cost:
                restockCost,

            special_cost:
                state.dailySpecialCost,

            profit:
                dailyProfit,

            money_before:
                moneyBeforeBusiness,

            money_after:
                state.money,

            decision_time_ms:
                decisionTime

        }
    );


    /*
       Animation khách hàng.
    */

    await animateCustomers(
        sold
    );


    /*
       Trừ hàng.
    */

    state.stock -=
        sold;


    /*
       Reset restock cho ngày sau.
    */

    state.restock =
        0;


    updateRestockDisplay();


    updateHUD();


    /*
       Hiển thị kết quả.
    */

    showDayResult({

        demand:
            demand,

        sold:
            sold,

        revenue:
            revenue,

        dailyProfit:
            dailyProfit

    });

}


/* =========================================================
   CUSTOMER ANIMATION
========================================================= */

function animateCustomers(
    sold
) {

    return new Promise(
        resolve => {

            if (
                !customersLayer
            ) {

                resolve();

                return;

            }


            customersLayer.innerHTML =
                "";


            /*
               Không tạo 60 emoji.
               Chỉ tạo tối đa 12 khách
               đại diện cho lượng khách thật.
            */

            const visualCustomers =
                Math.min(
                    12,
                    Math.max(
                        2,
                        Math.ceil(
                            sold / 5
                        )
                    )
                );


            let finished = 0;


            for (
                let i = 0;
                i < visualCustomers;
                i++
            ) {

                const customer =
                    document.createElement(
                        "div"
                    );


                customer.className =
                    "customer";


                const faces = [

                    "🧑",
                    "👩",
                    "👨",
                    "👧",
                    "🧒",
                    "👵",
                    "👴"

                ];


                customer.textContent =
                    faces[
                        Math.floor(
                            Math.random() *
                            faces.length
                        )
                    ];


                customer.style.bottom =
                    `${20 +
                    Math.random() * 55}px`;


                customer.style.transitionDelay =
                    `${i * 0.12}s`;


                customersLayer.appendChild(
                    customer
                );


                requestAnimationFrame(
                    () => {

                        customer.classList.add(
                            "enter"
                        );

                    }
                );


                setTimeout(
                    () => {

                        customer.classList.add(
                            "buy"
                        );

                    },
                    1500 +
                    i * 120
                );


                setTimeout(
                    () => {

                        customer.classList.add(
                            "leave"
                        );


                        finished++;


                        if (
                            finished >=
                            visualCustomers
                        ) {

                            setTimeout(
                                resolve,
                                600
                            );

                        }

                    },
                    2300 +
                    i * 120
                );

            }

        }
    );

}


/* =========================================================
   DAY RESULT
========================================================= */

function showDayResult(
    result
) {

    resultDemand.textContent =
        result.demand;


    resultSold.textContent =
        result.sold;


    resultRevenue.textContent =
        money(
            result.revenue
        );


    resultDailyProfit.textContent =
        money(
            result.dailyProfit
        );


    if (
        result.dailyProfit >=
        150000
    ) {

        resultIcon.textContent =
            "🔥";


        resultTitle.textContent =
            `Ngày ${state.day}: Quá tốt!`;


        resultMessage.textContent =
            "Bạn đã có một quyết định kinh doanh rất hiệu quả.";

    }

    else if (
        result.dailyProfit > 0
    ) {

        resultIcon.textContent =
            "🙂";


        resultTitle.textContent =
            `Ngày ${state.day}: Có lãi`;


        resultMessage.textContent =
            "Bạn đã kiếm được tiền. Nhưng liệu chiến lược này có tối ưu?";

    }

    else {

        resultIcon.textContent =
            "😵";


        resultTitle.textContent =
            `Ngày ${state.day}: Kinh doanh thua lỗ`;


        resultMessage.textContent =
            "Hãy suy nghĩ lại mối quan hệ giữa giá bán và nhu cầu.";

    }


    if (
        state.day >=
        state.maxDays
    ) {

        nextDayButton.textContent =
            "🏆 Xem kết quả cuối cùng";

    }

    else {

        nextDayButton.textContent =
            "Sang ngày tiếp theo →";

    }


    resultOverlay.classList.add(
        "show"
    );

}


/* =========================================================
   NEXT DAY
========================================================= */

nextDayButton.addEventListener(
    "click",
    function () {

        resultOverlay.classList.remove(
            "show"
        );


        /*
           Nếu đã đến ngày 5:
           kết thúc game.
        */

        if (
            state.day >=
            state.maxDays
        ) {

            finishGameAndShowResult();

            return;

        }


        state.day++;

        state.dayRunning =
            false;

        state.restock =
            0;

        state.dayStartTime =
            Date.now();


        /*
           Mở lại điều khiển.
        */

        priceSlider.disabled =
            false;

        restockMinus.disabled =
            false;

        restockPlus.disabled =
            false;

        openShopButton.disabled =
            false;


        /*
           Reset giá về 20.
        */

        priceSlider.value =
            20;

        state.price =
            20;


        updatePrice();

        updateRestockDisplay();


        /*
           Chọn sự kiện mới.
        */

        selectEvent();


        updateHUD();


        addFeed(
            `🌅 Ngày ${state.day} bắt đầu.`
        );


        recordEvent(
            "day_start",
            {

                day:
                    state.day,

                event:
                    state.currentEvent.id

            }
        );

    }
);


/* =========================================================
   FINAL RESULT
========================================================= */

async function finishGameAndShowResult() {

    if (
        state.gameFinished
    ) {

        return;

    }


    state.gameFinished =
        true;


    /*
       Thưởng mục tiêu lợi nhuận.
    */

    if (
        state.totalProfit >=
        500000
    ) {

        state.score +=
            300;

    }


    /*
       Thưởng quản lý hàng tốt.
    */

    if (
        state.noStockout
    ) {

        state.score +=
            150;

    }


    /*
       Thưởng khả năng thích nghi.
    */

    if (
        state.adaptiveDecisions >=
        2
    ) {

        state.score +=
            150;

    }


    /*
       Ghi toàn bộ kết quả.
    */

    await recordEvent(
        "game_complete",
        {

            total_profit:
                state.totalProfit,

            total_revenue:
                state.totalRevenue,

            total_sold:
                state.totalSold,

            total_customers:
                state.totalCustomers,

            final_money:
                state.money,

            score:
                state.score,

            no_stockout:
                state.noStockout,

            adaptive_decisions:
                state.adaptiveDecisions,

            decisions:
                state.decisions

        }
    );


    /*
       Kết thúc session.
    */

    await finishGame();


    /*
       Hiển thị kết quả.
    */

    finalProfit.textContent =
        money(
            state.totalProfit
        );


    finalCustomers.textContent =
        state.totalCustomers;


    finalSold.textContent =
        state.totalSold;


    finalScore.textContent =
        state.score;


    finalMoney.textContent =
        money(
            state.money
        );


    /*
       Achievement 1
    */

    if (
        state.totalProfit >=
        500000
    ) {

        achievementProfit.textContent =
            "🏆 Đã đạt mục tiêu 500.000đ";


        achievementProfit.classList.add(
            "unlocked"
        );

    }


    /*
       Achievement 2
    */

    if (
        state.noStockout
    ) {

        achievementStock.textContent =
            "📦 Không để cửa hàng hết hàng";


        achievementStock.classList.add(
            "unlocked"
        );

    }


    /*
       Achievement 3
    */

    if (
        state.adaptiveDecisions >=
        2
    ) {

        achievementStrategy.textContent =
            "🧠 Nhà kinh doanh biết thích nghi";


        achievementStrategy.classList.add(
            "unlocked"
        );

    }


    finalOverlay.classList.add(
        "show"
    );

}


/* =========================================================
   INITIALIZE GAME
========================================================= */

async function initGame() {

    console.log(
        "================================="
    );

    console.log(
        "GAME 01 - ÔNG CHỦ TẬP SỰ"
    );

    console.log(
        "Lesson ID:",
        LESSON_ID
    );

    console.log(
        "User ID:",
        USER_ID
    );

    console.log(
        "Game ID:",
        GAME_ID
    );

    console.log(
        "================================="
    );


    /*
       Khởi tạo giao diện.
    */

    selectEvent();

    updatePrice();

    updateRestockDisplay();

    updateHUD();


    /*
       Feed ban đầu.
    */

    addFeed(
        "👋 Chào mừng bạn đến với cửa hàng!"
    );

    addFeed(
        "💡 Hãy thử thay đổi giá và quan sát nhu cầu khách hàng."
    );


    /*
       Tạo session backend.
    */

    await createGameSession();


    /*
       Ghi game_start.
    */

    await recordEvent(
        "game_start",
        {

            game:
                "store_management",

            lesson_id:
                LESSON_ID,

            day:
                1,

            starting_money:
                state.startingMoney,

            starting_stock:
                state.stock

        }
    );

}


/* =========================================================
   START GAME
========================================================= */

initGame();