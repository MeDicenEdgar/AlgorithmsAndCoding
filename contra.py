import random
longitud = eval(input("Dame la longitud de tu cadena: \n"))
cadena = ""
mayus=0
for num in range(0, longitud+1):
    char = chr(random.randint(97, 122))
    """"mayus=random.randint(0,1)
    if mayus == 1:
        char=char.upper()"""
    
    cadena += char

print(cadena)