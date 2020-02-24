import random


def welcome():
    print("Welcome to Guess Game!!")


def generate_number(difficulty):
    global secret_number
    secret_number = random.randint(1, int(difficulty))


def get_guess_from_user(difficulty):
    global guess
    print("\nOK i picked a number from 1 to " + difficulty)
    guess = input("Please enter your guess number here:")


def compare_results(x, y):
    if x == y:
        print("True")
    else:
        print("False")


def play(difficulty):
    welcome()
    generate_number(difficulty)
    get_guess_from_user(difficulty)
    compare_results(secret_number, guess)
