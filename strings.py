# Description: Ejercicios de strings

lista= ["hola", "mundo", "cruel"]
print(lista[::-1])
print("=================================1=========================================")
print(len(lista))
print("=================================2=========================================")
mensaje= "Hola mundo cruel"
print(len(mensaje))
print("=================================3=========================================")
b = mensaje.split(" ")
print(b)
print("=================================4=========================================")
d=" ".join(b)
print(d)
print("=================================5=========================================")
e=d.upper()
print(e)
print("=================================6=========================================")
print(f"la palabra mundo empieza en la posicion: {e.find("MUNDO")}")
print("=================================7=========================================")


##Ejercicio 2 usos funcion bool()
numero= 123456789
print(bool(numero))
print("=================================8=========================================")
cadena=""
print(bool(cadena))
print("=================================9=========================================")
#asignacion vanrias variables en una linea

a,b,c = 45,68,98
print(a)
print(b)
print(c)
print("=================================10=========================================")
nombre, apellido, edad = "juan", "perez", 23
print(nombre)
print(apellido)
print(edad)
print("=================================11=========================================")