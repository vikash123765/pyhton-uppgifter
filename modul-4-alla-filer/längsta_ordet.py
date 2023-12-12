##Läs in ett antal ord från användaren till en lista och skriv ut det längsta ordet i listan.



user_words= input("skriv ett par ord").split()  ## lista av strängar 

longest = ""  ## toma variabel där vi ska sotra det längsta rd 

for ett_ord in user_words:
  if  len(ett_ord) > len(longest):  ## om ordet är längre än längsta då print that om inte kolla vidare 
    ## addera det öängsta ordet till variable longest
    longest = ett_ord
print(longest)
