user_input= input("skriv in valfri order eller mening")  ## input frå nanvändaren
vokaler = "aouåeiyäö"  # sparar alla vokaleer i en variabel

for bokstav in user_input: ## itererar varje bokstav i user input  
    if bokstav.lower in vokaler: ##ifall bokstaver i user inut är vokalerer. is lower omvandlar stora A tll litet a 
        print("*", end="")  ## printa istället asterisk 
    else:
        print(bokstav,end="")     # annars  printa som vanligt bokstäverna
print()        