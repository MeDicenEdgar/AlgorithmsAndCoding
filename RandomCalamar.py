""" 
Pseudocódigo:
INICIO
Definir miNumero como entero random entre el 0 y el 100
Definir salir como un booleano verdadero
Mientras salir sea verdadero
    Escribir "tengo un numero, intenta adivinarlo"
    Leer suNumero
    Si SuNumero es menor que miNumero
        Escribir "Incorrecto, mi numero es mayor"
        Continuar
    Si SuNumero es mayor que miNumero 
        Escribir "Incorrecto, mi numero es menor"
        Continuar
    Si no 
        Escribir "Correcto, lo lograste"
        Salir

FIN

"""

import random
miNumero= random.randint(0, 100)
salir = True 
while salir:
    suNumero=eval(input("tengo un numero, intenta adivinarlo: \n"))
    if suNumero<miNumero:
        print("Incorrecto, mi numero es mayor\n")
        continue
    elif suNumero>miNumero:
        print("Incorrecto, mi numero es menor\n")
        continue
    else:
        print("Correcto, lo lograste")
        break