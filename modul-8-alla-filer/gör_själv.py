import requests
import json 

response = requests.get("https://api.kanye.rest")
content= response.json()
print(content["quote"])



## hav ch land, valuteomvanling och dad jokes är kvar från modul 8 