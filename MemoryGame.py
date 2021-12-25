#!/usr/bin/python3

import random, os, time
from Live import load_game
from Score import add_score

def generate_sequence():
    generate_number = [random.randint(1, 101) for number in range(difficulty_number)]
    print(f'Random number list is : {generate_number}')
    time.sleep(0.7)
    os.system('clear')
    return generate_number

def get_list_from_user():
    get_list = input(f"Please guess the list : ").split()
    int_list = []
    for number in get_list:
        int_list.append(int(number))
    return int_list

def is_list_equal(generate_number, int_list):
    if generate_number == int_list:
        result=True

    else:
        result=False

    return result


if __name__ == '__main__':



 difficulty_number = int(input("Please enter your difficulty: "))
 #print(f'difficulty_number is : {difficulty_number}')
 generate_number = generate_sequence()
 int_list = get_list_from_user()
 result = is_list_equal(generate_number, int_list)
 #print(f"result is :" , result)
 if result == True:
     print("\nYOU WON!\n")
     add_score(difficulty_number)

 elif result == False:
     print("\nYou lost")
     add_score(difficulty_number)

