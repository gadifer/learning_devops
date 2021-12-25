#!/usr/bin/python3

def welcome():
    name = input("Pease Enter Your Name: ")
    print(f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.\n")


def load_game():
    print (f"1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.\n2. Guess Game - guess a number and see if you chose like the computer.\n3. Currency Roulette - try and guess the value of a random amount of USD in ILS.\n ")

    while True:
        num = input("Please choose Your Game number: ")

        if num == "1":
            print(f"You have selected {num} Memory Game\n")

            break
        elif num == "2":
            print(f"You have selected {num} Guess Game\n")
            break
        elif num == "3":
            print(f"You have selected {num} Currency Roulette\n")
            break

    while True:
        ##global level
        level = input("Please Enter Your difficulty level Game: ")
        if level in ["1", "2", "3", "4", "5"]:
            print(f"You have selected difficulty level Game {level} ")
            break
        else:
            print(f"You have selected wrong difficulty level Game {level} ")


if __name__ == '__main__':

    welcome()
    load_game()
