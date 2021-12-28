"""
INICIO
Definir cadena como un string
Escribir "Dame la cadena que quieres evaluar"
Leer cadena
Definir contador como 0
Mientras contador sea menor a la longitud de cadena
    comparador = cadena[contador]
    Escribir "dame la letra numero, conntador
    si contador es diferente a comparador
        Escribir "Error ponlo en orden"
        contador =0
Escribir "Bien hecho"
FIN
"""


cadena = input("Dame la cadena que quieres evaluar: \n")
contador =0
while contador < len(cadena):
    comparador = cadena[contador]
    inn = input("dame la letra numero {}: ".format(contador+1))
    if comparador != inn:
        print("Error ponlo en orden")
        contador=0
        continue

    contador+=1
print("Bien hecho")