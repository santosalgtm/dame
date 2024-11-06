const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");
const cellSize = 20;

async function fetchGameState() {
    const response = await fetch("/api/snake/get_game_state");
    return await response.json();
}

function drawGame(state) {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    // Draw snake
    state.snake.forEach(part => {
        ctx.fillStyle = "green";
        ctx.fillRect(part.x * cellSize, part.y * cellSize, cellSize, cellSize);
    });

    // Draw food
    ctx.fillStyle = "red";
    ctx.fillRect(state.food.x * cellSize, state.food.y * cellSize, cellSize, cellSize);
}

async function gameLoop() {
    const state = await fetchGameState();
    drawGame(state);
    if (!state.game_over) {
        setTimeout(gameLoop, 200);
    } else {
        alert("Game Over!");
    }
}

window.addEventListener("keydown", async (e) => {
    const directionMap = {
        "ArrowUp": "up",
        "ArrowDown": "down",
        "ArrowLeft": "left",
        "ArrowRight": "right"
    };
    if (directionMap[e.key]) {
        await fetch(`/api/snake/change_direction?direction=${directionMap[e.key]}`, { method: "POST" });
    }
});

gameLoop();
