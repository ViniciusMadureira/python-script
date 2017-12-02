### -*- coding: utf-8 -*-
__author__="Vinícius Silva Madureira Pereira <viniciusmadureira@outlook.com"
__date__="$Feb 2, 2017 6:33:19 AM$"

import random

# Main mathematical function of the algorithm: ƒ(n, m) = mⁿ
def player_value(n, m):
  return m ** n
  
def winner(player1, player2):
  if player1 == player2:
    return 'None'
  p1 = player_value(player1, player2)
  p2 = player_value(player2, player1)
  return get_element(player1) if p1 > p2 else get_element(player2)
  
def get_element(player_value):
  return [key for key, value in elements.items() if value == player_value][0]

elements = {'rock': 2, 'paper': 1, 'scissors': -2}

# Test
for index in range(11):
  player1= random.choice(list(elements.items()))[0]
  player2= random.choice(list(elements.items()))[0]
  print(player1.capitalize() + " vs. " + player2.capitalize() + ": " + winner(elements[player1], elements[player2]).capitalize())
