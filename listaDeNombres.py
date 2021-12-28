
nombres = []
def buscarNombre(busqueda):
    global nombres
    if busqueda in nombres:
        return "Si, si está"
    else:
        return "No, no está"
def agregar():
    salir = False
    while salir == False:
        global nombres
        nombreTemp = input("Dame un nombre, para salir al menu, escribe SALIR:\n")
        if nombreTemp.upper()=="SALIR":
            salir = True
        else:
            nombres.append(nombreTemp)
menu = True
while menu:
    select=input("Bienvenido a mi programa, para seleccionar que hacer que continuacion escribe un numero del 1 al 3\n 1. Buscar algo en la lista \n 2. Imprimir la lista\n 3. Agregar algo a la lista: \n")
    print(select)
    if select == "1":
        print(buscarNombre(input("Dame el nombre a buscar:\n ")))
    elif select=="2":
        print(nombres)
    elif select=="3":
        agregar()
    else:
        print("por favor dame un numero dle 1 al 3")
        


