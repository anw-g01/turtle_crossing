from gameplay import Game
import random


def main():
    game = Game()

    while True:
        while True:
            game.configure_controls()       # listens for user input events
            game.scoreboard.display_level()     # display current level

            rand_num = random.randint(1, game.spawn_frequency)  # generate random number for spawning probability
            if rand_num == 1:
                game.car_manager.generate_cars()    # generate cars both ways

            game.car_manager.march_cars()       # move cars from one side to the other
            game.update_screen()                # update the frame of animation

            if game.game_over():    # detect any collision, if so game over
                break
            game.next_level()     # if finish line reached, start next level

        if not game.play_again():   # prompt user to play again
            break
        else:
            game.reset_game()   # reset all game settings: level, positions, car obstacles etc.
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
