def arg_min(lst):
    if not lst:
        raise ValueError("Listan kan inte vara tom")
    
    min_val=lst[0]
    min_index= 0

    for i in range (len(lst)):
        if lst[i] < min_val:
            min_val=lst[i]
            min_index=i
    return min_index        



def find_all_positions(lst,value):
    pos=[]
    for i in range (len(lst)):
        if lst[i] == value:
            pos.append(i)
    return pos        

values = []
positions = find_all_positions(values, 5)  # []
print(positions)