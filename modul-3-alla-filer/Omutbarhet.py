""" ord = input("Skriv ett ord: ")
for bokstav in ord:
    if bokstav in "aouåeiyäö":
        bokstav = bokstav.upper()
    else:
        bokstav = bokstav.lower()
print(ord)             """


ord = input("Skriv ett ord: ")

nytt_ord = ""   ## måse skapa ny tom sträng och addera till den och till slut prita 

for bokstav in ord:
    if bokstav in "aouåeiyäö":
        nytt_ord += bokstav.upper()
    else:
        nytt_ord += bokstav.lower()
print(nytt_ord) 


