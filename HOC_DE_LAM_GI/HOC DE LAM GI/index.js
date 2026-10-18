const dialog = document.getElementById('dialog');
const dialogTitle = document.getElementById('dialogTitle');
const dialogText = document.getElementById('dialogText');
const confirmDialog = document.getElementById('confirmDialog');
const skyLayer = document.getElementById('skyLayer');
const homeScene = document.getElementById('homeScene');
const islandsLayer = document.getElementById('islandsLayer');
const parallaxFar = document.getElementById('parallaxFar');
let nextAction = null;

function showDialog(title, message, label = 'Đã hiểu', action = null) {
  dialogTitle.textContent = title;
  dialogText.textContent = message;
  confirmDialog.textContent = label;
  nextAction = action;
  dialog.classList.add('open');
  dialog.setAttribute('aria-hidden', 'false');
}

function hideDialog() {
  dialog.classList.remove('open');
  dialog.setAttribute('aria-hidden', 'true');
  nextAction = null;
}

document.getElementById('closeDialog').addEventListener('click', hideDialog);
dialog.addEventListener('click', e => { if (e.target === dialog) hideDialog(); });
confirmDialog.addEventListener('click', () => {
  const action = nextAction;
  hideDialog();
  if (action) action();
});
document.addEventListener('keydown', e => { if (e.key === 'Escape') hideDialog(); });

// Điều hướng khi bấm vào các đảo môn học
document.querySelectorAll('.hit[data-page]').forEach(b => {
  b.addEventListener('click', () => {
    window.location.href = b.dataset.page;
  });
});

// Các nút thông tin & Popup
document.getElementById('centerHit').addEventListener('click', () =>
  showDialog('Chân Tri', 'Nơi khám phá kiến thức qua tình huống thực tế và mini game để vận dụng điều đã học vào giải quyết vấn đề.')
);

document.getElementById('classButton').addEventListener('click', () =>
  showDialog('Lớp 12A3', 'Khu vực lớp học sẽ có thành viên, nhiệm vụ chung và thành tích của cả lớp.')
);

document.getElementById('rankingButton').addEventListener('click', () =>
  showDialog('Bảng xếp hạng', 'Thành tích người chơi sẽ được tổng hợp từ điểm kinh nghiệm và các nhiệm vụ hoàn thành.')
);

document.querySelectorAll('.hit[data-popup]').forEach(b => {
  b.addEventListener('click', () => {
    const name = b.dataset.popup;
    if (name === 'Thoát') {
      showDialog('Thoát', 'Bạn có muốn rời khỏi trang chủ không?', 'Rời trang', () => {
        window.location.href = 'about:blank';
      });
    } else {
      showDialog(name, `Khu vực ${name.toLowerCase()} sẽ được kết nối với dữ liệu người chơi ở bước phát triển tiếp theo.`);
    }
  });
});

/* ================= 1. ENGINE TÁCH NỀN THÔNG MINH CHO 2 MẪU ĐẢO ĐỒ SỘ MỚI ================= */
function loadImg(src) {
  return new Promise((resolve, reject) => {
    const img = new Image();
    img.onload = () => resolve(img);
    img.onerror = reject;
    img.src = src;
  });
}

async function processIslandImage(src, selector) {
  try {
    const img = await loadImg(src);
    const maxDim = 960;
    const scale = Math.min(1, maxDim / Math.max(img.naturalWidth, img.naturalHeight));
    const w = Math.round(img.naturalWidth * scale);
    const h = Math.round(img.naturalHeight * scale);

    const c = document.createElement('canvas');
    c.width = w;
    c.height = h;
    const ctx = c.getContext('2d');
    ctx.drawImage(img, 0, 0, w, h);

    const imgData = ctx.getImageData(0, 0, w, h);
    const d = imgData.data;
    const visited = new Uint8Array(w * h);

    // Xóa watermark góc dưới phải
    for (let y = Math.floor(h * 0.88); y < h; y++) {
      for (let x = Math.floor(w * 0.88); x < w; x++) {
        d[(y * w + x) * 4 + 3] = 0;
      }
    }

    // Phân biệt nền trắng/xám trung tính với bọt thác nước (bọt thác có ánh xanh B > R)
    const isBgPixel = idx => {
      const r = d[idx], g = d[idx + 1], b = d[idx + 2];
      const max = Math.max(r, g, b), min = Math.min(r, g, b);
      return (r > 228 && g > 228 && b > 228 && (b - r) < 10) || (max - min < 16 && min > 195);
    };

    const stack = [];
    for (let x = 0; x < w; x++) stack.push(x, (h - 1) * w + x);
    for (let y = 0; y < h; y++) stack.push(y * w, y * w + (w - 1));

    while (stack.length > 0) {
      const p = stack.pop();
      if (p < 0 || p >= w * h || visited[p]) continue;
      visited[p] = 1;

      const idx = p * 4;
      if (isBgPixel(idx)) {
        d[idx + 3] = 0;
        const x = p % w;
        const y = (p / w) | 0;
        if (x > 0) stack.push(p - 1);
        if (x < w - 1) stack.push(p + 1);
        if (y > 0) stack.push(p - w);
        if (y < h - 1) stack.push(p + w);
      } else {
        const r = d[idx], g = d[idx + 1], b = d[idx + 2];
        if (r > 210 && g > 210 && b > 210 && (b - r) < 12) {
          d[idx + 3] = Math.max(0, 255 - ((r + g + b) / 3 - 210) * 5.5);
        }
      }
    }

    // Xóa các khe trắng純 túy (#FFFFFF) bị kẹt giữa các sợi dây leo, vòm cổng đá và gầm cầu
    for (let i = 0; i < w * h; i++) {
      const idx = i * 4;
      if (d[idx + 3] > 0) {
        const r = d[idx], g = d[idx + 1], b = d[idx + 2];
        const diff = Math.max(r, g, b) - Math.min(r, g, b);
        if (r > 240 && g > 240 && b > 240 && diff < 8) {
          d[idx + 3] = 0;
        } else if (r > 226 && g > 226 && b > 226 && diff < 8) {
          d[idx + 3] = Math.round(d[idx + 3] * 0.2);
        }
      }
    }

    ctx.putImageData(imgData, 0, 0);
    c.toBlob(blob => {
      if (!blob) return;
      const url = URL.createObjectURL(blob);
      document.querySelectorAll(selector).forEach(el => {
        el.style.backgroundImage = `url("${url}")`;
      });
    }, 'image/png');
  } catch (e) {
    console.error('Lỗi xử lý ảnh đảo:', src, e);
  }
}

const birdFrames = { up: '', down: '' };

async function processSpriteSheet(src, mappingList) {
  try {
    const img = await loadImg(src);
    const W = img.naturalWidth;
    const H = img.naturalHeight;
    const cellW = W / 4;
    const cellH = H / 4;

    for (const item of mappingList) {
      const { col, row, selector, removeInnerWhite, saveKey } = item;
      const padX = cellW * 0.04;
      const padY = cellH * 0.04;
      const sx = col * cellW + padX;
      const sy = row * cellH + padY;
      const sw = cellW - padX * 2;
      const sh = cellH - padY * 2;

      const size = 240;
      const c = document.createElement('canvas');
      c.width = size;
      c.height = size;
      const ctx = c.getContext('2d');
      ctx.drawImage(img, sx, sy, sw, sh, 0, 0, size, size);

      const imgData = ctx.getImageData(0, 0, size, size);
      const d = imgData.data;
      const visited = new Uint8Array(size * size);

      const isBg = idx => {
        const r = d[idx], g = d[idx + 1], b = d[idx + 2];
        const max = Math.max(r, g, b), min = Math.min(r, g, b);
        return (r > 224 && g > 224 && b > 224) || (max - min < 20 && min > 165);
      };

      const stack = [];
      for (let x = 0; x < size; x++) stack.push(x, (size - 1) * size + x);
      for (let y = 0; y < size; y++) stack.push(y * size, y * size + (size - 1));

      while (stack.length > 0) {
        const p = stack.pop();
        if (p < 0 || p >= size * size || visited[p]) continue;
        visited[p] = 1;

        const idx = p * 4;
        if (isBg(idx)) {
          d[idx + 3] = 0;
          const x = p % size;
          const y = (p / size) | 0;
          if (x > 0) stack.push(p - 1);
          if (x < size - 1) stack.push(p + 1);
          if (y > 0) stack.push(p - size);
          if (y < size - 1) stack.push(p + size);
        } else {
          const r = d[idx], g = d[idx + 1], b = d[idx + 2];
          if (r > 205 && g > 205 && b > 205) {
            d[idx + 3] = Math.max(0, 255 - ((r + g + b) / 3 - 205) * 5);
          }
        }
      }

      if (removeInnerWhite) {
        for (let i = 0; i < size * size; i++) {
          const idx = i * 4;
          if (d[idx + 3] > 0 && d[idx] > 238 && d[idx + 1] > 238 && d[idx + 2] > 238) {
            d[idx + 3] = 0;
          }
        }
      }

      ctx.putImageData(imgData, 0, 0);
      const dataUrl = c.toDataURL('image/png');

      if (saveKey) {
        birdFrames[saveKey] = dataUrl;
      }
      if (selector) {
        document.querySelectorAll(selector).forEach(el => {
          el.style.backgroundImage = `url("${dataUrl}")`;
        });
      }
    }
  } catch (e) {
    console.error('Lỗi cắt Sprite Sheet:', src, e);
  }
}

// Khởi chạy tách nền cho 2 mẫu đảo mới và 32 dụng cụ
processIslandImage('assets/island-center.png', '.island-center-art');
processIslandImage('assets/island-subject.png', '.island-art');

processSpriteSheet('assets/props-sheet-1.png', [
  { col: 0, row: 0, selector: '.flask-left' },
  { col: 1, row: 0, selector: '.flask-right' },
  { col: 2, row: 0, selector: '.chem-boom, .spark, .lava' },
  { col: 3, row: 0, selector: '.chem-smoke' },
  { col: 0, row: 1, selector: '.ruler', removeInnerWhite: true },
  { col: 1, row: 1, selector: '.compass', removeInnerWhite: true },
  { col: 2, row: 1, selector: '.magnet', removeInnerWhite: true },
  { col: 3, row: 1, selector: '.apple' },
  { col: 0, row: 2, selector: '.book' },
  { col: 1, row: 2, selector: '.quill, .brush' },
  { col: 2, row: 2, selector: '.shoe' },
  { col: 3, row: 2, selector: '.ball' },
  { col: 0, row: 3, selector: '.palette', removeInnerWhite: true },
  { col: 1, row: 3, selector: '.globe' },
  { col: 2, row: 3, selector: '.volcano' },
  { col: 3, row: 3, selector: '.laptop' }
]);

processSpriteSheet('assets/props-sheet-2.png', [
  { col: 0, row: 0, selector: '.sprout, .bush-l, .bush-r' },
  { col: 1, row: 0, selector: '.flower, .rainbow' },
  { col: 2, row: 0, selector: '.butterfly, .bird-paper' },
  { col: 3, row: 0, selector: '.bug' },
  { col: 0, row: 1, selector: '.hammer' },
  { col: 1, row: 1, selector: '.chat-a' },
  { col: 2, row: 1, selector: '.chat-b' },
  { col: 3, row: 1, selector: '.music-fx' },
  { col: 0, row: 2, selector: '.sword-l, .sword-r' },
  { col: 1, row: 2, selector: '.crown' },
  { col: 2, row: 2, selector: '.crystal' },
  { col: 3, row: 2, selector: '.goal' },
  { col: 0, row: 3, selector: '.cloud-white' },
  { col: 1, row: 3, selector: '.cloud-gold' },
  { col: 2, row: 3, saveKey: 'up' },
  { col: 3, row: 3, saveKey: 'down' }
]);

/* ================= 2. HIỆU ỨNG CAMERA PARALLAX KHI DI CHUỘT ================= */
homeScene.addEventListener('mousemove', e => {
  const x = (e.clientX / window.innerWidth - 0.5);
  const y = (e.clientY / window.innerHeight - 0.5);
  islandsLayer.style.transform = `translate(${x * -20}px, ${y * -14}px)`;
  if (parallaxFar) {
    parallaxFar.style.transform = `translate(${x * 24}px, ${y * 14}px) scale(1.04)`;
  }
});

/* ================= 3. HỆ THỐNG CANVAS 60FPS (SAO BĂNG & ĐOM ĐÓM BOKEH) ================= */
const canvas = document.getElementById('cinematicCanvas');
const ctx = canvas ? canvas.getContext('2d') : null;
let cw = 0, ch = 0;

function resizeCanvas() {
  if (!canvas) return;
  cw = canvas.width = window.innerWidth;
  ch = canvas.height = window.innerHeight;
}
window.addEventListener('resize', resizeCanvas);
resizeCanvas();

const orbs = Array.from({ length: 28 }, () => ({
  x: Math.random() * window.innerWidth,
  y: Math.random() * window.innerHeight,
  r: Math.random() * 4 + 1.5,
  vy: -(Math.random() * 0.55 + 0.2),
  vx: (Math.random() - 0.5) * 0.35,
  hue: Math.random() > 0.45 ? '#fde047' : '#38bdf8',
  alpha: Math.random() * 0.65 + 0.25
}));

let shootingStar = null;
setInterval(() => {
  if (!document.hidden && Math.random() < 0.75) {
    shootingStar = {
      x: Math.random() * cw * 0.65 + cw * 0.2,
      y: Math.random() * ch * 0.25 + 20,
      vx: -9,
      vy: 4.5,
      len: 110,
      life: 1
    };
  }
}, 4500);

function renderCinematicCanvas() {
  if (!ctx) return;
  ctx.clearRect(0, 0, cw, ch);

  if (shootingStar) {
    const st = shootingStar;
    const grad = ctx.createLinearGradient(st.x, st.y, st.x - st.vx * 10, st.y - st.vy * 10);
    grad.addColorStop(0, `rgba(255, 250, 210, ${st.life})`);
    grad.addColorStop(1, 'rgba(56, 189, 248, 0)');
    ctx.strokeStyle = grad;
    ctx.lineWidth = 2.4;
    ctx.beginPath();
    ctx.moveTo(st.x, st.y);
    ctx.lineTo(st.x + st.len, st.y - st.len * 0.5);
    ctx.stroke();

    st.x += st.vx;
    st.y += st.vy;
    st.life -= 0.022;
    if (st.life <= 0) shootingStar = null;
  }

  orbs.forEach(o => {
    o.x += o.vx;
    o.y += o.vy;
    if (o.y < -20) {
      o.y = ch + 15;
      o.x = Math.random() * cw;
    }
    ctx.save();
    ctx.globalAlpha = o.alpha;
    ctx.shadowColor = o.hue;
    ctx.shadowBlur = 12;
    ctx.fillStyle = o.hue;
    ctx.beginPath();
    ctx.arc(o.x, o.y, o.r, 0, Math.PI * 2);
    ctx.fill();
    ctx.restore();
  });

  requestAnimationFrame(renderCinematicCanvas);
}
renderCinematicCanvas();

/* ================= 4. ĐÀN CHIM VỖ CÁNH 2 FRAME ================= */
function spawnFlyingBirds() {
  if (!skyLayer || !birdFrames.up) return;

  const group = document.createElement('div');
  group.className = 'flying-bird-group';

  const isFlock = Math.random() < 0.65;
  group.innerHTML = isFlock
    ? `<div class="bird-sprite"></div><div class="bird-sprite small-mate"></div>`
    : `<div class="bird-sprite"></div>`;

  const sprites = group.querySelectorAll('.bird-sprite');
  let flap = false;
  sprites.forEach(s => { s.style.backgroundImage = `url("${birdFrames.up}")`; });

  const flapTimer = setInterval(() => {
    flap = !flap;
    const frame = flap ? birdFrames.down : birdFrames.up;
    sprites.forEach(s => { s.style.backgroundImage = `url("${frame}")`; });
  }, 220);

  const randomTop = Math.floor(Math.random() * 58) + 6;
  const duration = (Math.random() * 7 + 12).toFixed(1);

  group.style.top = `${randomTop}%`;
  group.style.animationDuration = `${duration}s`;

  skyLayer.appendChild(group);

  setTimeout(() => {
    clearInterval(flapTimer);
    group.remove();
  }, parseFloat(duration) * 1000 + 500);
}

setTimeout(spawnFlyingBirds, 1200);
setInterval(() => {
  if (!document.hidden) {
    spawnFlyingBirds();
  }
}, 5200);