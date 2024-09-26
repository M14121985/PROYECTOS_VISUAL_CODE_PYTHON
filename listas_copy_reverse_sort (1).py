numeros=[1,2,3,4,5,6,7]
id(numeros)
print(id(numeros))
numeros2=numeros
print(id(numeros2))
print("_____________^________________")
numeros3=numeros.copy()
print(id(numeros3))
#.copy tiene un id distinto que numeros y numeros2 que es igual a numeros, porque .copy() copiq la lista y da nuevo espacio en memoria ram por eso tiene otro id
print("______________________________")
numeros.reverse()
print(numeros)
numeros.sort()
print(numeros)
numeros.reverse()
print(numeros)
numeros.sort()
print(numeros)
