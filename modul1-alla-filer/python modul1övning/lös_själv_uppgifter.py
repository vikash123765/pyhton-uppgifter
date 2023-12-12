import math

#   Priset på en vara är tillfälligt nedsatt. Etiketten anger det ursprungliga priset och prissänkningen 
#i procent men det nedsatta priset saknas. Skriv ett program som läser in det ursprungliga priset samt prissänkningen 
#i procent. Programmet ska beräkna och skriva ut det nedsatta priset. Avrunda svaret till två decimaler.

#original_price = float(input("original cost: "))
#discount_in_procent= int(input("discount in % : "))

#calculated_discount = original_price * discount_in_procent / 100 

#price_after_discount = original_price - calculated_discount
#print(f"final price is {price_after_discount:.2f}")




#Skriv ett program som läser in önskad volym och höjd. Programmet ska sedan med hjälp av formeln ovan beräkna och skriva ut cylinderns radie. 


cylinders_volym= float(input("ange cylindenrs volym in cm3"))
cylinders_height= float(input("ange cylindenrs height i cm"))
r = math.sqrt(cylinders_volym/math.pi * cylinders_height)
print(f"cycilnderns radie är : {r} cm ")


##Priset på en vara är tillfälligt nedsatt. Etiketten anger det ursprungliga priset och prissänkningen 
#i procent men det nedsatta priset saknas. Skriv ett program som läser in det ursprungliga priset samt prissänkningen 
#i procent. Programmet ska beräkna och skriva ut det nedsatta priset. Avrunda svaret till två decimaler.

#original_price = float(input("original cost: "))
#discount_in_procent= int(input("discount in % : "))

#calculated_discount = original_price * discount_in_procent / 100 

#price_after_discount = original_price - calculated_discount
#print(f"final price is {price_after_discount:.2f}")




#Skriv ett program som läser in önskad volym och höjd. Programmet ska sedan med hjälp av formeln ovan beräkna och skriva ut cylinderns radie. 


cylinders_volym= float(input("ange cylindenrs volym in cm3"))
cylinders_height= float(input("ange cylindenrs height i cm"))
r = math.sqrt(cylinders_volym/math.pi * cylinders_height)
print(f"cycilnderns radie är : {r} cm ")

