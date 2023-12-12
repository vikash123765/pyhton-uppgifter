## definera funktion som beräknar variations bredeen

def variationsbredd(lst):
    return max(lst)-min(lst)

my_lst= (12,34,6,678,554,89)
distance=variationsbredd(my_lst)
print( distance)
    