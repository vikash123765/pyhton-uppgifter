## will print elemtnts unordered

""" frukt = {'drakfrukt', 'litchi', 'papaya', 'granatäpple'}
frukt.add('guava')
print(frukt) """

##Alla vokaler (aouåeiyäö) i ordet ord ska läggas till som de är i den nya strängen översättning. Alla konsonanter (alla andra bokstäver) ska läggas till dubbelt med ett 'o' emellan.

""" def rövarspråk(ord):
    vokaler = frozenset('aouåeiyäö')
    översättning = ''
    for bokstav in ord:
        if bokstav not in vokaler:
            översättning += bokstav + "o" + bokstav
    else:
        översättning += bokstav
   
    return översättning

  
svenskt_ord = input('Skriv ett ord: ')
översatt_ord = rövarspråk(svenskt_ord)
print(f'På rövarspråket blir det {översatt_ord}.') """



""" 
def lektion(students):
    for student in students:
        if student not in närvarande and student not in ledig and student not in sjuk:
            print(f"{student} har ogiligt frånvaro")
        elif student in ledig or sjuk:
            print(f"{student} har gilig frånvaro")

elever = {'Ali', 'Bo', 'Carl', 'David', 'Emma', 'Frida'}
närvarande = {'Carl', 'David'}
ledig = {'Ali', 'Emma'}
sjuk = {'Frida'}

lektion(elever) """



""" def scrabble(ord):
    alfabetet = 'abcdefghijklmnoprstuvxyzåäö'
    poäng = [1, 4, 8, 1, 1, 3, 2, 2, 1, 7, 2, 1, 2, 1, 2, 4, 1, 1, 1, 4, 3, 8, 7, 10, 4, 3, 3]
    poängtabell = dict(zip(alfabetet, poäng))
    total = 0
    for bokstav in ord:
        if bokstav in poängtabell:
            total += poängtabell[bokstav]
        else:
            print(f"{bokstav} är inte tillåten i scrabble ch kommer ignoreras")    
    return total

användarord = input('Skriv ett ord: ')
ordpoäng = scrabble(användarord)
print(f'Din ordpoäng är {ordpoäng}.') """




def räkna_röster(röst_lista):
    resultat = {}
    for röst in röst_lista:
        resultat.setdefault(röst, 0)
        resultat[röst] += 1
    return resultat

data = input('Skriv in avgivna röster: ')
avgivna_röster = data.split()
sammanställning = räkna_röster(avgivna_röster)
for kandidat in sammanställning:
    print(f'{kandidat}: {sammanställning[kandidat]} röster')