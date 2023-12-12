##Skriv en funktion med namnet addera som tar två tal som parametrar. Funktionen ska returnera summan av de två talen. Placera funktionen på ett lämpligt ställe i följande kodruta så att anropet fungerar.
""" 
def addera(a,b):
    return a + b

tal_1 = int(input('Skriv ett tal: '))
tal_2 = int(input('Ett till: '))
summa = addera(tal_1, tal_2)
print(f'Summan av {tal_1} och {tal_2} är {summa}.')
 """
#Följande funktion skriver ut en välkomstfras eller inget alls. Anropa funktionen med olika argument för att testa de två olika alternativen.
""" 
def hälsa_välkommen(namn):
    if namn == '':
        return 
    print(f'Välkommen {namn}!')


passed_name="vikash"
fras=hälsa_välkommen(passed_name)
print(fras)
 """

##Följande funktion räknar ut största och minsta värdena i en lista, .

""" def störst_och_minst(lst):
    största = max(lst)
    minsta = min(lst)
    return största, minsta
    

en_lista = [4, 8, 1, 7, 5]
resultat = störst_och_minst(en_lista)
print(f'Största och minsta värden i listan är {resultat}.') """

## hitta problemet = löst

""" def medelvärde(lst):
    summa = sum(lst)
    n = len(lst)
    return summa / n

mätvärden = input('Mätvärden: ')
lst_data = mätvärden.split()
data = [float(x) for x in lst_data]
mv = medelvärde(data)
print(f'Medelvärdet av de inmatade värdena är {mv}') """

## hitta felet = löst

""" def sänkt_pris(ordinarie_pris, prissänkning_procent):
    return ordinarie_pris * (1 - prissänkning_procent / 100)

orginal_price = float(input('Varans ordinarie pris: '))
price_altering = float(input('Prissänkning i procent: '))
nytt_pris = sänkt_pris(orginal_price,price_altering)
print(f'Det sänkta priset blir {nytt_pris}.')


 """

##Skriv en funktion dividera som kan anropas på följande sätt.

""" def dividera(täljare,nämnare):
    return täljare/nämnare  

print(dividera(6, 3))                  # 6 / 3 = 2
print(dividera(nämnare=2, täljare=8))  # 8 / 2 = 4
print(dividera(10, nämnare=4))         
 """



##Ändra i funktionen så att den kan anropas med endast ett argument. Funktionen ska då returnera kvadratroten ur talet det vill säga den ska använda  n=2 .

""" def roten_ur(x, n=2):  ## la till default värde som 2 
    return x ** (1 / n)

print(roten_ur(2, 2))   # kvadratroten ur 2 är 1.41421...
print(roten_ur(27, 3))  # tredje roten ur 27 är 3
print(roten_ur(4))      # ska returnera kvadratroten ur 4, alltså 2 """

""" 
def summera_positiva(*värden): ## lägg till asterisk 
    summa = 0
    for item in värden:
        if item > 0:
            summa += item
    return summa

print(summera_positiva(2, 5, -3, 1, -2))
print(summera_positiva(-1, 1, -1)) """


##Ändra i följande kod så att utskriften istället ser ut så här: 0 noll * 1 ett * 2 två * 3 tre
""" 
lst = ['noll', 'ett', 'två', 'tre']
for i, num in enumerate(lst):    ## använd enumare för index plus elemnt nman 
    print(f"{i} {num} * ", end="") ## print ondex och eleemnt namn och end="" för unddvika skriva på ny rad """

def nollställ_negativa(lst):
    for i in range (len(lst)):
        if lst[i] < 0:
            lst[i]= 0
      
värden = [4, 0, -3, 5, 1, -1]
nollställ_negativa(värden)
print(värden)                  # [4, 0, 0, 5, 1, 0]

