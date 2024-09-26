

frase="Hola, ¿cómo estás?"
contador=0
lista=[]


for letra in frase:
    lista.append(letra)
    contador+=1
print("la letra {} es el contador {}".format(letra, contador))
print(lista)


frase2="Hola, ¿cómo estás python?"
nuevalista= [i for i in frase2]
print(nuevalista)

frase3="Hola, ¿cómo estás javascript ?"
lista1=frase3.split(" ")
print(lista1)
print(len(lista1))

print("=================================1=========================================")

matriz=[[1,2,3],
        [4,5,6],
        [7,8,9]
        ]

for fila in matriz:
    for columna in fila:
        print(columna, end=",")
    print("\n")
print("\nfin del programa")


pt=["s", "m", "i", "l", "e", "s"]

i=0 
lista_while=[] 
while i<len(pt):
    lista_while+=pt[i]
    i+=1
print(lista_while, i)

lsta2=list(map(lambda x:x,pt))
print(lsta2)

suma=ord("a")+ord("b")
print(suma)
suma2=eval("3**4")
print(suma2)

variable="hola12345"
print(variable.isalnum())
variable2="1458775523663"
print(variable2.isdigit())
variable3="holamundo"
print(variable3.isalpha())#solo letras sin espacios si no daria false