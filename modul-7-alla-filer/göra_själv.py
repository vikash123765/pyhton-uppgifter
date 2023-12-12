##
""" 
def addera_värden(numbers):
    tota=sum(numbers.values())
    return tota



d = {'a': 2, 'o': 7, 'u': 10, 'å': 5, 'e': 2, 'i': 1, 'y': 9, 'ä': 6, 'ö': 3}
summa = addera_värden(d)
print(summa)
                       # 45 """



""" 
def högst_värde(winners):
    highest_value= max(winners.keys())
    return highest_value

d = {'Nisse': 43, 'Birger': 21, 'MÅG': 35, 'Frida': 12, 'Folk': 20}
vinnare = högst_värde(d)
print(f'Vinnare är {vinnare} med {d[vinnare]} röster.')  # Nisse, 43
 """


def filtrera(num, limit):
    result={}
   
    for key in num: 
        värde= num[key]
        if värde > limit:
               result[key] = värde
           
    return result


d = {'Nisse': 43, 'Birger': 21, 'MÅG': 35, 'Frida': 12, 'Folk': 20}
eliten = filtrera(d, 30)
print(eliten)               # {'Nisse': 43, 'MÅG': 35}