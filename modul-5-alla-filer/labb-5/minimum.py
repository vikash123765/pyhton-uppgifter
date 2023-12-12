def set_min_value(lst,min):  ## 2 parameters that accept 2 arguments 
    for num in range (len(lst)): ## iterating trough the indexes in lst
        if lst[num]< min:  ## if current index element is less then min value 
            lst[num] = min ## update that elemnt with min value 


lst = [8, 9, 13, 6, 5]
set_min_value(lst, 1)
print(lst)