'''Se carga una fecha (día, mes y año) por teclado.
 Mostrar un mensaje si corresponde al primer trimestre del año (enero, febrero o marzo) 
 Cargar por teclado el valor numérico del día, mes y año.'''
dia=int(input("Ingrese el dia en formato numerico dd : "))
mes=int(input("Ingrese el mes en formato numerico mm : "))
anio=int(input("Ingrese el año en formato numerico aaaa : "))
if mes<=3:
    print("1er TRIMESTRE")
elif mes<=6:
    print("2do TRIMESTRE")
elif mes<=9:
    print("3ro TRIMESTRE")
else:
    print("4to TRIMESTRE")