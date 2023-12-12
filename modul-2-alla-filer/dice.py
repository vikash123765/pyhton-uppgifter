import random


counter = 0
while True:
    input("tryck enter för att kasta tärning")
    dice_throw =random.randint(1,6)
    if dice_throw < 6:
        counter += 1
        print(f"{dice_throw}försök igen")
   
    if dice_throw == 6:
       print(f"det tog {counter+1} kast för att få en 6:a")
       break
