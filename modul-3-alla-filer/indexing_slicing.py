ord = input("skriv ett ord: ")
första = ord[0]
fjärde = ord[3]
sista = ord[-1]
 
baklänges = ""
for i in range(len(ord)):
        baklänges += ord[-i -1]
      

print(f"ordet börjar på {första} och slutar på {sista}")
print(f"ordets fjärde bokstav {fjärde}")
print(f"Baklänges blir det {baklänges}")