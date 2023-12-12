filename = input("filename")

with open(filename,encoding="utf-8") as f: 
    conent= f.readlines()


for i,line in enumerate(conent):
  
    print(i,line[:-1])
