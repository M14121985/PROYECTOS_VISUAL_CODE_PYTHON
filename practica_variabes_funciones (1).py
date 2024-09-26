def adding(x):
    var=7
    return x + var
print(adding(10))

a=10
def funcion():
    global a 
    a=4567
    print(a)
    
funcion()
resultado=funcion()
print(resultado)

