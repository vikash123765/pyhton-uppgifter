#Be användaren om ett positivt heltal n och beräkna n! = 1 * 2  * ... * n (n-fakultet). alltså upprepade muliplikationer tills vi nått talet n
# läs in tal från användaren
n = int(input("n:"))
#skapa variabel för att lagra resultatet
n_fakultet= 1 

## mulipliplicera heltalen från 1 till n+1
for i in range (1,n +1):
    n_fakultet *= i

print("n! fakukultet:",n_fakultet)    
