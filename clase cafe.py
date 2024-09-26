#alumno.vazquez zubimendi matias gonzalo.

class Cafe():
    """
    Una clase utilizada para representar un Café

    ...

    Atributos
    ----------
    __nombre : str
        una cadena privada que representa el nombre del café
    __precio : float
        un número flotante privado que representa el precio del café
    cantidad : int
        un entero que representa la cantidad de café
    tipo : str
        una cadena que representa el tipo de café

    Métodos
    -------
    nombre():
        Propiedad que devuelve el nombre del café
    nombre(otro_nombre):
        Establece el nombre del café si otro_nombre no es una cadena vacía
    precio():
        Propiedad que devuelve el precio del café
    precio(nuevo_precio):
        Establece el precio del café si nuevo_precio es mayor que el precio actual
    __str__():
        Devuelve una representación en cadena del café
    __repr__():
        Devuelve una representación más completa del café
    __add__(otro):
        Devuelve la suma de los precios de este café y otro café
    """

    def __init__(self, nombre, precio, cantidad, tipo):
        """
        Parámetros
        ----------
        nombre : str
            El nombre del café
        precio : float
            El precio del café
        cantidad : int
            La cantidad de café
        tipo : str
            El tipo de café
        """
        self.__nombre = nombre
        self.__precio = precio
        self.cantidad = cantidad
        self.tipo= tipo

    """@property######para probar acceso a metodos y atributos privados con dict o dir desactive momentaneamente el decorador###
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,otro_nombre):
        if otro_nombre!="":
            self.__nombre=otro_nombre"""

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self,nuevo_precio):
        if nuevo_precio> self.__precio:
            self.__precio=nuevo_precio
        else:
            return f" Error, no puedes establecer un precio menor al actual"



    def __str__(self):
        print("ESTE DATO SE VERA IMPRESO LLAMANDO A STR()tipo de cafe: ", self.tipo, self.__nombre, self.__precio, self.cantidad)
        return f" ESTE MENSAJE SE VERA IMPRESO LLAMANDO A PRINT(), Nombre: {self.__nombre}, Precio: {self.__precio}, Cantidad: {self.cantidad}"
       

    def __repr__(self):
        print("ESTE DATO SE VERA IMPRESO LLAMANDO A REPR(), tipo de cafe: ", self.tipo, self.__nombre, self.__precio, self.cantidad)
        mensaje=" ESTE DATO SE VERA IMPRESO LLAMADO DENTRO DE PRINT.__REPR__() nombre {} precio {} cantidad {} y tipo {}"
        return mensaje.format(self.__nombre, self.cantidad, self.__precio, self.tipo)

    def __add__(self, otro):
        return self.__precio + otro.precio

##instancias    
cafe_con_leche = Cafe("cafe con leche", 1.50, 10, "con leche")
# print(cafe_con_leche)
# cafe_con_leche.nombre = "cafe solo"
# print(cafe_con_leche)
# print(cafe_con_leche.nombre)
# print(cafe_con_leche.__dict__) #accedemos a nombre privado
# print(cafe_con_leche._Cafe__nombre) #accedemos a nombre privado
# print(cafe_con_leche._Cafe__nombre)
# cafe_con_leche._Cafe__nombre = "cafe irlandes"
# print(cafe_con_leche)
# print(cafe_con_leche._Cafe__nombre)
# print(cafe_con_leche.__doc__) #accedemos a docstring PERO SOLO DE LA CLASE
# print("=================================1====================================================================================================")
# print(dir(cafe_con_leche)) #accedemos a los metodos de la clase y a los atributos privados
# help(Cafe) #accedemos a docstring de la clase y de los METODOS
str(cafe_con_leche)
print(cafe_con_leche)
repr(cafe_con_leche)
print(cafe_con_leche.__repr__)