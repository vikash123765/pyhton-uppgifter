
vänsterskor= int(input("Hur många vänsterskor finns det?")) 
högerskor= int(input("Hur många högerskor finns det?")) 
total= vänsterskor + högerskor
par = min(vänsterskor,högerskor)
max = max(vänsterskor,högerskor)

remainder =  max - par

if remainder ==  vänsterskor - par and remainder > 1:
    print(f"Det finns {par} par och {remainder} överblivna vänsterskor ")
if remainder ==  högerskor - par and remainder > 1:
    print(f"Det finns {par} par och {remainder} överblivna högerskor ")    
if  vänsterskor - par == 1 :
    print(f"Det finns {par} par och 1 överbliven vänstersko")
if  högerskor - par  ==1  :
    print(f"Det finns {par} par och 1 överbliven högersko")    
if par - max == 0:
    print(f"Det finns {par} par och inga överblivna skor.")      