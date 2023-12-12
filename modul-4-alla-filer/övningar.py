

##Komplettera följande kod genom att anropa de funktioner och operatorer som behövs.

""" lst = [41, 39, 26, 32, 40, 46, 51, 37]

först =lst[0]

sist = lst[-1]

minst = min(lst)

max = max(lst)

sum = sum(lst)

antal =len(lst)

print(först, sist, minst, max, sum, antal) """
""" 
tpl = (41, 39, 26, 32, 40, 46, 51, 37)   ## tuple

först =tpl[0]

sist = tpl[-1]

minst = min(tpl)

max = max(tpl)

sum = sum(tpl)

antal =len(tpl)
print(först, sist, minst, max, sum, antal) """



""" lst = [3, 0, -2, 1, 1, -1, -2, 3, 2, 3, 0]
for item in lst:
    if item > 0:
        print(item, end=" ")
print() """

""" tpl = (6, 4, 3, 6, 1, -2)
summan = 0
for item in tpl:
    summan = sum(tpl)
print(summan) """


""" lst = [3, 0, -2, 1, 1, -1, -2, 3, 2, 3, 0]
for i in range(len(lst)):
    if lst[i] < 0:
        lst[i] = 0
  # om det aktuella elementet är negativt:
    # sätt elementet till 0
print(lst) """

""" exakta_värden = [14.32, 13.5, 15.11, 14.89, 15.7, 13.1]
arundade= [round(x) for x in exakta_värden]
print(arundade) """

""" mätvärden = input('Mätvärden: ')
lst_data = mätvärden.split(" ")

data= [float(x) for x in lst_data ]

summa =sum(data)
print(f"summan av v värderna är {summa}")
 """

""" data = (3, 1, 4, 3, 2, 2, 1)
result= 1

for num in data:
    result = result * num
print(result)     """


user_data = input('Ange värden: ') # 7 3 -5 0 2 -1 8 -3

input= user_data.split(" ")

numbers= [int(x) for x in input if int(x) > 0 ]

for num in numbers:
    
       print(num,end =" ")
print()       