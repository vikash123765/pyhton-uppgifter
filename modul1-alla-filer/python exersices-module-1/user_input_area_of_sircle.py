import math # imoortera modul 
# läs in circle area för om till float 
circle_area =float(input ("circle area : "))
#använda formen A = pi * r *r och lös ut r -> radius
radius = math.sqrt(circle_area / math.pi)  # använd prefix math.

# skriv ut resultatet med 3 decimaleer       
print(f"Circles radius: {radius:.3f}")