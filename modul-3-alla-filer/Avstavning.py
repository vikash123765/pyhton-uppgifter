word = input("skriv in ett ord ")

new_word= "" 

for i  in range(len(word)-1): ## ieterete trough all the elemnt -1 will delete the last element +ssymbol 
    new_word += word[i] + "-"  # add the letter and - on i index position 
new_word += word[-1]   ## here -1 is the last element not symbol so we add the last letter  
print(new_word  )    



