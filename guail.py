print("Introduce la calificación a registrar, en caso de no tener mas estudiante, introducir la letra F")
caliProm=0
estudiante=0
salir=False
recibir=""
while salir==False:
    recibir = input("Dame la calificacion del estudante {}: ".format(estudiante+1))
    if recibir.upper()=="F":
        break
    elif recibir.isdigit()==True:
        caliProm+=eval(recibir)
        estudiante+=1
       # print(caliProm)
       # print(estudiante)
    else:
        print("Comando no reconocido, favor de poner un numero o una f")
print("El promedio de los estudiantes es {}".format(caliProm/estudiante))

    


