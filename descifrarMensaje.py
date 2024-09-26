diccionario = {
    'a': '78', 'b': '102', 'c': '789', 'd': '45', 'e': '765',
    'f': '853', 'g': '963', 'h': '///**', 'i': '-+-+', 'j': '63265',
    'k': '7895', 'l': '787777', 'm': '45588', 'n': '88888', 'o': '47777777',
    'p': '654456', 'q': '789789', 'r': '789569', 's': '789329', 't': '7897549', 
    'u': '7896589', 'v': '798-+89', 'w': '7????', 'x': '78¿¿¿¿¿9', 'y': '78%%%%%89',
}

# Función para encriptar el mensaje
def encriptar_mensaje(mensaje):
    mensaje_encriptado = []
    for i in mensaje:
        if i.lower() in diccionario:
            mensaje_encriptado.append(diccionario[i.lower()])
        else:
            mensaje_encriptado.append(i)
    return ' '.join(mensaje_encriptado)

# Crear un diccionario invertido para descifrar el mensaje
diccionario_invertido = {valor: clave for clave, valor in diccionario.items()}


# Función para descifrar el mensaje
def descifrar_mensaje(mensaje_encriptado):
    mensaje_descifrado = []
    partes = mensaje_encriptado.split(' ')
    for parte in partes:
        if parte in diccionario_invertido:
            mensaje_descifrado.append(diccionario_invertido[parte])
        else:
            mensaje_descifrado.append(parte)
    return ' '.join(mensaje_descifrado)
mensaje = input("Ingrese el mensaje a encriptar: ")
mensaje_encriptado = encriptar_mensaje(mensaje)
print("Mensaje encriptado:", mensaje_encriptado)


mensaje_descifrado = descifrar_mensaje(mensaje_encriptado)
print(f"Mensaje descifrado: {mensaje_descifrado}")

