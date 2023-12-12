import omvandling_av_temp



c = float(input("temp i celsius: ? "))
f=omvandling_av_temp.CtoF(c)
print(f"{c} in celsius is {f} in farengehight")


f1 = float(input("temp i f: ? "))
c1=omvandling_av_temp.FtoC(f1)
print(f"{f1} in farnehight is {c1:.2f} in celsius")