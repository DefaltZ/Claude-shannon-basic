
import numpy as np
import random
import os

last = second_last = 0
player_score = computer_score = 0

inputs = np.zeros((2, 2, 2), dtype = int)

def update_inputs(player_input):
  global last, second_last 
  if inputs[second_last][last][0] == player_input:
    inputs[second_last][last][1] = 1
    inputs[second_last][last][0] = player_input

  else:
    inputs[second_last][last][1] = 0
    inputs[second_last][last][0] = player_input

  second_last = last
  last = player_input 

def prediction():
  if inputs[second_last][last][1] == 1:
    predict = inputs[second_last][last][0]

  else:
    predict = random.randint(0, 1)

  return predict 

def update_scores(player_input, predict):
  global player_score, computer_score

  if predict == player_input:
      computer_score = computer_score + 1
      print("computer got a point")
      print("computer score =", computer_score)
      print("player score =", player_score)

  else:
     player_score = player_score + 1
     print("player got a point")
     print("computer score =", computer_score)
     print("player score =", player_score)

def gameplay(): 
  inputs_list = ["0", "1"]
  while True:
    player_input = input("Enter a value between 0 and 1: ")
    while player_input not in inputs_list:
      print("invalid input")
      player_input = input("Enter a value between 0 and 1: ")

    player_input = int(player_input)
    predict = prediction()
    update_inputs(player_input)
    update_scores(player_input, predict)

    if player_input == 10:
      print("player won the game")
      break

    elif computer_score == 10:
      print("computer won the game")
      break
     


gameplay()


