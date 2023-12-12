## läs in antal ägg från navändaren gör om till heltal
eggs_from_user = int(input("how many eggs? :"))

# används heltals division för att räkna ut antelt karotnger om en kartong har 6 ägg

number_of_boxes = eggs_from_user // 6

# använd modular division för att räkna ut hur många egg som blir över om äggen totalt är ett omjämnt tal
remainderof_eggs = eggs_from_user % 6  ## hur många egg blir över om vi delar med 6

## skriv ut resulatetet
print(f"{number_of_boxes} karotnger och {remainderof_eggs} ägg över.")
       # hut många egg i 6 pack finns    # hur mpnga eggs utöver 6 packen finns