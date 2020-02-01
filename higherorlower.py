import time

lookedaway = 0
temp = 10000
lives = 10
allowhighorlow = 10
goback = 10000

while temp > 0:
  print("")
  temp -= 1

print("Welcome to higher or lower!")
time.sleep(2)
print("This amazing version was created by Sebastian Webster, and put into his arcade on the 1st of February 2020")
time.sleep(5)
print("Now, lets go back to the game!")
time.sleep(1)
temp = 100
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

while (allowhighorlow > 1) or (allowhighorlow < 0):
 allowhighorlow = int(input("Do you want the game to give the other player Higher or Lower hints? 0 = No 1 = Yes"))
 if (allowhighorlow > 1) or (allowhighorlow < 0):
   print("Please answer with 0 or 1.")
   time.sleep(2)
   temp = 100
   while temp > 0:
     print("")
     temp -= 1
temp = 100 
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
numberattempt = guessnumber + 1
while (numberattempt != guessnumber) and (lives != 0):
 numberattempt = int(input("Player 2, what do you think the number is?"))
 if numberattempt == guessnumber:
   print("Congratulations you won with")
   print(lives)
   print("lives left, well done!")
 elif allowhighorlow == 1:
   if numberattempt > guessnumber:
     print("Lower!")
     print("You have")
     print(lives)
     print("lives left.")
     lives -= 1
   else:
     if numberattempt < guessnumber:
       print("Higher!")
       print("You have")
       print(lives)
       print("lives left.")
       lives -= 1
 elif allowhighorlow == 0:
   print("Wrong!")
   print("You have")
   print(lives)
   print("lives left.")
   lives -= 1
 else:
   print("You have ran out of lives. Game over!")
   time.sleep(1)
   print("The actual numnber was...")
   time.sleep(1)
   print(guessnumber)

while (goback < 0) or (goback > 1):
  goback = int(input("Do you want to go back to the Arcade menu? 0. No 1. Yes"))
  if (goback < 0) or (goback > 1):
    print("Please only use 0 or 1.")

if goback == 0:
  print("Ok, goddbye! We hope to see you soon at...")
  time.sleep(1)
  print("Sebastian's Arcade!")
else:
  print("Taking you back to the arcade screen...")
  time.sleep(1)
  temp = 50
  while temp > 0:
   print("")
   temp -= 1
  import main



