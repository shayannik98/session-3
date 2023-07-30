print("welcome to your game:")
print("select option :\n 1) start  \n2) end ")
choice = input("your choose is : ")
import random

while True:
   if choice=="1":
      roll = random.randint(1,6)
      print("Dice Roll Result: " , roll)
      if roll==6:
         print("good luck, you have gift")
         gift = random.randint(1,6)
         print("gift result: " , gift)
      else:
         break
      
   if choice=="2":
      break
   else:
      print("invalid choise")
      
      

    