#Calcular el sueldo mensual de un operario conociendo la cantidad de horas trabajadas
# y el valor por hora.

#Teniendo en cuenta que se trabaja de lunes a viernes de 8 a 17, con 1 hora de almuerzo
#y el mes tiene 30 dias
cantHora=(17-8)+1*5*4.5#5 son los dias trabajados y 4.5 las semanas del mes
valorHora=123.66
#si se quiere se puede agregar por teclado seria un valorHora=float(input("mensaje"))
print("El sueldo mensual es: ", cantHora*valorHora," moneda de pago")
