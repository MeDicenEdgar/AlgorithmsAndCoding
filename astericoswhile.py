ciclos = eval(input("¿Cuántos pisos quieres?: \n"))
contador=0
wow=0
while wow < ciclos:
    wow+=1
    contador+=1
    espacio=" "*(ciclos-wow)
    espacio+="* "*wow
    print(espacio)
