moneda = input("¿Qué moneda tienes, dolar o peso?\n")
cantidad = eval(input("¿Qué cantidad quieres cambiar?\n"))
cambio = input("¿A qué moneda quieres cambiar? \n(Aceptamos: euro, yen, libra esterlina, peso colombiano, franco y rublo\n")
conversion=0.0
#Aqui pedimos la moneda que tiene, la que quiere y la cantidad
if (moneda.upper()=="DOLAR") or (moneda.upper()=="DOLARES"):
    #Vemos si la moneda que tiene es dolar o peso y dependiendo de cual tenga se va a un if o a otro
    if (cambio.upper()=="EURO") or (moneda.upper() == "EUROS"):
        conversion=cantidad*0.86
        print(conversion)
    elif (cambio.upper()=="YEN") or (moneda.upper() == "YENES"):
        conversion=cantidad*111.91
    elif (cambio.upper()=="LIBRA") or (moneda.upper() == "LIBRAS"):
        conversion=cantidad*0.74
    elif (cambio.upper()=="FRANCO") or (moneda.upper() == "FRANCOS"):
        conversion=cantidad*0.93
    elif (cambio.upper()=="RUBLO") or (moneda.upper() == "RUBLOS"):
        conversion=cantidad*72.86
    elif (cambio.upper()=="PESO COLOMBIANO") or (moneda.upper() == "PESOS COLOMBIANOS"):
        conversion=cantidad*3830.50
    else:
        print("La moneda que quieres no es válida")
    #Ya dentro de un if, ya sea el de dolar o peso, se entra a otro if donde se ve la moneda a la que quiere convertir
elif (moneda.upper()=="PESO") or (moneda.upper()=="PESOS"):
    if (cambio.upper()=="EURO") or (moneda.upper() == "EUROS"):
        conversion=cantidad*0.042
    elif (cambio.upper()=="YEN") or (moneda.upper() == "YENES"):
        conversion=cantidad*5.46
    elif (cambio.upper()=="LIBRA") or (moneda.upper() == "LIBRAS"):
        conversion=cantidad*0.036
    elif (cambio.upper()=="FRANCO") or (moneda.upper() == "FRANCOS"):
        conversion=cantidad*0.046
    elif (cambio.upper()=="RUBLO") or (moneda.upper() == "RUBLOS"):
        conversion=cantidad*3.56
    elif (cambio.upper()=="PESO COLOMBIANO") or (moneda.upper() == "PESOS COLOMBIANOS"):
        conversion=cantidad*3830.50
    else:
        print("la moneda que quieres no es válida")
else:
    print("El cambio a convertir no es valido")
    #En caso de que no coincida con ninguna, se le dice al usuario que la moneda no es valida
print("El cambio de {0} a {1} es: {2}".format(moneda, cambio, conversion))
    #Concatenamos la respuesta para que sea entendible