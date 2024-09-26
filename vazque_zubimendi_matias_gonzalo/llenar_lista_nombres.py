import copy
#para poder hacer copia profunda

nombres=[]

while True:
    try:
        nombre=input("ingresa un nombre:......  ")
        nombres.append(nombre)
    except Exception as e:
        print("Error: Ingresa un nombre válido.",e, type(e))

    try:
        #variable para salir del bucle
        salir=input("quiere salir? s/n ")
        if salir=="s":
            break
        elif salir!="n":
            raise Exception("ingrese s o n ")

    except Exception as e:
        print("Error: Ocurrió una excepción", e, type(e))


for i in range(len(nombres)):
    print( f"{i}->{nombres[i]}")

for c,v in enumerate(nombres):
    print(f"{c}->{v}")
 

nombres2=copy.deepcopy(nombres)
print(nombres2)
print(len(nombres2))
print(nombres2)