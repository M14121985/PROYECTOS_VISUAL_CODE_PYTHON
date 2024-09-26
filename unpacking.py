lista0=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista1=[11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
lista2=[lista0, lista1]
#unpacking* desempaquetado

lista3=[*lista0, *lista1]
print(lista2)
print(lista3)
#unpacking de diccionarios

diccionario1={
    "nombre":"juan",
    "apellido":"perez",
    "edad":"30",
    "profesion": "programador"
}


diccionario2={
    
    "ciudad":"madrid",
    "pais":"españa",
    "telefono":"123456789"
}

diccionario1.update(diccionario2)
#diccionario3={**diccionario1, **diccionario2}
print(diccionario1)

#zip

lista4=["hola", "como", "estas", "yo", "estoy", "muy", "bien"]
lista5=(1, 2, 3, 4, 5, 6, 7)

lista_zip=list(zip(lista4, lista5))
print(lista_zip)