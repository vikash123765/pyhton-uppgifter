import math
import random
#Skriv ett program som väljer ett slumptal mellan 1 och 20. Låt användaren gissa vilket talet är. Ange för varje felaktig gissning 
#om det är för högt eller för lågt. Fortsätt ända tills användaren gissat rätt.

random_num = random.randint(1,10)



while True:
    gussed_num= int(input("gissa talet jag tänker på ! "))
    if  random_num == gussed_num:
        print("you guessed the right numher")
        break
    elif gussed_num > random_num:
        print("gueesed number is higher then the nuber im thinking")    
    elif gussed_num < random_num:
        print("gueesed number is lower then nuber im thinking")

    