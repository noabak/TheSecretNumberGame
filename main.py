import random
import json
import datetime

secret= random.randint(1,5)
guess=0
attempts=0
list_wrong_guesses=[]

player = input("Please enter your name:")

with open("score_list.txt","r") as score_file:
  a=score_file.read()
  score_list = json.loads(a)
  print("Top score:" + str(score_list[:3])) # PRINT ONLY THE FIRST THREE ELEMENTS

while guess!=secret:
  guess = int(input("Please enter a number:"))
  attempts += 1

  if guess == secret:
    print("**** CONGRATULATIONS! *** You guessed it!")
    #score_list.append(attempts)
    current_time = datetime.datetime.now()  # datetime --> FECHA Y HORA
    # add player name, secret number and wrong guesses keys
    score_data = {"Player name": player, "Secret number": secret,"attempts": attempts, "date":str(current_time), "List wrong guesses": list_wrong_guesses}
    score_list.append(score_data)
    print(attempts," : ",current_time)

    sorted_list = sorted(score_list, key=lambda k: k['attempts']) # SORT LIST PER ATTEMPTS
    print(sorted_list[:3])
    with open("score_list.txt", "w") as score_file:
      b= json.dumps(score_list)
      score_file.write(b)
    break  # ponemos BREAK para salir del bucle una vez acertado el numero

  elif guess>secret:
    list_wrong_guesses.append(guess)
    print("Try something smaller")
  elif guess<secret:
    list_wrong_guesses.append(guess)
    print("Try something bigger")

