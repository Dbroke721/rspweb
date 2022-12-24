from django.shortcuts import render
from . import models
import random
import rsp

context = {
    'player_score': 0,
    'computer_score': 0,
    }


def homeView(request):
  result = 'Start'
  context['logs'] = ''
  if request.POST:
    if request.POST['action'] == 'ROCK_ACTION':
      context['left_gesture'] = 'img/HumanRock.png'
      logs = models.BattleLog()
      computer_choice = random.randint(1, 3)
      winner, gesture, result = rsp.battle(computer_choice, rsp.ROCK_ACTION)
      if winner == 1:
        context['player_score'] += 1
        context['right_gesture'] = 'img/RobotScissors.png'
      elif winner == 2:
        context['computer_score'] += 1
        context['right_gesture'] = 'img/RobotPaper.png'
      else:
        context['right_gesture'] = 'img/RobotRock.png'
      logs.winner = winner
      logs.gesture = gesture
      logs.save()

    if request.POST['action'] == 'SCISSORS_ACTION':
      context['left_gesture'] = 'img/HumanScissors.png'
      logs = models.BattleLog()
      computer_choice = random.randint(1, 3)
      winner, gesture, result = rsp.battle(computer_choice, rsp.SCISSORS_ACTION)
      if winner == 1:
        context['player_score'] += 1
        context['right_gesture'] = 'img/RobotPaper.png'
      elif winner == 2:
        context['computer_score'] += 1
        context['right_gesture'] = 'img/RobotRock.png'
      else:
        context['right_gesture'] = 'img/RobotScissors.png'
      logs.winner = winner
      logs.gesture = gesture
      logs.save()

    if request.POST['action'] == 'PAPER_ACTION':
      context['left_gesture'] = 'img/HumanPaper.png'
      logs = models.BattleLog()
      computer_choice = random.randint(1, 3)
      winner, gesture, result = rsp.battle(computer_choice, rsp.PAPER_ACTION)
      if winner == 1:
        context['right_gesture'] = 'img/RobotRock.png'
        context['player_score'] += 1
      elif winner == 2:
        context['right_gesture'] = 'img/RobotScissors.png'
        context['computer_score'] += 1
      else:
        context['right_gesture'] = 'img/RobotPaper.png'
      logs.winner = winner
      logs.gesture = gesture
      logs.save()

  context['result'] = result  
  logs = models.BattleLog.objects.all()
  for log in logs:
    context['logs'] += f'(Winner: {log.winner}, Gesture: {log.gesture}) \n'

  return render(request, 'base/home.html', context)
