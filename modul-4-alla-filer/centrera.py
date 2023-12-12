##Skapa en lista och räkna ut medelvärdet av elementen. Subtrahera medelvärdet från vart och ett av listans element.
list =  [12,34,56,78,90]

avg = sum(list)/ len(list)  ## clalcuate avg value 

for i in range (len(list)):  ## iterate trough indexes
    list[i] -= avg   ## minus the avg value on each index
print(list)  ## print the new vaues in list 
