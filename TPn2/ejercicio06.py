#
valorx=float(input("ingrese el valor de X "))
print("Esta X se cargara en f(X)=3x^3-2*x^2+3*x-1")
print("Esta X=",valorx," se cargara en f(",valorx,")=3",valorx,"^3-2*",valorx,"^2+3*",valorx,"-1")
print("X=",valorx,"       Y=f(X)=",3*valorx**3-2*valorx**2+3*valorx-1,"\n\n")


#le da valores a X de -1 a 1
for i in range(-1,2):
    print("X=",i,"       Y=f(X)=",3*i**3-2*i**2+3*i-1)
