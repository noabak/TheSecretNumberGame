import random
import json
import datetime


def play_game():

 secret= random.randint(1,5)
 guess=0
 attempts=0
 list_wrong_guesses=[]

 player = input("Please enter your name:")
 with open("score_list.txt","r") as score_file:
  a=score_file.read()
  score_list = json.loads(a)
  # PRINT ONLY THE FIRST THREE ELEMENTS
  #print("Top score:" + str(score_list[:3]))

 while guess!=secret:
  guess = int(input("Please enter a number:"))
  attempts += 1

  if guess == secret:
    print("**** CONGRATULATIONS! *** You guessed it!")
    #score_list.append(attempts)
    current_time = datetime.datetime.now()
    # add player name, secret number and wrong guesses keys
    score_data = {"Player name": player, "Secret number": secret,"attempts": attempts, "date":str(current_time), "List wrong guesses": list_wrong_guesses}
    score_list.append(score_data)
    print("Nº ATTEMPTS: ",attempts," : ",current_time)

    with open("score_list.txt", "w") as score_file:
      b= json.dumps(score_list)
      score_file.write(b)
    break

  elif guess>secret:
    list_wrong_guesses.append(guess)
    print("Try something smaller")
  elif guess<secret:
    list_wrong_guesses.append(guess)
    print("Try something bigger")

def get_top_scores():
    with open("score_list.txt", "r") as score_file:
        a = score_file.read()
        score_list = json.loads(a)
        # SORT LIST PER ATTEMPTS
        sorted_list = sorted(score_list, key=lambda k: k['attempts'])
        return sorted_list[:3]
