# läs in namn från användaren 
namn = input("vad är ditt namn (förnamn och efternamn): ? ")

##Hitta första mellanslag
position= namn.find(" ")
print(position)

#Plocka ut en del av ens träng och starta efter mellanslag därför +1
efternamn = namn[position +1:]
print(efternamn)

print(f"the mame is {efternamn}, {namn}")
