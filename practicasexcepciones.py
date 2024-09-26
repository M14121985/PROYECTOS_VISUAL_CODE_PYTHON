class MiClaseExcepcion(Exception):
    def __init__(self, mensaje):
        self.mensaje=mensaje




def evaluacion(nota):
    if nota < 0:
        raise MiClaseExcepcion("la nota nunca puede ser un valor negativo, estas suspenso en cualquier caso.") #puedo usar cualquier clase de eror que quiera ya definido en python.
    #se añade el mensaje de error que se quiere mostrar, o como EN ESTE CASO   CREAR MI PROPIA CLASE DE ERROR
    elif nota <=4:
        print("suspenso")
        
    elif nota ==5:
        print("suficiente")
        
    elif nota ==6:
        print("bien")
    
    elif nota ==7:
        print("notable")
    
    elif nota ==8:
        print("notable")
    
    elif nota ==9:
        print("sobresaliente")
    else:
        print("matricula de honor")
        
        


print("\n")


evaluacion(-7)