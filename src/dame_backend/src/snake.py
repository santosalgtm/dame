from kybra import query, update, Principal
from typing import List, Dict

# Game board size
BOARD_WIDTH = 10
BOARD_HEIGHT = 10

# Initial state
snake: List[Dict[str, int]] = [{"x": 5, "y": 5}]
direction: Dict[str, int] = {"x": 0, "y": 1}  # Moving right initially
food: Dict[str, int] = {"x": 3, "y": 3}
game_over: bool = False

@query
def get_game_state() -> Dict:
    return {
        "snake": snake,
        "food": food,
        "game_over": game_over
    }

@update
def change_direction(new_direction: str):
    global direction
    if new_direction == "up":
        direction = {"x": 0, "y": -1}
    elif new_direction == "down":
        direction = {"x": 0, "y": 1}
    elif new_direction == "left":
        direction = {"x": -1, "y": 0}
    elif new_direction == "right":
        direction = {"x": 1, "y": 0}

@update
def update_game():
    global snake, food, game_over
    if game_over:
        return

    # Move the snake
    new_head = {
        "x": (snake[0]["x"] + direction["x"]) % BOARD_WIDTH,
        "y": (snake[0]["y"] + direction["y"]) % BOARD_HEIGHT
    }
    snake.insert(0, new_head)

    # Check if snake eats food
    if new_head["x"] == food["x"] and new_head["y"] == food["y"]:
        food = {"x": randint(0, BOARD_WIDTH - 1), "y": randint(0, BOARD_HEIGHT - 1)}
    else:
        snake.pop()  # Remove tail

    # Check for collisions
    if new_head in snake[1:]:
        game_over = True
