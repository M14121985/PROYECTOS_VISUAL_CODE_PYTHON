import re 

cadena="""Simplemente agrega este código después de la sección donde insertaste los primeros datos.
Asegúrate de que la variable query esté definida y tenga el formato correcto para la inserción de datos en tu tabla."""
buscar="esté"

if re.search(buscar, cadena):
    print("Se encontró la palabra")
    
    
  #comprension de listas  
lista=[]

[lista.append(elemento) for elemento in range(0,101)]
print(lista)

texto="HOLA MUNDO"
texto2=texto.casefold()#convierte a minusculas como el lower  pero este es mas rapido 
print(texto)
print(texto2)

texto3=texto2.swapcase()#convierte las minusculas en mayusculas y viceversa
print(texto3)
print("======================================================================funciones anonimas lamnda=====================================================")

numero87=lambda numero: numero **1/2 #funcion lambda para la raiz de un numero se hace con el doble asterisco y una fraccion ejemplo raiz de 2 es **1/2, raiz de 3 es **1/3,
#raiz de 4 es **1/4 y asi sucesivamente
print(numero87(4))

suma=lambda *args:sum(args)#funcion lambda para sumar varios numeros

print(suma(1,2,3,4,5,6,7,8,9,10,200))

def multiplicar(*n):
 return n*5
  
  
  
resultadoi=(multiplicar(10,20,30,40,50,60,70,80,90,100))
print(resultadoi) 