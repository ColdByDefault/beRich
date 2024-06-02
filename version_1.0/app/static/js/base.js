const canvas = document.querySelector('canvas');
const ctx = canvas.getContext('2d');

let w = canvas.width = window.innerWidth;
let h = canvas.height = window.innerHeight;
let stars = [];
const starCount = 300;

class Star {
  constructor() {
    this.x = Math.random() * w;
    this.y = Math.random() * h;
    this.radius = Math.random() * .9;
    this.speed = Math.random() * 0.5 + 0.2;
    this.directionAngle = Math.floor(Math.random() * 360);
    this.color = "white";

    this.vx = Math.cos(this.directionAngle) * this.speed;
    this.vy = Math.sin(this.directionAngle) * this.speed;
  }

  draw() {
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2, false);
    ctx.fillStyle = this.color;
    ctx.fill();
  }

  update() {
    this.border();
    this.x += this.vx;
    this.y += this.vy;
  }

  border() {
    if (this.x <= 0 || this.x >= w) this.vx *= -1;
    if (this.y <= 0 || this.y >= h) this.vy *= -1;
  }
}

function createStars() {
  for (let i = 0; i < starCount; i++) {
    stars.push(new Star());
  }
}

function draw() {
  ctx.clearRect(0, 0, w, h);
  for (let i = 0; i < stars.length; i++) {
    stars[i].draw();
    stars[i].update();
  }
}

function resize() {
  w = canvas.width = window.innerWidth;
  h = canvas.height = window.innerHeight;
}

window.addEventListener('resize', resize);
createStars();
setInterval(draw, 20);