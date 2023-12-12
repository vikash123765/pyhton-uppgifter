
ord = input("Ange ett ord: ")

# Inled med att göra den första bokstaven liten
omvandlat_ord = ord[0].lower()

# loopa igenom resten av bokstäverna  eftersom första[0] alltid är lower vi börjar från index[1]
for i in range(1, len(ord)):
    if i % 2 == 0:
        # Om index är jämt, gör bokstaven liten 
        omvandlat_ord = omvandlat_ord+ ord[i].lower()
    else:
        # Om index är udda, gör bokstaven stor
        omvandlat_ord = omvandlat_ord+ ord[i].upper()


print(omvandlat_ord)
