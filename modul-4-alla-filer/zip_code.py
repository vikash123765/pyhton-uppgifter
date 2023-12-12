##Läs in en amerikansk zip code och skriv ut varje siffra med bokstäver.


user_input = input("Zip code: ")

numbers = ["zero","one","two","three","four","five","six","seven","eight","nine","ten"]

for tecken in user_input:
    n = int(tecken)
    digit = numbers[n]
    print(digit, end= " ")
print()    