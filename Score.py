#!/usr/bin/python3

from Utils import SCORES_FILE_NAME, BAD_RETURN_CODE


def add_score(difficulty_number):
    with open(SCORES_FILE_NAME,"r") as file:
        scorenow = int(file.read())
        print(f"your score now is" , int(scorenow))
        file.close()
        win_points = (difficulty_number * 3) + 5
        new_score = scorenow + win_points
        print(f"New Score is" , int(new_score))
        with open(SCORES_FILE_NAME,"w") as f:
         f.write(str(new_score))
         f.close()


if __name__ == '__main__':

    add_score()
