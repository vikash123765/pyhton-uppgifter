#Val handlar om att låta programmet ta olika vägar, exempelvis beroende på vilket värde en variabel har. Vi har sett if-satsen, vilket är den vanligaste konstruktionen för att göra val.
#Följande exempel kontrollerar om en beökare på Liseberg är tillräckligt lång för att få åka Radiobilarna. Kör koden och se om du får åka!'

""" print("välkommen till liseberg")
längd = int(input("hur lång är du"))
if längd >=130:
    print("du får åka")
else:
    print("du är för kort tyär")
 """

 #För att få åka Lisebergbanan behöver man vara minst 130 cm *eller* 110 cm i vuxens sällskap.Komplettera koden så att tre olika meddelanden ges, beroende på användarens längd.

""" print("välkommen till liseberg")
längd = int(input("hur lång är du"))
vuxen_sällskap= input("är du med en vuxen ? svara Ja eller Nej : ")
if längd >=130:
    print("du får åka")
elif längd >=110 and vuxen_sällskap == "Ja" :
    print("du får också men med wn vuxen")
elif längd <=110 and vuxen_sällskap == "Nej":
    print("tyvär du får inte åka du är för kort och har ingen vuxen  med dig")
            
 """

 #För andra attraktioner räcker det inte att vara tillräckligt lång: Man måste även ha uppnått en viss ålder. För att få åka Loke måste man vara minst 130 cm lång och minst 7 år gammal.
 #Komplettera följande kod med en if-sats som skriver ut `Du får åka` om användaren uppfyller *båda* kraven och `Du får tyvärr inte åka` annars.

""" print("välkommen till liseberg")
längd = int(input("hur lång är du"))
ålder = int(input("hur gammal är du? "))

if ålder >= 7 and längd >= 130:
    print("du får åka")
else:
    print("du får inte åka")
 """


#Tillbaka till Lisebergbanan: För att få åka behöver man vara minst 130 cm *eller* 110 cm i vuxens sällskap. Vi har två parametrar och behöver alltså ställa två frågor till användaren för att avgöra huruvida hen får åka eller inte. 
#Komplettera följande kod så att den skriver ut `Du får åka` om användaren uppfyller kraven och `Du får tyvärr inte åka` annars. Du kan testa om svaret på andra frågan är `ja` med `har_vuxen_med == 'ja'`.

""" print("välkommen till liseberg")
längd = int(input("hur lång är du"))
vuxen_sällskap= input("är du med en vuxen ? svara Ja eller Nej : ")
if längd >= 130 or längd >=110 and vuxen_sällskap == "Ja":
    print("du får åka eftersom du är minst 130cm eller du är minst 110 cm med en vuxen")
else:
    print("du får inte åka")
 """

#Ovanstående konstruktion löser problemet, men efter att ha frågat alldeles för många vuxna besökare om de har mamma eller pappa med sig inser vi att vi kan lösa problemet på ett smartare sätt.
#Skriv om koden ovan med nästlade if-satser, så att endast de som är mellan 110 och 130 cm får frågan om vuxet sällskap.
""" print('Välkommen till Lisebergbanan!')
längd = int(input('Hur lång är du? '))

if längd >=130 :
    print("du får åka")
    
if längd >= 110:
    vuxen_sälllkap=input("har du en vuxen med dig svara ja eller nej")
    if vuxen_sälllkap == "ja":
        print("du får åka")
else:
    print("du får inte åka")
 """
 
#While-satsen används för att upprepa ett kodblock så länge ett visst villkor är uppfyllt.
#Ser du problemet med följande kod? Testa den gärna för att se vad som händer. Fixa sedan problemet, så att koden räknar in det nya året baklänges från 10.

""" t = 10
while t >= 0:
    print(t)
    t -=1
print("gott nytt år")     """


#I exemplet ovan vill vi göra något ett visst antal gånger, så vi använder en räknare i villkoret. En annan metod är att låta villkoret uttrycka något vi vill uppnå.
#Komplettera koden så att den beräknar och skriver ut hur många månader det tar.
""" goal = 20000
population = 2000
n =0
while population < goal :
    population += 0.1 * population * (1 - population / 25000)
    n +=1
print(f"it took {n} months ")
 """
#Ibland väljer vi att inte skriva ut ett villkor, utan att låta kodblocket köras ända tills det avbryts med `break`.
#Komplettera följande kod så att while-satsen avbryts när användaren angett ett jämnt tal. Kom ihåg att vi känner igen jämna tal på att resten vid heltalsdivision med 2 blir 0.
 

""" while True:
    print("ange ett jämnt tal: ")
    tal = int(input())
    if tal % 2 == 0:
        print("du angav talet",tal)
        break """

#Ändra nu koden så att räknaren startar på 1 och går till 10 istället.
""" 
for i in range(1,10):
    print(i ) """

# test med 3 värden

""" for i in range(50,1,-10):
    print(i, end=" ")
print()
print("i har nu värdet", i)    

for i in range(1,50,10):
    print(i, end=" ")
print()
print("i har nu värdet", i)     """


#Precis som if-satser, så kan for-satser nästlas.Experimentera med följande exempel för att förstå hur de nästlade for-satserna fungerar.
#Skriv nu ut följande mönster:
#1
#1 2 
#1 2 3
#1 2 3 4


""" for i in range(1, 5): # number of times to loop(rows)
    for j in range(1,i+1): # increment i by one each time we loop  
       print(j , end ="")  # 
    print()        
 """

#Skriv nu ut följande mönster:
#4 4 4 4 
#3 3 3 
#2 2 
#1 

for i in range(4,0,-1): # start 4 stop 1 and decrement i with 1 oeach time
    for j in range (i): # numbher of times each number is printed in the current row
        print(i , end=" ") # prints the  value of i which decreasy by each row 

    print() # move to next line after printing each row     