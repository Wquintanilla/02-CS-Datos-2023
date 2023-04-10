#a)
#print("Hola mundo")
#b)
#nombre="Wilder"#entre comillas el nombre
#print(nombre)
#c)
###
import os
opcion=int(input("Seleccione \n[1] Kilometros a Millas\n[2]Millas a Kilometros\n"))
while not(opcion==1 or opcion==2):
    print("Ingreso una opcion no valida")
    opcion=int(input("Seleccione \n[1] Kilometros a Millas\n[2]Millas a Kilometros\n"))
if opcion == 1:
    kilometro=float(input( "Ingrese La cantidad de Kilometros: " ))
    print("la cantidad ",round(kilometro,2)," kilometros equivalen a ",round(kilometro*(1/1.61),2)," millas")
else:
    
    milla=float(input( "Ingrese La cantidad de MILLAS: " ))
    print("la cantidad ",round(milla,2)," millas equivalen a ",round(milla*(1/1.61),2)," Kilometros")




