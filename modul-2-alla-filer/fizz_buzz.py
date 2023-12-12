#FizzBuzz är ett spel som används för att träna barn i division. Man sitter i en ring och räknar, i tur och ordning. Varje tal som är delbart med 3 ska bytas ut mot *Fizz* och varje tal som är delbart med fem ska bytas ut mot *Buzz*. Ett tal som är delbart med både 3 och 5 ska bytas ut mot *FizzBuzz*.
#Räknar vi från 1 börjar ramsan så här:
#`1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16, ...`
#*   Läs in ett tal från användaren och låt programmet räkna från 1 till det givna talet enligt reglerna ovan. Talen eller orden ska skrivas ut på skärmen, ett på varje rad.

tal = int(input("hur långt vill du räkna ?" ))

for i in range(1,tal+1):
    if i % 3 == 0 and i % 5 == 0:
       print("fizzbuzz,",end=" ")
    elif i % 3 == 0:
        print("fizz,", end=" ")
    elif i % 5 == 0:
        print("buzz,", end=" ")
    else:
        print(i, end=", ")        

        
