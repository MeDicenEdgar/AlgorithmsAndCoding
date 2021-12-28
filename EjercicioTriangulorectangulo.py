ToC = input("Escriba si quiere un triangulo(poniendo una t), o un rectangulo(poniendo una r) \n " )
Altura = eval(input("Introduzca la altura: "))
Base = eval(input("Introduzca la Base: "))
if ToC[0].upper()== "T":
    Resultado = (Base*Altura)/2
    print("El Área es ", Resultado)

elif ToC[0].upper()== "R":
    Resultado = (Base*Altura)
    print("El Área es: ", Resultado)

else:
    print("Resultado no Valido, favor de reintroducirlo")