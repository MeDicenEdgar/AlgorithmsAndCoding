
def sumaN(*numeros):
    suma=0
    for i in range(len(numeros)):
        if not(type(numeros[i]) == int or type(numeros[i]) == float):
            return("error")
            break
        else:
            suma=suma+numeros[i]           
    return suma
    
def restaN(*numeros):
    numero = numeros[0]
    if type(numeros[0])==str:
        return("error")            
    else:
        for i in range(1, len(numeros)):
            numero = numero - numeros[i]
        return(numero)

def encriptaC(cadena):
    if type(cadena)!=str:
        return("error")
    else:
        resu = ""    
        cadena = cadena.lower()
        for i in cadena:
            asqui = ord(i)
            if asqui != 32:
                asqui +=6
                if asqui > 122:
                    asqui=asqui-26
            resu += chr(asqui)
        return resu
    
def desencriptaC(cadena):
    if type(cadena)!=str:
        return("error")
    else:
        resu = ""    
        cadena = cadena.lower()
        for i in cadena:
            asqui = ord(i)
            if asqui >= 111 and asqui <= 122:
                asqui=asqui-14
            elif asqui >= 97 and asqui <= 110:
                asqui=asqui+12
            resu += chr(asqui)
        return resu