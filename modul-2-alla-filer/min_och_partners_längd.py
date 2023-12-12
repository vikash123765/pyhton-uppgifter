#   Komplettera följande kod så att en av följande texter skrivs ut, beroende på de två längder användaren anger:
 #  * `Du är 13 cm längre än din partner.`
 #  * `Din partner är 6 cm längre än dig.`
 #  * `Du och din partner är lika långa.` 
#Längdskillnaderna i exemplen ovan ska naturligtvis bytas ut mot skillnaden mellan de två angivna längderna.

min_längd= int(input("hur lång är jag? "))
partners_längs = int(input("hur lång är partner? "))

if min_längd == partners_längs +13:
    print("jag är 13 cm längre än min partner")
if partners_längs == min_längd +6:
    print("partner är 6 cm längre än mig")
if partners_längs == min_längd:
    print("jag och min partner är lika långa")
else:
    print("inget av alternativen stämer")            