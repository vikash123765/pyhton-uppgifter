import requests
import json

""" url = 'https://catfact.ninja/fact'
response = requests.get(url)
content=response.json()
cat_fact=content["fact"]

print(cat_fact) """



""" url = 'https://official-joke-api.appspot.com/random_joke'
response = requests.get(url)
joke = response.json()
print(joke["setup"])
print(joke["punchline"])
 """

##Plocka ut dict:en som innehåller de personer som finns ombord på ISS. Plocka därifrån ut namnet på var och en av personerna och skriv ut dessa. Skriv gärna ut alla steg på vägen för att lättare se vad nästa steg är.


""" 
url = 'http://api.open-notify.org/astros.json'
response_humans = requests.get(url)
data = response_humans.json()
people_activee=data["people"]
for person in people_activee:
    name = person["name"]
    print(name) """


""" 
url = 'http://api.open-notify.org/iss-now.json'
response = requests.get(url)
data = response.json()
latitude= data["iss_position"]["latitude"]
longitude=data["iss_position"]["longitude"]
print(f"latididue is: {latitude} and longitude is {longitude}")
 """


##Vi har sett hur webb-API:er tar emot parametrar i url:en. Det finns även webb-API:er som tar emot parametrar på andra format. Ett sådant exempel ges av följande kod.


from_currency=input("ange valuta att convertera fråm ")
to_currency=input("ange valuta att convertera till ")
amount=float(input("ange summa att konvertera"))

url = 'https://api.exchangerate.host/convert'
query = {'from': from_currency, 'to': to_currency, 'amount':amount }
response = requests.get(url, params=query)
data = response.json()
converted_amount=data["convert"]
print(f" {amount} in {from_currency} is {converted_amount} in {to_currency}" ) 