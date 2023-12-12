def CtoF(temp_c):
    if temp_c < -273.15:
        raise ValueError("Temp under absolut noll point")
    temp_f = temp_c * 9 / 5 + 32
    return temp_f

def FtoC(temp_f):
 
    temp_c = (temp_f - 32) * 5 / 9   
    if temp_c < -273.15:
        raise ValueError("Temp under absolut noll point")
    return temp_c

if __name__ == "__main__":
    c= 30 
    f = CtoF(c)
    print(f"{c} celsius is {f} farenheight")

if __name__ == "__main__":
    f1= 30 
    c1 = FtoC(f1)
    print(f"{f1} farenheight is {c1} celsiys")