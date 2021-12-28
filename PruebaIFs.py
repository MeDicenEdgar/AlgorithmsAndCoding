Num1 = eval(input("Numero 1: "))
Num2 = eval(input("Numero 2: "))
#print(type(Num1))
if (type(Num1) == int) and (type(Num2) == int):
    Num3=Num2/Num1
    print("El resultado es: ",Num3)
    Res= Num2%Num1
    if(Res == 0):
        print("El número es entero")
    else:
        print("El número es flotante")
else:
    print("Favor de introducir 2 numeros enteros")


