# Profundizando en el tipo str

# caracteres de escape
resultado = 'Hola \' Mundo'
print(f'Resultado: {resultado}')

resultado = 'Se va a eliminar el punto.\b\b\b'
print(f'Resultado: {resultado}')

# Caracter \
resultado = 'c:\\nuevo\\juan'
print(f'Resultado: {resultado}')

# raw string
resultado = r'Cadena con \n salto de línea'
print(f'Resultado: {resultado}')

resultado = R'c:\nuevo\juan'
print(f'Resultado: {resultado}')



#unpacking de valores
valor=(1,2,3)

valor1, valor2, valor3 = valor

print(valor1)
print(valor2)
print(valor3)
print("==========================================================multiples valores en una variable=============================================================")
print("\n")
valor_1, *valor_2, valor_3 = (1,2,3,4,5,6,7,8,9,10) #el valor_2 toma del 2 al 9
print(valor_1)
print(valor_2)
print(valor_3)
print("\n")
#unpacking de listas
mi_lista=["naranja","manzana","pera","uva","sandia","melon","papaya","piña","mango","platano","coco","kiwi","fresa","cereza","durazno","ciruela","mandarina","limon","lima","toronja","aguacate"]
lista1, lista2, lista3 = mi_lista[:8], mi_lista[8:16], mi_lista[16:]
print(lista1)
print(lista2)
print(lista3)