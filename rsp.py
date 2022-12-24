ROCK_ACTION = 1
SCISSORS_ACTION = 2
PAPER_ACTION = 3

counter = 0

def battle(computer_choice, player_choice):
    global counter
    result = 'Error'
    winner = 0
    if computer_choice == player_choice:
      if computer_choice == ROCK_ACTION:
        gesture = 'rock'
      elif computer_choice == SCISSORS_ACTION:
        gesture = 'scissors'
      else:
        gesture = 'paper'
      result = 'Ничья!'
    elif computer_choice == ROCK_ACTION:
        if player_choice == SCISSORS_ACTION:
            result = 'Поражение!'
            winner = 2
            gesture = 'rock'
        else:
            result = 'Победа!'
            winner = 1
            gesture = 'paper'
    elif computer_choice == SCISSORS_ACTION:
        if player_choice == ROCK_ACTION:
            result = 'Победа!'
            winner = 1
            gesture = 'rock'
        else:
            result = 'Поражение!'
            winner = 2
            gesture = 'scissors'
    elif computer_choice == PAPER_ACTION:
        if player_choice == SCISSORS_ACTION:
            result = 'Победа!'
            winner = 1
            gesture = 'scissors'
        else:
            result = 'Поражение!'
            winner = 2
            gesture = 'paper'
    return winner, gesture, result

