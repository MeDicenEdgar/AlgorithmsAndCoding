#Ejercicio 1
parte1 = (10*4)>13
print(parte1)
#True
parte2 = (5+4) == 30
print(parte2)
#False
parte3 = parte2 and parte1 == True
print (parte3)
#False

#Ejercicio2
part1 = (4 ** 2) >= (2 * 8)
#True
part2 = ((8 / 2) != (10 - 6))
#False
resultado1 = part1 and part2 == True
#False
part3 = ((5 * 5) >= (20 + 5)) 
#True
part4 =  (10 == (5 * 2))
#True
resultado2 = part2 and part3 == True
#True
resultadoFinal = resultado1 and resultado2==True
#False
print(((4 ** 2) >= (2 * 8)) and ((8 / 2) != (10 - 6)) and (((5 * 5) >= (20 + 5)) or (10 == (5 * 2))))

