
import requests

def hitta_kommunkod(name):
    url=(f"https://api.skolverket.se/skolenhetsregistret/v1/kommun")
    response = requests.get(url)
    data=response.json()
    kommun_list = data["Kommuner"]

    for kommun in kommun_list:

        if kommun["Namn"] == name:
            result=kommun
            kommunkod=result["Kommunkod"]

            return kommunkod
    raise ValueError("Kommun kod finns ej")
 
    

if __name__ == "__main__":
    try:
        kod = hitta_kommunkod('Stockholm')
        print(kod) 
    except ValueError as e:
        print(e) 



    
import requests

def hitta_skolor(kod):
    url="https://api.skolverket.se/skolenhetsregistret/v1/skolenhet"
    response = requests.get(url)
    data=response.json()

    skolenheter=data["Skolenheter"]

    lst=[]

    for item in skolenheter:
        if kod == item["Kommunkod"]:
            lst.append(item["Skolenhetsnamn"])
    return lst
    
 
if __name__ == "__main__":
        kommun_name = input("Ange kommunnamn: ")
        try:
            kod = hitta_kommunkod(kommun_name)
            skolor = hitta_skolor(kod)
            if skolor:
                print(f"Skolenheter i {kommun_name}:")
                for skola in skolor:
                    print(skola)
            else:
                print(f"Inga skolenheter hittades för {kommun_name}.")
        except ValueError:
            print("Felaktigt kommunnamn.")
   