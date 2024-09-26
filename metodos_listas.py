
# metodo count() cuenta cuantas veces se repite un elemento en una lista

numeros = [1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10]

conteo=numeros.count(3)
print(conteo)
print("=================================1=========================================")
# metodo index() devuelve el indice de un elemento en una lista

indice=numeros.index(9)
print(indice)

print("=================================2=========================================")

# metodo reverse() invierte el orden de los elementos de una lista
numeros.reverse()
print(numeros)
print("=================================3=========================================")
# metodo sort() ordena los elementos de una lista
numeros.sort()
print(numeros)
print("=================================4=========================================")
# metodo append() añade un elemento al final de una lista
numeros.append(897)
print(numeros)
print("=================================5=========================================")
#funcion max() devuelve el elemento mayor de una lista
valor_mamximo= max(numeros)
print(valor_mamximo)
print("=================================6=========================================")
#funcion min() devuelve el elemento menor de una lista
minimo_valor=min(numeros)
print(minimo_valor)
print("=================================7=========================================")
#funcion sum() devuelve la suma de los elementos de una lista
suma_lista=sum(numeros)
print(f" la suma total de los valores de la lista es :{suma_lista}")
print("=================================8=========================================")
#funcion len() devuelve la longitud de una lista
tamaño=len(numeros)
print("el numero de elementos que hay en la lista es {}".format(tamaño))
print("=================================9=========================================")
#funcion del() elimina un elemento de una lista
lista_frutas=["manzana", "pera", "uva", "mango", "fresa"]
print(lista_frutas)
del lista_frutas[0]
print(lista_frutas)
print("=================================10=========================================")
lista_frutas[0]="platano de canarias"
print(lista_frutas)
print("=================================11=========================================")
lista_verduras=["tomate", "lechuga", "pepino", "cebolla", "pimiento"]
print(lista_verduras)
lista_verduras+=["calabacin", "berenjena"]
lista_verduras+=lista_frutas
print(lista_verduras)
print("=================================12=========================================")   
#metodo insert() añade un elemento en una posicion determinada de una lista
lista_frutas.insert(2, "kiwi")
print(lista_frutas)
print("=================================13=========================================")
#metodo remove() elimina un elemento de una lista
lista_frutas.remove("mango")
print(lista_frutas)
print("=================================14=========================================")
#metodo pop() elimina un elemento de una lista por su indice
lista_frutas.pop(0)
print(lista_frutas)
print("=================================15=========================================")
#metodo insert() añade un elemento en una posicion determinada de una lista
lista_frutas.insert(0, "kiwi")
print(lista_frutas)
print("=================================16=========================================")
#metodo extend() añade varios elementos a una lista
lista_frutas.extend(["sandia", "melon", "coco", "piña", "naranja", "mandarina", "limon", "lima", "pomelo", "toronja"])
print(lista_frutas)
print("=================================17=========================================")
print(lista_verduras)
