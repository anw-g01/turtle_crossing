from turtle import Turtle
from config import *
import random


class Player(Turtle):
    """
    Inherits the Turtle class from the turtle module to represent the player.

    attributes (all inherited):
    setpos -  player starts the game at the bottom centre of the screen window
    color -  color of the player
    setheading -  player character (turtle) always faces upwards (north) to begin
    """

    def __init__(self):
        super().__init__(shape="turtle")
        self.penup()
        self.setpos(PLAYER_STARTING_POSITION)
        self.color(PLAYER_COLOUR)
        self.setheading(90)

    def move_up(self):
        """Moves the player one step upward after facing the north direction."""
        self.setheading(90)     # north
        self.forward(PLAYER_MOVE_INCREMENT)     # self.goto(self.xcor(), self.ycor() + PLAYER_MOVE_INCREMENT)

    def move_down(self):
        """Moves the player one step downward after facing the south direction."""
        self.setheading(270)    # south
        self.forward(PLAYER_MOVE_INCREMENT)

    def move_left(self):
        """Moves the player one step to the left after facing the west direction."""
        self.setheading(180)    # west
        self.forward(PLAYER_MOVE_INCREMENT)

    def move_right(self):
        """Moves the player one step to the right after facing the east direction."""
        self.setheading(0)    # east
        self.forward(PLAYER_MOVE_INCREMENT)

    def reach_finish_line(self):
        """Boolean check if the player character has reached the top of the window screen i.e. reach the next level."""
        if self.ycor() > SCREEN_HEIGHT / 2:
            return True
        return False

    def reset_turtle_pos(self):
        """Returns the turtle to the starting position."""
        self.setheading(90)
        self.goto(PLAYER_STARTING_POSITION)


class Car(Turtle):
    """
    Inherits the Turtle class from the turtle module to represent a moving car obstacle.

    args:
    right_side (bool) - creates a left-moving car if True, otherwise right-moving. Used
    to spawn and move cars from both the left and right of the screen in the game.

    attributes (all inherited):
    setpos -  player starts the game at the bottom centre of the screen window
    color -  color of the car set randomly from a list of colours
    shapesize - uses integer parameters, CAR_WIDTH and CAR_LENGTH, to stretch the size into a rectangular car-like body.
    """

    def __init__(self, right_side=True):
        super().__init__(shape="square")
        self.penup()
        self.color(random.choice(CAR_COLORS))
        self.shapesize(
            stretch_wid=CAR_WIDTH / 20,
            stretch_len=CAR_LENGTH / 20
        )
        # generate a random y coordinate depending on the window dimensions and width of each car
        rand_y = list(range(int(-SCREEN_HEIGHT / 2) + 45, int(SCREEN_HEIGHT / 2), int(CAR_WIDTH) + CAR_GAP))
        if right_side:
            self.goto(SCREEN_WIDTH / 2, random.choice(rand_y))
            self.setheading(180)    # face to the left side
        else:
            self.goto(-SCREEN_WIDTH / 2, random.choice(rand_y))
            self.setheading(0)  # face to the right side


class CarManager:
    """
    Responsible for managing methods related to car obstacles in the game.

    attributes:
    cars_list (list) - list storing all cars generated in a given game
    """

    def __init__(self):
        self.cars_list = []     # initiate an empty list

    def reset_cars(self):
        """Hides all current cars displayed in the game window and empties the main car list."""
        for car in self.cars_list:
            car.hideturtle()
            car.clear()
        self.cars_list = []

    def generate_cars(self):
        """Spawns a one car on each side of the game window at a random y-coordinate position."""
        right_car, left_car = Car(), Car(right_side=False)
        self.cars_list.extend([right_car, left_car])

    def march_cars(self):
        """
        Moves all generated cars on the screen from one side to the opposite side. Then disappears the car.
        """
        for car in self.cars_list:
            car.forward(random.choice(range(CAR_MOVE_INCREMENT)))
            if abs(car.xcor()) > (SCREEN_WIDTH / 2):
                self.disappear_car(car)

    def disappear_car(self, car_obj):
        """Removes are car from the main ilst and hides it from display in the game window"""
        if car_obj in self.cars_list:
            self.cars_list.remove(car_obj)
            car_obj.hideturtle()
            car_obj.clear()

    def collision(self, player):
        """Detects a collision between the player and a car obstacle through distance measurements."""
        player_width = 20 / 2
        from_below, from_side = (CAR_WIDTH / 2) + player_width / 2, (CAR_LENGTH / 2) + player_width / 2
        for car in self.cars_list:
            if car.distance(player) < from_below or car.distance(player) < from_side:
                return True
        return False

    def hide_half(self):
        """Makes roughly half the generated cars on display disappear as a visual display for end of game. """
        for i in range(len(self.cars_list) // 2):
            self.disappear_car(self.cars_list[i])


class Scoreboard(Turtle):
    """
    Inherits the Turtle class from the turtle module to display text as the scoreboard.

    args:
    current_level (int) - the current level of the game played by the user

    non-inherited attributes:
    level - adds the current level of the game as an attribute for referencing text displays
    """

    def __init__(self, current_level):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color(TEXT_COLOUR)
        self.level = current_level

    def display_level(self):
        """Displays the current level as a text display at the top left of the game window screen."""
        self.clear()
        self.setpos(TEXT_LOCATION)     # top-left position
        self.write(
            f"Level: {self.level}",
            font=FONT
        )

    def increase_level(self):
        """Increases the level attribute of the Scoreboard class by 1."""
        self.level += 1

    def reset_level(self):
        """Resets the current level of the game back to level 1."""
        self.level = 1

    def display_game_over(self):
        """Displays a game over and high score display when the player loses."""
        self.clear()
        self.goto(0, 0)
        self.write(
            "GAME OVER",
            align="center",
            font=("Courier", 30, "bold")
        )
        self.goto(0, -50)
        self.write(
            f"Highest Level: {self.level}",
            align="center",
            font=FONT
        )
