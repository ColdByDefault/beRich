const canvas = document.getElementById('starsCanvas');
const ctx = canvas.getContext('2d');

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const starRadius = 1.5;
const starCount = 300;
const stars = [];
const speed = 0.5;
const maxDepth = 5;

function createStar() {
    const x = Math.random() * canvas.width;
    const y = Math.random() * canvas.height;
    const z = Math.random() * maxDepth;
    const dx = (Math.random() - 0.5) * speed * (z / maxDepth);
    const dy = (Math.random() - 0.5) * speed * (z / maxDepth);
    return { x, y, dx, dy, z };
}

function initializeStars() {
    stars.length = 0;  // Clear existing stars
    for (let i = 0; i < starCount; i++) {
        stars.push(createStar());
    }
}

initializeStars();

function drawStar(star) {
    ctx.beginPath();
    const adjustedRadius = starRadius * (star.z / maxDepth);
    ctx.arc(star.x, star.y, adjustedRadius, 0, Math.PI * 2);
    ctx.fillStyle = '#00bbf0';
    ctx.fill();
    ctx.closePath();
}

function updateStar(star) {
    star.x += star.dx;
    star.y += star.dy;

    if (star.x - starRadius > canvas.width) star.x = -starRadius;
    if (star.x + starRadius < 0) star.x = canvas.width + starRadius;
    if (star.y - starRadius > canvas.height) star.y = -starRadius;
    if (star.y + starRadius < 0) star.y = canvas.height + starRadius;
}

function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    stars.forEach(star => {
        drawStar(star);
        updateStar(star);
    });
    requestAnimationFrame(animate);
}

animate();

window.addEventListener('resize', () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    initializeStars();  // Reinitialize stars to fit the new canvas size
});




/* theme btn */
const themes = [
    {
        '--prime-background-color': '#00204a',
        '--secondary-background-color': '#222',
        '--color-palette-first': '#005792',
        '--color-palette-second': '#00bbf0',
        '--color-palette-third': '#fdb44b', 
        '--color-palette-fourth': '#41d8bf',
        '--color-palette-fifth': '#ee5a5a',
    },
    {
        '--prime-background-color': '#000000',
        '--secondary-background-color': '#14213d',
        '--color-palette-first': '#22223b',
        '--color-palette-second': '#4a4e69',
        '--color-palette-third': '#9a8c98', 
        '--color-palette-fourth': '#c9ada7',
        '--color-palette-fifth': '#f2e9e4',
    }
];

document.addEventListener('DOMContentLoaded', () => {
    // Check if there's a theme index saved in local storage
    let themeIndex = localStorage.getItem('themeIndex');
    if (themeIndex !== null) {
        themeIndex = parseInt(themeIndex, 10);
        applyTheme(themes[themeIndex]);
    } else {
        themeIndex = 0;
        applyTheme(themes[themeIndex]);
    }
    localStorage.setItem('themeIndex', themeIndex);
});

function toggleTheme() {
    // Get the current theme index from local storage
    let themeIndex = localStorage.getItem('themeIndex');
    themeIndex = (parseInt(themeIndex, 10) + 1) % themes.length;
    
    // Apply the next theme
    applyTheme(themes[themeIndex]);
    
    // Save the new theme index to local storage
    localStorage.setItem('themeIndex', themeIndex);
}

function applyTheme(theme) {
    for (const [key, value] of Object.entries(theme)) {
        document.documentElement.style.setProperty(key, value);
    }
}







/* '--prime-background-color': '#00204a',
        '--secondary-background-color': '#222',
        '--color-palette-first': '#005792',
        '--color-palette-second': '#00bbf0',
        '--color-palette-third': '#fdb44b', 
        '--color-palette-fourth': '#41d8bf',
        '--color-palette-fifth': '#ee5a5a', */

/* '--prime-background-color': '#000000',
        '--secondary-background-color': '#14213d',
        '--color-palette-first': '#22223b',
        '--color-palette-second': '#4a4e69',
        '--color-palette-third': '#9a8c98', 
        '--color-palette-fourth': '#c9ada7',
        '--color-palette-fifth': '#f2e9e4', */