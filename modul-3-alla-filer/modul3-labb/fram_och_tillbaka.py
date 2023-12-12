
ord = input("Ange ett ord: ")

for i in range(len(ord)):
    print(f"{ord[i]} - {ord[-i - 1]}")  ## last element minus one index position until 0 element 

