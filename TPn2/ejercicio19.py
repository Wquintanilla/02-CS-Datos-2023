pan=3.49
canP=int(input("Ingrese la cantidad de barras de pan vendidas que no son del dia: "))
costo=pan*canP
print("\nEl costo del pan es de ",round(costo,2),"$ y se realiza un descuento del 60%: ",round(costo*0.6,2),"$")
print("el costo final es de ",round(costo*0.4,2),"$")
