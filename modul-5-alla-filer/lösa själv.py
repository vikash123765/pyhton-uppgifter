##Skriv en funktion som tar en sträng och returnerar samma sträng men med asterisker mellan varje bokstav.
## skriv om ordet så output bli k*a*n*o*n
""" def med_eftertryck(ord):
    new_word= "" 
    for item in ord:
        new_word = new_word+ item + "*"
    return new_word[:-1]
 """

""" ett_ord = 'kanon'
nytt_ord = med_eftertryck(ett_ord)
print(nytt_ord)                        # k*a*n*o*n
annat_ord = 'perfekt'
nyare_ord = med_eftertryck(annat_ord)  # p*e*r*f*e*k*t
print(nyare_ord) """

## aderar element vis och stora i en tom lista res som du senare reutrneerar

""" def addera_elementvis(l1,l2):
    new_list= []
    for i in range (len(l1)):
        new_list.append(l1[i] + l2[i])
    return new_list

lst1 = [1, 1, 2, 2, 3, 3]
lst2 = [0, 1, 2, 3, 4, 5]
summa = addera_elementvis(lst1, lst2)
print(summa)                           # [1, 2, 4, 5, 7, 8]
L1 = [1, 1, 1, 4, 4]
L2 = [3, 5, 6, 0, -1]
total = addera_elementvis(L1, L2)
print(total)                           # [4, 6, 7, 4, 3]
 """
def multiplicera(a,b=2):
    for i in range (len(a)):
        a[i] *= b


värden = [1, 3, 2, 1, 4, 0]
multiplicera(värden,8)        # Multiplicera med 8
print(värden)                  # [8, 24, 16, 8, 32, 0]

tal = [9, 2, 12, 4, -2]
multiplicera(tal)              # Multiplicera med 2
print(tal)                     # [18, 4, 24, 8, -4]     