from time import sleep
import Guess_Game
import MemoryGame


def welcome(name = input("What's your name? ")):
    print("Hello", name, "and welcome to the World of Games (WoG).", "\nHere you can find many cool games to play.")


def check_range(x, y, number):
        while number < x or number > y:
            load_game()


def load_game():
    print("\nPlease choose a game to play: ")
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    print("2. Guess Game - guess a number and see if you chose like the computer")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
    global game_number
    game_number = input("\nEnter a game number here please:)")
    try:
        check_range(1, 3, int(game_number))
    except ValueError as e:
        print("Please enter a number")
        sleep(1)
        load_game()
    print("Good Choice!!")
    print("Please choose game difficulty from 1 to 5:")
    global difficulty_number
    difficulty_number = input()
    try:
        check_range(1, 5, int(difficulty_number))
    except ValueError as e:
        print("Please enter a number")
        sleep(1)
        load_game()
    print("Alright let's begin!!")
    if game_number == "1":
        MemoryGame.play(difficulty_number)
    elif game_number == "2":
        Guess_Game.play(difficulty_number)
    elif game_number == "3":
        print("game-3")
    else:
        print("else")

