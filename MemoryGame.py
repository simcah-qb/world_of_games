import random
import os
from time import sleep


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def welcome():
    print("\nWelcome to Memory Game!!")
    print("Here i am going to show you a few numbers for 0.7 seconds and you are gonna need to memories them!!")


def generate_sequence(difficulty):
    global random_number
    global list_from_random
    for number in range(0, int(difficulty)):
        random_number = str(random.randint(1, 101))
        print(random_number)
        list_from_random = list(random_number)
        sleep(0.7)


def get_list_from_user():
    global the_list
    global guess_number
    print("Please enter the numbers you remember: ")
    guess_number = input()
    list_of_user = list(guess_number)
    if list_of_user == list_from_random:
        print("You won!!")
    else:
        print(list_of_user, list_from_random)


def play(difficulty):
    clear()
    welcome()
    generate_sequence(difficulty)
    clear()
    print("Your time ended!!")
    get_list_from_user()
