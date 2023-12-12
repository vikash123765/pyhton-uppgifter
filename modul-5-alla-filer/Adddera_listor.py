## definera en funktion som adderar lika långa listor element vis 
def add_lists(ls1,lst2):
    ## skapa tom lista för att lagra resulatatet
    res=[]
    ## iteraera över all positioner i listan 
    for i  in range (len(ls1)):
        res.append(ls1[i]+lst2[i])
    return res

l1 = [32,70,87,98]
l2 = [34,76,987,998]
new_list= add_lists(l1,l2)
print(new_list)


## addera 2 tal från 2 listor element vis  i en lista och kapa en ny lista 