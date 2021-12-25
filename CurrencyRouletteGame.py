import random
import requests
res = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
res = res.json()
rate_ils = res.get("rates").get("ILS")
#print(rate_ils)


def get_money_interval():
    t = (random.randint(1, 100))
    print(t)
    return t

def get_guess_from_user(d,t):
    my_value = int(input("Please guess Your Value in Shekel: "))
    print(my_value)
    value_interval = (t - (5 - d)) * rate_ils, (t + (5 - d)) * rate_ils
    print(value_interval)
    if my_value > value_interval[0] and my_value < value_interval[1]:
        print("You Won")
    else:
        print("you lost")

def play():
    d = int(input("Please choose Your difficulty Level between 1-5 : "))
    t = get_money_interval()
    get_guess_from_user(d, t)

     # MAIN #


if __name__ == "__main__":
    play()

