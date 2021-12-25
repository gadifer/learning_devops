import random

def generate_number():

   difficulty=int(input("Please choose game highest difficulty level:  "))
   print(f"difficulty is", difficulty)
   secret_number =(random.randint(0, difficulty))
   print(secret_number)
   return secret_number

def get_guess_from_user():

   myguess=int(input("Please guess your secret number:  "))
   print(f"you guessed {myguess} ")
   return myguess

def compare_results(secret_number, myguess):
  if myguess == secret_number:
     result=True
  else:
     result=False
  return result

def play():
  secret_number = generate_number()
  myguess = get_guess_from_user()
  result = compare_results(secret_number, myguess)
  if result == True:
     print("\nYou won")
  elif result == False:
     print("\nYou lost")


          # MAIN #


if __name__ == "__main__":

   play()