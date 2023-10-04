
# ====== GAME WINDOW ====== #
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

# ====== ANIMATION ====== #
TIME_STEP = 0.01
DECREASE_INCREMENT = 0.85

# ====== PLAYER CHARACTER ====== #
PLAYER_STARTING_POSITION = (0, -SCREEN_HEIGHT / 2 + 20)
PLAYER_COLOUR = "black"
PLAYER_MOVE_INCREMENT = 20

# ====== CAR OBSTACLES ====== #
SPAWN_VALUE = 200   # higher value -> less likely for a car to spawn
SPAWN_INCREMENT = 20    # number to reduce SPAWN_VALUE for every increase in difficulty
CAR_WIDTH = 30
CAR_LENGTH = 40
CAR_GAP = 5     # vertical gap between cars
CAR_MOVE_INCREMENT = 2
CAR_COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

# ====== SCOREBOARD ====== #
TEXT_COLOUR = "black"
TEXT_LOCATION = (-SCREEN_WIDTH / 2 + 20, SCREEN_HEIGHT / 2 - 45)
FONT = ("Courier", 20, "normal")
