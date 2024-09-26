def numero_par(numero):
    return numero%2==0

numeros = [1,2,3,4,5,6,7,8,9,10]

resultado=list(map(numero_par, numeros))
print(resultado)

resultado2=list(filter(numero_par, numeros))
print(resultado2)   
print("=====================================================================================================")

numeros2=[45,78,82,34,65,23,56,89,90,12,34,56,78,90,23,45,67,89,90,12,34,56,78,90,23,45,67,89,90,12,34,56,78,
          90,23,45,67,89,90,12,34,56,78,90,23,45,67,89,90,12,34,56,78,90,23,45,67,89,90,12,34,56,78,90,23,45,
          67,89,90,12,34,56,78,90,23,45,67,89,90,12,34,56,78,90,23,45,67,89,90,12,34,56,78,90,23,45,67,89,90,
          12,34,56,78,90,23,45,67,89,90,12,34,56,78,90,23,45,67,89,90,12,34,56,78,90,23,45,67,89,90,12,34,56,78,90,23,45,67,89,90]
 
print(f"el resultado es {list(filter(lambda i: i%2==0, numeros2))}")

texto="hola mundo, como estas, espero que bien, yo estoy muy bien, gracias por preguntar"
lista_map=list(map(lambda i:i.upper(), texto))
print(lista_map)
################
print("=====================================================================================================")
def convertir_a_mayusculas(texto):
    resultado = []
    for i in texto:
        resultado.append(i.upper())
    return resultado

texto1 = "La Guardia Civil ha detenido a 16 personas por tráfico de droga en vehículos desde Melilla a Europa, Buen trabajo COMPAÑEROS!!!"
resultado = convertir_a_mayusculas(texto1)
print(resultado)