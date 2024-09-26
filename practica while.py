

num=1
bandera = True

while bandera==True:
    a=0 
    b=0 
    print("1. suma de dos numeros.")
    print("2. resta de dos numeros")
    print("3. salir")
    num=int(input("selecciona una de las tres opciones.  "))
    if num ==1 or num==2 or num==3:
        if num==1:
            a=float(input("introduce un numero:  "))
            b=float(input("introduce el segundo numero:  "))
            suma= a+b
            print("la suma de los dos numeros es {} ".format(suma))
        elif num==2:
            a=float(input("introduce un numero:  "))
            b=float(input("introduce el segundo numero:  "))
            resta=a-b
            print("la resta de dos numeros es {} ".format(resta))
            
        elif num==3:
            print("saliendo")
            bandera=False
            
    else:
        print("esta no es una opcion ")