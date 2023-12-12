

##Felsignaler 

""" def division(täljare, nämnare):
    assert nämnare != 0, 'kan inte dividera med 0'
    return täljare / nämnare


tälj,nämn= 12,0
res= division(tälj,nämn)
print(res)


def dela_med(täljare,nämnare):
    if nämnare == 0:
        raise ZeroDivisionError('kan inte dividera med 0')
    return täljare / nämnare
tälj,nämn= 12,0
res= dela_med(tälj,nämn)
print(res) """



## Felhantering
""" while True:
    try:
        tal= float(input("ange ett tal"))
        break
    except ValueError:
        print("inte ett tal ")
 """

def addListElements(ls1,ls2):
    try:
        assert len(ls1) == len(ls2),"list are equal legnht"
        new_list=[]
        for i in range (len(ls1)):
             new_list.append(ls1[i] + ls2[i])
        return new_list
    except AssertionError as e:
        print(e)
       



lst1 = [1, 1, 2, 2, 3, 5,3,4]
lst2 = [0, 1, 2, 3, 4, 5]
summa = addListElements(lst1, lst2)
print(summa)
    


