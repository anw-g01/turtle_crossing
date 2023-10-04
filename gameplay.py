from turtle import Screen
from config import *
from classes import Player, CarManager, Scoreboard
import time


def make_screen():
    """Initialise the Screen() object from the turtle module for the game window."""
    screen = Screen()
    screen.title("Turtle Crossing")
    screen.setup(
        width=SCREEN_WIDTH,
        height=SCREEN_HEIGHT
    )
    screen.tracer(0)
    return screen


class Game:
    """
    Represents the turtle crossing game and holds the main game logic methods.

    attributes:
    screen - instantiates a Screen() object from the turtle class
    player - instantiates a Player() object to form the player's turtle character
    car_manager - instantiates the CarManager() object to call all relevant car handling methods
    current_level (int) - the current level of the game
    scoreboard - instantiates a Scoreboard() object to call text displaying methods
    time_step (int) - governs the speed of the animation of the movement in the game
    spawn_frequency (int) - a value associated with the random probability of spawning cars
    """
    def __init__(self):
        self.screen = make_screen()
        self.player = Player()
        self.car_manager = CarManager()
        self.current_level = 1
        self.scoreboard = Scoreboard(self.current_level)
        self.time_step = TIME_STEP
        self.spawn_frequency = SPAWN_VALUE

    def update_screen(self):
        """Updates the screen with the next frame of the game animation using TIME_STEP increments."""
        self.screen.update()
        time.sleep(self.time_step)

    def configure_controls(self):
        """Configures keybindings for controlling the player's turtle character."""
        self.screen.listen()
        self.screen.onkey(self.player.move_up, "Up")
        self.screen.onkey(self.player.move_down, "Down")
        self.screen.onkey(self.player.move_left, "Left")
        self.screen.onkey(self.player.move_right, "Right")

    def spawn_cars(self):
        """Generates cars and marches them across the game window."""
        self.car_manager.generate_cars()
        self.car_manager.march_cars()

    def increase_difficulty(self):
        """
        Decreases the animation time step and SPAWN_INCREMENT value to increase car
        speed and spawning frequency for progressing difficulties.
        """
        self.time_step *= DECREASE_INCREMENT    # percentage decrease in time step
        self.spawn_frequency -= SPAWN_INCREMENT   # increase the chance of more cars to spawn

    def next_level(self):
        """
        Updates level attributes, text displays, resets the player's turtle
        character to the starting position, and increases the difficulty.
        """
        if self.player.reach_finish_line():
            self.current_level += 1
            self.increase_difficulty()
            self.scoreboard.increase_level()
            self.player.reset_turtle_pos()

    def game_over(self):
        """
        Checks if player has collided with a car obstacle. If so
        end the game by displaying relevant text and reset and game settings.
        """
        if self.car_manager.collision(self.player):
            self.car_manager.hide_half()    # remove half the cars on display as a visual
            self.update_screen()
            self.scoreboard.display_game_over()
            self.current_level = 1      # reset level
            self.time_step = TIME_STEP      # reset speed of animation
            return True

    def play_again(self):
        """Prompts the user if they wish to play a new game."""
        while True:
            ans = self.screen.textinput(
                title="Game Over",
                prompt="Play again? (y/n)?"
            ).lower()
            if ans in ["y", "n"]:
                return ans == "y"
            print("Invalid input. Try again.")

    def reset_game(self):
        """Resets all attributes related to current level, player position and car obstacles."""
        self.scoreboard.reset_level()
        self.player.reset_turtle_pos()
        self.car_manager.reset_cars()




