a=True
b="c"

try:
    print(a/b)
    
except BaseException as e: #clase padre de los errores es la mas general capturo todos los errores 
    print(f"Ocurrio un error de tipo {e} {type(e)}")
    
    
print("\n=================================================mi propia clase de error mi propia clas de error================================================================================================")    
#mi propia clas de error

class MiError(Exception):
    
    def __init__(self, mensaje):
        self.mensaje=mensaje
        
        
#vamos a usarla
try:
    c=int(input("ingrese un numero: "))
    d=int(input("ingrese otro numero: "))
    if c==d:
        raise MiError("Los numeros son iguales")
    
    
    
    
        
except BaseException as e:
    print(f"ocurrio un error de tipo {e} {type(e)}")
    
else:
    print("no hubo errores")
    
    
lista=[1,2,3,4,5,6,7,8,9,10]
print(lista[::-1])