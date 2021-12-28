from ast import Index


salir = True
registro={
    "Nombre":[],
    "NSS":[],
    "Edad":[],
    "Estatura":[],
    "Peso":[],
    "Oxigenación":[],
    "Fecha de contagio":[],
    "Observaciones":[]
}

def registrar():
    NSS=0
    global registro
    while salir:
        NSS=input("Dame el numero de seguro social del paciente:\n")
        if NSS.strip().isdigit():
            NSS=eval(NSS)
            
        else:
            if NSS.lower()=="salir":
                break
            else:
                print("Dame un numero")
                continue
        if NSS in registro["NSS"]:
            indice=registro["NSS"].index(NSS)
            print("Paciente ya contagiado en la fecha {}".format(registro["Fecha de contagio"][indice]))
            continue
       #Aqui checa que todo lo que puso de NSS sea valido
        nombre=input("Dame el nombre del paciente:\n")
        if nombre == "":
            continue
        edad=input("Dame la edad del paciente:\n")
        if edad == "":
            continue
        estatura=input("Dame la estatura del paciente:\n")
        if estatura == "":
            continue
        peso=input("Dame el peso del paciente:\n")
        if peso == "":
            continue
        oxigenacion=input("Dame la oxigenación del paciente:\n")
        if oxigenacion == "":
            continue
        fechaDeContagio=input("Dame la fecha de contagio del paciente:\n")
        if fechaDeContagio == "":
            continue 
        observaciones=input("Dame las observaciones del paciente:\n")
        if observaciones == "":
            continue
        #Checa que no estén vaxios
        registro["NSS"].append(NSS)
        registro["Edad"].append(edad)
        registro["Estatura"].append(estatura)
        registro["Peso"].append(peso)
        registro["Oxigenación"].append(oxigenacion)
        registro["Fecha de contagio"].append(fechaDeContagio)
        registro["Nombre"].append(nombre)
        registro["Observaciones"].append(observaciones)
        print("el paciente ha sido registrado\n")
        #los añade a las lista

def eliminar():
    global registro
    contador=0
    listaTemp=[]
    while salir:
        for i in registro["NSS"]:
            contador+=1
            print("{}. {}".format(contador, i))
            listaTemp.append(i)
        eliminar=eval(input("Dame el paciente a eliminar, ya sea por numero de indice o por NSS:\n"))
        if eliminar in registro["NSS"]:
            borrar=registro["NSS"].index(eliminar)
            registro["NSS"].pop(borrar)
            registro["Nombre"].pop(borrar)
            registro["Edad"].pop(borrar)
            registro["Estatura"].pop(borrar)
            registro["Peso"].pop(borrar)
            registro["Oxigenación"].pop(borrar)
            registro["Fecha de contagio"].pop(borrar)
            registro["Observaciones"].pop(borrar)
            print("Paciente eliminado")
            break
        #Lo borra sacando el numeor de indice que coincida
        elif eliminar<=len(registro["NSS"]):
            registro["NSS"].pop(eliminar-1)
            registro["Nombre"].pop(eliminar-1)
            registro["Edad"].pop(eliminar-1)
            registro["Estatura"].pop(eliminar-1)
            registro["Peso"].pop(eliminar-1)
            registro["Oxigenación"].pop(eliminar)
            registro["Fecha de contagio"].pop(eliminar-1)
            registro["Observaciones"].pop(eliminar-1)
            print("Paciente eliminado")
            break
        #Lo borra usando la entraada como numero de indice
        else:
            print("No es un NSS o indice valido")
            break

def imprimir():
    global registro
    contador = 1
    for i in range(len(registro["NSS"])):
        nombres=tuple(registro["Nombre"])
        NSSs=tuple(registro["NSS"])
        oxigenaciones=tuple(registro["Oxigenación"])
        fechas = tuple(registro["Fecha de contagio"])
        print("{}. El paciente {} con el NSS {} fue internado con oxigenación de {} el día {}".format(contador, nombres[i], NSSs[i], oxigenaciones[i], fechas[i]))
        contador+=1
#Basico, saca el numeor de indice y usa el mismoinidice para las otras listas
        
while salir:
    print("Hola Alfredo, que desea realizar? ")
    seleccionModo=input("1 - Registrar nuevo paciente \n2 - Eliminar paciente \n3 - Mostrar lista de pacientes \n4 - Salir\n")
    if seleccionModo == "1" or seleccionModo.upper() == "R":
        registrar()
    elif seleccionModo == "2" or seleccionModo.upper() == "E":
        eliminar()
    elif seleccionModo == "3" or seleccionModo.upper() == "M":
        imprimir()
    elif seleccionModo == "4" or seleccionModo.upper() == "S":
        print("Gracias por usar el programa")
        break
    else:
        print("Input no valido")    
