frase = input("Ingrese una frase: ")
CantVocales = 0
frase.lower()
vocales = "aeiou"
contador = 0
for i in frase:
    for j in vocales:
        contador+=1
        if i==j:
            CantVocales+=1

print("la frase continene {} vocales".format(CantVocales))

print(contador)
