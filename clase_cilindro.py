from math import *

class Cilindro():
    """esta es la clase cilindro teiene un radio, una altura y un color, y metodos para calcular el volumen y el area de la superficie del cilindro."""
    
    def __init__(self, radio, altura, color):
        self.radio=radio
        self.altura=altura
        self.color=color
    
        
    def volumen(self):
        return pi*self.radio**2*self.altura
    
    def area(self):
        return 2*pi*self.radio*(self.radio+self.altura)
    
    def __str__(self):
        return "estos son los datos del cilindro\nCilindro de radio %.2f, altura %.2f, color %s" % (self.radio, self.altura, self.color) 
    
    @classmethod
    def tanque_cilindro(cls):
        altura=10
        radio=5 
        color="verde"
        return cls(radio,altura,color)
    
    @staticmethod
    def are_iqual(cilindro1, cilindro2):
        if cilindro1.radio==cilindro2.radio:
            return True
        else:
            return False
    
if __name__=="__main__":
    
    
      #creamos un objeto de la clase cilindro  
    mi_cilindro1=Cilindro(3,5,"rojo")
    cilindro1=Cilindro(3,5,"verde")
    cilindro2=Cilindro(13,5,"azul")
    #================================================================================#
    
    print(mi_cilindro1)
    print(mi_cilindro1.__dict__) #muestra los atributos del objeto AUNQUE SEAN PIVADOS
    print(mi_cilindro1.__doc__)
    tanque1=Cilindro.tanque_cilindro()
    print(tanque1)
    print(Cilindro.are_iqual(mi_cilindro1, cilindro1))