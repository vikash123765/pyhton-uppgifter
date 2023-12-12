# 
pris_dollar = float (input ("pris in dollar: "))    # vad det kostar i dollar gär om svaret från sträng till float
kr_per_dollar =float( input("kr värde per dollar: "))   # hur mycket kronor en dollar är värd
pris_kr = pris_dollar * kr_per_dollar    #  kostnad i dollar * koronor per dollar = kostnad i kronor 
print(f" this is value in kr:                        {pris_kr:.2f} ")    # printar variabelen pris_kr 
# f för att mixa literal sträng med variable värd  # 2 hur många decimaler, f: att det är ett flyat tal