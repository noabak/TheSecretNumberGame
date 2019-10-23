from game import *

''' The secret number game: The player is supposed to guess a random number between 1 and 30.
    He can get the score list and top scores. '''

while True:
    selection = input("Would you like to A) play a new game, B) see the best scores, or C) quit?")

    if selection.upper() == "A":
      valid = True
      level = input("Please enter the level: H) hard, E) easy:")
      while valid:
        if level.lower() == "h":
          play_game("hard")
          break
        elif level.lower() == "e":
          play_game("easy")
          break
        else:
          print("Invalid caracter!")
          valid=False


    elif selection.upper() == "B":
        print(get_top_scores())
        for score_dict in get_top_scores():
            print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))
    else:
        print("BYE!")
        break

