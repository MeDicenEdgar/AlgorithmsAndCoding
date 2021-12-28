ciclos = eval(input("¿Cuántos pisos quieres?: \n"))
contador=0
for i in range(0, ciclos+1):
    contador+=1
    espacio=" "*(ciclos-i)
    espacio+="* "*i
    print(espacio)
print(contador)

