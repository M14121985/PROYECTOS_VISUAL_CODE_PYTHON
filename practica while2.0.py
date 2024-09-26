

bandera=True
contador=0
while bandera ==True:
    contador+=1
    print("este es el numero {}".format(contador))
    if contador==200:
        bandera=False
        break
print(contador)