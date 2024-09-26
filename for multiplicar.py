
#num=int(input("ingrese un numero:  "))
#un numero del primer for recorre todos los del for anidado y vuelve a el primer for por el siguiente numero
    
for x in range(1,11):
    for num in range (1,11):
        print(f"{x}x{num}={x*num}, ")
        
edad=7
mayor="eres mayor de edad"
menor="eres menor de edad"
print(mayor if edad >= 18 else menor)#condicion del if se coloca siempre a la izquierda de la condicion

diccionario={
             "a":"1","b":"2","c":"3","d":"4","e":"5","f":"6","g":"7","h":"8",
             "i":"9","j":"10","k":"11","l":"12","m":"13","n":"14","ñ":"15","o":"16",
             "p":"17","q":"18","r":"19","s":"20","t":"21",
             "u":"22","v":"23","w":"24","x":"25","y":"26","z":"27"
             
             
             }

def encriptar(mensaje):
    mensaje_encriptado=""
    for letra in mensaje:
        if letra.casefold() in diccionario:
            mensaje_encriptado+=diccionario[letra.lower()]
        else:
            mensaje_encriptado+=letra
    return mensaje_encriptado

mensaje=input("ingrese un mensaje: ")
resultado = encriptar(mensaje)
print(resultado)

def desencriptar(mensaje):
    mensaje_desencriptado=""
    for letra in mensaje:
        if letra in diccionario.values():
            for key, value in diccionario.items():
                if letra == value:
                    mensaje_desencriptado+=key
        else:
            mensaje_desencriptado+=letra
    return mensaje_desencriptado

mensaje_desencriptado=desencriptar(resultado)
print(mensaje_desencriptado)