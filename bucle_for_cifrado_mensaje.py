
#vazquez zubimendi matias gonzalo.

posicion = list(range(0, 26))#LISTA HECHA DE FORMA MAS RAPIDA.


letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
          "k", "l", "m", "n", "o", "p", "q", "r",
          "s", "t", "u", "v", "w", "x", "y", "z"]


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
            # el %26 es porque al llegar al final se volveria a empezar desde el 0 desbordamineto
        else:
            raise ValueError("Carácter inválido: {}".format(letra))

    print("Mensaje cifrado:", mensaje_cifrado)

except ValueError as error:
    print("caracter invalido, ingrese caracter valido, {}".format(error))

except Exception as error:
    print("caracter invalido, ingrese caracter valido, {}".format(error))