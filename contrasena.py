contrasena="Contraseña"
Numintentos =0
while Numintentos < 5:
    intento=input("Contraseña: ")
    if intento == contrasena:
        print("acceso permitido")
        break
    else:
        Numintentos+=1
        print("contraseña incorrecta, numeo de intentos restantes {}".format(5-Numintentos))
if Numintentos>=5:
    print("No mas intentos, intentelo de nuevo mas tarde")
