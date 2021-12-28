pasos = eval(input("¿hasta qué numero quieres llegar?:\n"))
num1 = 0
num2 = 1
num3 = 0
for i in range(0, pasos):
    if num3<=55:
        print(num3)
        num3=num1+num2
        num1=num2
        num2=num3
    else:   
        break
    
    
