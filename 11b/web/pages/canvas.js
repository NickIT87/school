document.addEventListener("DOMContentLoaded", function() {
    console.log("DOMContentLoaded");

    const canvas = document.querySelector("canvas");
    const ctx = canvas.getContext("2d");
    ctx.fillStyle = "green";
    // Add a rectangle at (10, 10) with size 100x100 pixels
    ctx.fillRect(10, 10, 100, 100);

    ctx.fillStyle = "red";
    ctx.fillRect(100, 100, 100, 100);

    let xPosition = 100;

    function drawRedCube(x) {
        ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear the canvas
        ctx.fillStyle = "green";
        ctx.fillRect(10, 10, 100, 100);
        ctx.fillStyle = "red";
        ctx.fillRect(x, 100, 100, 100);
    }

    function moveRedCube() {
        if (xPosition < 490) {
            xPosition += 5; // Adjust the movement speed as needed
            drawRedCube(xPosition);
            // Request the next animation frame
            requestAnimationFrame(moveRedCube);
        }
    }

    // Start the animation loop
    moveRedCube();
});