document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('starCanvas');
    const ctx = canvas.getContext('2d');

    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    let stars = [];
    const numberOfStars = 300;
    let hoverEffect = false;

    function generateStars(){
        for(let i = 0; i < numberOfStars; i++){
            stars.push({
                x: Math.random() * canvas.width,
                y: Math.random() * canvas.height,
                radius: Math.random() * 2 + .5,
                dx: (Math.random() - 0.2) * .5,
                dy: (Math.random() - 0.2) * .5,
                /* color: 'rgb(199, 226, 252)', */
            });
        }
    }

    function drawStars(){
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        stars.forEach(star => {
            ctx.beginPath();
            ctx.arc(star.x, star.y, star.radius, 0, Math.PI * 2, false);
            ctx.fillStyle = hoverEffect ? '#3880c4' : 'rgb(169, 212, 252)';
            ctx.fill();
        });
    }
    let hoverPosition = { x: 0, y: 0 }; 

    document.querySelectorAll('.hero-left a').forEach(anchor => {
        anchor.addEventListener('mouseenter', (e) => {
            const rect = e.target.getBoundingClientRect();
            hoverEffect = true;
            hoverPosition = { 
                x: rect.left + rect.width / 2, 
                y: rect.top + rect.height / 2 
            };
        });
        anchor.addEventListener('mouseleave', () => hoverEffect = false);
    });

    function update(){
        if(hoverEffect){
            stars.forEach(star => {
                star.x += star.dx * 3;
                star.y += star.dy * 3;
    
                if (star.x < 0 || star.x > canvas.width) star.dx *= -1;
                if (star.y < 0 || star.y > canvas.height) star.dy *= -1; 
        
        })}}

    function animate() {
        requestAnimationFrame(animate);
        drawStars();
        update();
    }

    

    generateStars();
    animate();
});
