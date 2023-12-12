##Läs in ett antal heltal från användaren till en lista. Skapa en ny lista som innehåller alla jämna tal från den ursprungliga listan.

user_input = input("skriv ett serie tal").split()

## list comprehension for loop för att  göra om listans elemtn till strängar 

heltal = [int(tal) for tal in user_input]  ## ta alla tal från user input och lägg till i int listan

jömna_tal = []

for tal in heltal:  ## iterera över varje heltal i listan
    if tal % 2 ==0:  ## ifall resten är 0 då addera till jömna tal listan
        jömna_tal.append(tal)
print(jömna_tal)        
