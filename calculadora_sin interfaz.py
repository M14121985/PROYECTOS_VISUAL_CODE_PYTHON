

# Programa que simula una calculadora sin interfaz gráfica

number1=int(input("Ingresa un número:"))

number2=int (input("Ingresar tu segundo número:"))

eleccion=0

while eleccion !=5:

    print("""

indique la operación a realzar:

1. suma

2. resta

3. multiplicacion

4. división

5. salir

""")

    eleccion= int(input())

    if eleccion==1:
        print("\n")
        print("Resultado:",number1,"+",number2,"=",number1+number2)

    if eleccion==2:
        print("\n")
        print("Resultado:",number1,"-",number2,"=",number1-number2)

    if eleccion==3:
        print("\n")
        print("Resultado:",number1,"*",number2,"=",number1*number2)

    if eleccion==4:
        try:
            print("\n")
            print("Resultado:",number1,"/",number2,"=",number1/number2)
        except ZeroDivisionError:
            print("Error: No se puede dividir entre 0")

    if eleccion==5:
        print("Gracias por particpar") 