
diccionario = {
    'a': '78', 'b': '102', 'c': '789', 'd': '45', 'e': '765',
    'f': '853', 'g': '963', 'h': '///**', 'i': '-+-+', 'j': '63265',
    'k': '7895', 'l': '787777', 'm': '45588', 'n': '88888', 'o': '47777777',
    'p': '654456', 'q': '789789', 'r': '789569', 's': '789329', 't': '7897549', 
    'u': '7896589', 'v': '798-+89', 'w': '7????', 'x': '78¿¿¿¿¿9', 'y': '78%%%%%89',
}

def encriptar_mensaje(mensaje):
    mensaje_encriptado = ''
    for letra in mensaje:
        if letra.lower() in diccionario:
            mensaje_encriptado += diccionario[letra.lower()]
        else:
            mensaje_encriptado += letra
    return mensaje_encriptado

"""

def encriptar_mensaje(mensaje):
    mensaje_encriptado = [] con list 
    for letra in mensaje:
        if letra.lower() in diccionario:
            mensaje_encriptado.append(diccionario[letra.lower()]) ##se añade con apppend
        else:
            mensaje_encriptado.append(letra)
    return ''.join(mensaje_encriptado) ##devuelve un string piodria quitar el join y retornar la lista

mensaje = input("Ingrese el mensaje a encriptar: ")
mensaje_encriptado = encriptar_mensaje(mensaje)
print("Mensaje encriptado:", mensaje_encriptado)

"""

mensaje = input("Introduce el mensaje a encriptar: ")

mensaje_encriptado = encriptar_mensaje(mensaje)
print("Mensaje encriptado:", mensaje_encriptado)
