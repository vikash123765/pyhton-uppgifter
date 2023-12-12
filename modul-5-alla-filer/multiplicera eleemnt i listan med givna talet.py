## definera en funktion som lutiplecerar element i en lista med ett givet tal 

def muliply(lst,tal=2):
    ## iteraera lver alla positioner i listan
    for i in range (len(lst)):
        lst[i] *= tal 

list = [23,65,3,67]
new_tal = 5
muliply(list,new_tal)
print(list)

