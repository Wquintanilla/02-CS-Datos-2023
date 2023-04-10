ano=int(input("Ingrese el ano: "))
bisiesto=True   
if ano<1582:
    print("No esta dentro del periodo del Calendario Gregoriano")
elif ano%4!=0 :
    bisiesto=False
elif ano%100!=0:
    pass
elif ano%400!=0:
    bisiesto=False
else:
    pass

if bisiesto:
    print("AÑO BISIESTO")
else:
    print("AÑO COMUN ")