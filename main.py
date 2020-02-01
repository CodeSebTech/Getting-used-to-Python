import time
gamechooser = 0


while (gamechooser < 1) or (gamechooser > 1):
  print("Welcome to Sebastian's Awesome Game Arcade!")
  time.sleep(1)
  gamechooser = int(input("What game would you like to play? 1. Higher or Lower"))
  if gamechooser < 1:
   print("Please try again, do not make it less than 1.")
  if gamechooser > 2:
   print("Please make the number smaller, we do not have than many games.")

if gamechooser == 1:
  import higherorlower

