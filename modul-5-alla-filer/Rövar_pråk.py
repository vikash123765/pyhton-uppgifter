konsonatner = "bcdfghjklmnpqrstvwxz"

def translate(original):
    translation=" "
    for letter in original:
        if letter.lower() in konsonatner:
            translation += letter + "o" + letter.lower() 
        else:
            translation += letter
    return translation  

if "__main__":  
    text = input("skriv en text: ")
    översättning=translate(text)
    print(översättning)        