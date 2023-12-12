import math
import random

# Kör följande kod och se till att du förstår vad den gör:
#name = input("whats your name ? ")  # storing input prompt in name variable
#print("hello",name)     ## printing string literal hello and name variable 


# Läsa och skriva numeriska värden. Precis som med text
# kan vi läsa in och skriva ut numeriska värden. Vi gör ett första försök med följande kod
#tal = input("give any number")
#print("the number you chose is : ",tal)

#tal = input("give any number")
#dubbelt_up= 2 * tal   # wont wrk because its stored as string default 
#print("the number you chose is : ",tal, " but i say double up! : ",dubbelt_up )

#tal = int(input("give any number"))  # specify conversion type
#dubbelt_up= 2 * tal   
#print("the number you chose is : ",tal, " but i say double up! : ",dubbelt_up )

# Decimaltal: Ibland kanske vi vill läsa in ett tal som inte är ett heltal.
# Fixa följande kod så att den funkar. Användaren ska kunna mata in en diameter
#  som tolkas som ett decimaltal.

##pi = 3.14159
##diameter = float(input("ange diamter"))
##omkrets= pi * diameter
##print("cirkels omkrets: ",omkrets)

# version med bara 2 decimal tal 
#pi = 3.14159
#diameter = float(input("ange diamter"))
#omkrets= pi * diameter
#print(f"cirkels omkrets: {omkrets:.2f}")

#Formatera numeriska värden
#Vi kan formatera utskrifter med hjälp av f-strängar. Följande kod skriver ut resultatet av en beräkning med två decimaler.

#värde = 8 
#invers = 1/ värde
#print(f"inversen av {värde} är {invers}")

# Numeriska uttryck och beräkningar
#Ett uttryck som resulterar i ett numeriskt värde kallas även ett aritmetiskt uttryck. Aritmetiska operatorer är exempelvis de fyra räknesätten.
#Komplettera följande kod så att andelen kvinnor i gruppen skrivs ut, uttryckt i procent.

#1.(antal_kvinnor = int(input('Antal kvinnor: ')
#antal_män = int(input('Antal män: '))
#andel_kvinnor = 
#procent_kvinnor = 
#print(f'I gruppen är det {procent_kvinnor:.2f} % kvinnor.') )

#1 svar :
#antal_män = int(input("antal män : "))
#antal_kvinnor = int(input("antal kvinnor : "))
#andel_kvinnor =  antal_kvinnor/antal_män 
#procent_kvinnor =  andel_kvinnor * 100 
#print(f"i gruppen är det{procent_kvinnor:.2f} % kvinnor"))

#2.(
#antal_kakor = int(input('Antal kakor: '))
#antal_barn = int(input('Antal barn: '))
#kakor_per_barn = 
#kakor_över = 
#print(f'Det blir {kakor_per_barn} kakor per barn och {kakor_över} kakor över.')
#)

#2 svar: 
#antal_kakor = int(input("antal kakor : "))
#antal_barn = int(input("antal barn : "))
#kakor_per_barn = antal_kakor//antal_barn  # delar totatal antalet kakor med antalet ban
#kakor_över  = antal_kakor % antal_barn   # hittar remainder när vi modulär delar totala antlet kakor med totala antalet bar

#print(f"så här många kakor per barn = {kakor_per_barn} och så här många kakor blir över = {kakor_över}")



#Inbyggda funktioner
#I Python finns de inbyggda funktioner `min()`, `max()`, `abs()`. Dessa är användbara när man inte i förväg vet vilket värde som är störst.
#Komplettera följande kod så att längdskillnaden skrivs ut.
#3.
#l1 = int(input('Din längd i cm: '))
#l2 = int(input('Din partners längd i cm: '))
#delta_l = 
#print(f'Längdskillnaden är {delta_l} cm.')


# 3 svar = 
#l1= int(input("din längs i cm "))
#l2= int(input("din partnes längd i cm "))
#highest_number = max(l1,l2)
#lowest_number = min(l1,l2)
#delta_1= highest_number - lowest_number
#print(f"läng skillnaden är {delta_1} cm")


#Modulen `math`
#Ytterligare funktioner, som kvadratroten `sqrt()` finns i en modul som heter `math`. För att komma åt funktionen behöver vi först importera modulen och sedan ange att funktionen ska hämtas från modulen.
#Vi använder Pythagoras sats $$a^2 + b^2 = c^2 \quad \Longleftrightarrow \quad c = \sqrt{a^2 + b^2}$$ för att beräkna hypotenusan i en rätvinklig triangel.
#Komplettera följande kod så att resultatet skrivs ut med en decimal. *Glöm inte att börja med att göra modulen tillgänglig.
#4.(a = float(input('Första kateten, a: '))
#b = float(input('Andra kateten, b: '))
#c = 
#print(f'Hypotenusan är {c}.')

# 4 svar = 
#a = float(input(" första kataten a är : "))
#b = float(input(" första kataten b är : "))
#c =   math.sqrt(a * a + b * b)
#print(f"hypotenusan är {c:.1f}")


#5.I modulen `random` definieras funktioner som kan användas för att generera slumptal.
#Använd funktionen `randint()` från module `random` för att komplettera följande kod så att den simulerar en tärning med ett valfritt antal sidor. *Glöm inte att börja med att göra modulen tillgänglig.*


n = int(input("ange sidor på tärningarna"))
utfall= random.randint(1,n)
print(f"tärningen med {n} sidor är kastad. Du fick en {utfall}:a")



