from collections import Counter


texto="hola como estas yo  estoy muy bien"
texto2=texto.split()

print("\n")
print(texto2)

#join
print("\n")
texto3=" ".join(texto2)
print(f"estes es el metodo join lo contrario a split es decir convierte a cadena->  {texto3}")
lista4=["hola", "como", "estas", "yo", "estoy", "muy", "bien"]
lista5=["cristiano", "ronaldo", "es", "el", "mejor", "jugador", "del", "mundo"]
print(lista4+lista5)
lista_nueva=lista4.extend(lista5)
print(lista_nueva)
print(lista4.index("ronaldo"))
lista_numeros=[1,2,3,4,5,6,7,8,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]

print(Counter(lista_numeros)[10])
print(lista_numeros.count(10))
print(min(lista_numeros))
print(max(lista_numeros))