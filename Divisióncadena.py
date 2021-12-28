cadena=input(" Favor de introducir la cadena con la siguiente sintaxis \n Operación Numero1 Numero 2 \n Solo se aceptan suma resta multiplicación y división:\n")
res=cadena.split(" ")
#print(res[0])
operacion=(res[0].upper())
#print(operacion)
N1=eval(res[1])
N2=eval(res[-1])
#print(N1)
#print(N2)
if operacion=="SUMA":
    #print("suma")
    resultado=N1+N2
elif operacion=="RESTA":
    #print("resta")
    resultado=N1-N2
elif operacion == "MULTIPLICACION":
    #print("multi")
    resultado=N1*N2
elif operacion == "DIVISION":
    #print("divi")
    resultado=N1/N2

print(resultado)
