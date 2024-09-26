
#vazquez zubimendi matias gonzalo.


# Inicializamos una cadena para almacenar el mensaje cifrado
mensaje_cifrado = ""
posicion = list(range(0, 26))#LISTA HECHA DE FORMA MAS RAPIDA.

letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
          "k", "l", "m", "n", "o", "p", "q", "r",
          "s", "t", "u", "v", "w", "x", "y", "z"]

while True:
    # Pedimos la entrada al usuario
    mensaje = input("Ingrese su mensaje de texto a cifrar, los únicos caracteres válidos son letras de la a a la z: ")
    mensaje = mensaje.lower()

    # Inicializamos una cadena para almacenar el mensaje cifrado
    mensaje_cifrado = ""
    try:
        for letra in mensaje:
            if letra == " ":
                mensaje_cifrado += " "
            elif letra in letras:
                posicion_letra = letras.index(letra)
                mensaje_cifrado += letras[(posicion_letra + 3) % 26]  # Cifrado  con desplazamiento de 3
            else:
                raise ValueError("Carácter inválido: {}".format(letra))
        print("Mensaje cifrado:", mensaje_cifrado)
            
    except ValueError as a:
        print("caracter invalido, ingrese caracter valido, {}".format(a))
    except Exception as b:
        print("caracter invalido, ingrese caracter valido, {}".format(b))
        try:
            continua=input("quiere continuar cifrando mensajes; s/n ")
            if continua.lower()!="s":
                break
        except Exception as c:
            print("caracter invalido {}".format(c))

