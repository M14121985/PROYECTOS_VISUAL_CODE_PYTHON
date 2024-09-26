def calculadora():
    """
    Esta función implementa una calculadora básica.
    Solicita al usuario que ingrese dos números y un operador,
    luego realiza la operación correspondiente y muestra el resultado.
    Maneja errores como la división por cero y entradas no válidas.
    """
while True:
    try:
        
        num1= int(input("ingresa el primer numero:  "))
        signo= input("ingresa +, -, *, / :   ")
        num2 = int(input("numero 2:   "))

        

        if signo == "+":
            resultado = num1 + num2
        elif signo == "-":
            resultado = num1 - num2
        elif signo == "*":
            resultado = num1 * num2
        elif signo == "/":
            if num2 == 0:
                raise ZeroDivisionError("Error: No se puede dividir por cero.")
            else:
                resultado = num1 / num2
        else:
            raise ValueError("Error: Operación inválida.")

        print("El resultado es:{}".format(resultado))

    except Exception as e:
        print("Error: Ingresa números o signo de operacion válidos.",e, type(e))
   
    try:
        # Variable para salir del bucle   
        salir = input("¿Quiere salir? s/n ")
        if salir.lower() == "s":
            break
        elif salir.lower() != "n":
            print("Error: Ingrese 's' o 'n'")
    except Exception as e:
        print("Error: Ocurrió una excepción", e, type(e))




# Llamamos a la función para ejecutar la calculadora
calculadora()
