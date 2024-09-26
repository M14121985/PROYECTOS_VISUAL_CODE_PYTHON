

lista1=list(range(10))
print(lista1)
texto="argentina, uruguay,brasil,chile,Mexico,estados unidos, canada"


lista2=texto.split(",")
print(lista2)
print("______________________________")
lista3=tuple(zip(lista1, lista2))
print(lista3)