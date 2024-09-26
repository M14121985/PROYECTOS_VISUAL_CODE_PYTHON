
contador=0

while True:
    if contador <=200:
        print("Estoy en el bucle while", contador)
        contador+=1
    else:
        break

print("fin del programa")



while True:#SIMULAMOS DO WHILE ALMENOS SE EJENCUTA UNA VEZ
    entrada=input("escribe salir para salir:  ").casefold()
    if entrada=="salir":
        break
    else:
        print("Escribe salir para salir del bucle")