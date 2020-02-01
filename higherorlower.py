import time

lookedaway = 0
temp = 10000

while temp > 0:
  print("")
  temp -= 1
highguess = int(input("Player 2, what do you want the highest possible number to be?"))
minguess = highguess + 1
guessnumber = highguess * 99
temp = 100
while temp > 0:
  print("")
  temp -= 1

while minguess > highguess:
  minguess = int(input("Player 2, what do you want the smallest possible number to be?"))
  if minguess > highguess:
    print("Please change your answer, and make it smaller than the highest number.")
    time.sleep(1)
temp = 100
while temp > 0:
  print("")
  temp -= 1

print("Player 2, NOW DO NOT LOOK!")
time.sleep(3)
temp = 100
while temp > 0:
  print("")
  temp -= 1

while (lookedaway < 1) or (lookedaway > 1):
 lookedaway = int(input("Has player 2 looked away yet? 0. No 1. Yes"))
 if (lookedaway < 1) or (lookedaway > 1):
   print("LOOK AWAY PLAYER 2!!")
   time.sleep(3)
   temp = 100
   while temp > 0:
     print("")
     temp -= 1
temp = 100
while temp > 0:
  print("")
  temp -= 1

while (guessnumber > highguess) or (guessnumber < minguess):
 print("Min is")
 print(minguess)
 print("Max is")
 print(highguess)
 guessnumber = int(input("What do you want the guessing number to be?"))
 if (guessnumber > highguess) or (guessnumber < minguess):
   print("Make it in between Player 2's requests please.")
   time.sleep(2)
   temp = 100
   while temp > 0:
     print("")
     temp -= 1
temp = 10000
while temp > 0:
  print("")
  temp -= 1

print("Player 1, tell Player 2 he/she can look now!")
time.sleep(3)
temp = 50
while temp > 0:
  print("")
  temp -= 1
print("Game starting in 5...")
time.sleep(1)
temp = 50
while temp > 0:
  print("")
  temp -= 1
print("Game starting in 4...")
time.sleep(1)
temp = 50
while temp > 0:
  print("")
  temp -= 1
print("Game starting in 3...")
time.sleep(1)
temp = 50
while temp > 0:
  print("")
  temp -= 1
print("Game starting in 2...")
time.sleep(1)
temp = 50
while temp > 0:
  print("")
  temp -= 1
print("Game starting in 1...")
time.sleep(1)
temp = 50
while temp > 0:
  print("")
  temp -= 1
print("Go!!!")
time.sleep(1)
temp = 50
while temp > 0:
  print("")
  temp -= 1


