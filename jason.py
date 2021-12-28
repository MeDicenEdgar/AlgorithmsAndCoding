import json

datos={
    "usuarios":[]
}
nombre =""

while nombre.lower()!="salir":
    nombre=input("Dame un nombre: ")
    if nombre.lower()=="salir":
        break
    apellido= input("Dame un apellido: ")
    edad=input("Dame una edad: ")
    sexo= input("Dame un sexo: ")
    dicttemp={
        "nombre": nombre.title(),
        "apellido": apellido.title(),
        "edad": edad,
        "sexo": sexo[0],
    }
    datos["usuarios"].append(dicttemp)
archivo = open("usuarios.json", "w")
json.dump(datos["usuarios"], archivo)