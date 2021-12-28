from mi_libreria_ayp import *

res = sumaN(45,45,45,34,23,45,57)
print(res == 294)
res = sumaN(45,45,34,23)
print(res == 147)
res = sumaN(45,45,34,23,45,65,89,34,56)
print(res == 436)
res = sumaN("HOLA COMO ESTAS")
print(res == "error")

res = restaN(5000,45,678,99,234,675,46)
print(res == 3223)
res = restaN(8000,455,787,569,634,67,46,654,678,983)
print(res == 3127)
res = restaN(50,2,4,5,1,34,7,8,9,2,4,9,5)
print(res == -40)
res = restaN("HOLA COMO ESTAS")
print(res == "error")

# usen lower() para encriptar cualquier cadena que reciban, esté o no esté en mayúsculas 
res = encriptaC("Hola") 
print(res == "nurg")
res = encriptaC("Hola Mundo")
print(res == "nurg satju")
res = encriptaC("Super Secreto")
print(res == "yavkx ykixkzu")
res = encriptaC("abcdefghijklmnopqrstuvwxyz")
print(res == "ghijklmnopqrstuvwxyzabcdef")
res = encriptaC(45466)
print(res == "error")

res = desencriptaC("vczo")
print(res == "hola")
res = desencriptaC("vczo aibrc")
print(res == "hola mundo")
res = desencriptaC("gidsf gsqfshc")
print(res == "super secreto")
res = desencriptaC("opqrstuvwxyzabcdefghijklmn")
print(res == "abcdefghijklmnopqrstuvwxyz")
res = desencriptaC(45466)
print(res == "error")