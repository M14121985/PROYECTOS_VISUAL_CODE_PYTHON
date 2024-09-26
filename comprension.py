usuarios=[
    
    [0, "Juan"],
    [1, "Pedro"],
    [2, "Maria"],
    [3, "Jose"],
    [4, "Luis"],
    [5, "Ana"],
    [6, "Elena"],
    [7, "Carlos"],
    [8, "Sofia"],
    [9, "Andres"]

]
#nombres= tuple()

#for usuario in usuarios:
    #nombres+=(usuario[0], usuario[1],)
    
#print(nombres)

nombres1=[ ]
"""for indice, usuario in enumerate(usuarios):
    nombres1.append(usuario)
print(nombres1) """
indice=0
for usuario in usuarios:
    nombres1+=indice,usuario[1]
    indice+=1
print(nombres1)

print(nombres1[0], end=",")
print(nombres1[1], end=",")
print(nombres1[2], end=",")
print(nombres1[3], end=",")
print(nombres1[4], end=",")
print(nombres1[5], end=",")
print("\n")

lista=[1,2,3,4,5,6,7,8,9,10]
print(*lista)#imprime los elementos de la lista sin corchetes ni comas desempaquetando la lista con el operador *
from examen import *

print(Yo.__name__)


squares = []
for x in range(10):
    squares.append(x**2)

print(squares)


squares1 = list(map(lambda x: x**2, range(10)))

squares2=[x**2 for x in range(21)]
print(squares1)
print(squares2)

milista=['s' , 'm', 'i', 'l', 's']

milista2="".join([i for i in milista])
print(milista2) 


lista45=[]