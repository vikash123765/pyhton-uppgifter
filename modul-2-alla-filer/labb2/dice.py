import random


counter = 0
while True:
    dice_throw =random.randint(1,6)
    if dice_throw < 6:
        counter += 1
        print(f"{dice_throw}")
    if dice_throw == 6:
        print(f"{dice_throw}\nDet tog {counter+1} kast att få en 6:a.")
        break

