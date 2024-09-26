from tkinter import *


"""IMPORTO LA LIBRERIA TKINTER PARA LA INTERFAZ GRAFICA CON *  LO QUE CONTIENE LA LIBRERIA TKINTER Y NO TENGO QUE USAR 
DOT NOTATION PARA ACCEDER A LOS METODOS Y CLASES DE LA LIBRERIA TKINTER

"""



class CalculadoraModel:
    """Clase que representa el modelo de la calculadora."""
    
    
    def __init__(self):
        """Inicializa el modelo de la calculadora."""
        self.resultado = ""






    def calcular(self, operacion):
        """
        Calcula el resultado de la operación ingresada.

        Parameters:
            operacion (str): La operación a calcular.

        Returns:
            None
        """
        try:
            self.resultado = str(eval(operacion))#eval evalua la operacion y la resuelve (OPERACION DE CADENA,STR A NUMERO INT). 
            #EVAL() ES UNA FUNCION DE PYTHON QUE EVALUA UNA EXPRESION DADA Y LA EJECUTA (EVALUA LA EXPRESION Y LA EJECUTA EJEMPLO: eval("2+2") = 4) Y SON OPERACIONES DE CADENA
            #las operaciones se resuelven con eval en ((((((PYTHON)))))) no hace falta hacer un switch case con distintas operaciones
        except Exception as e:
            self.resultado = f"Error {e} tipo de eror: {type(e)}"
            #si hay un error se imprime el error en la interfaz gráfica podrtiamos implementar una clase propia de algun error pero no es realmente necesario






class CalculadoraView:
    """Clase que representa la vista de la calculadora."""
    
    def __init__(self, ventana_interfaz):
        """Inicializa la vista de la calculadora."""
        
        
        self.ventana_interfaz = ventana_interfaz
        self.ventana_interfaz.title("Calculadora ALUMNO VAZQUEZ ZUBIMENDI MATIAS GONZALO.")
        
        #  color de fondo y transparencia
        self.ventana_interfaz.configure(bg='#8a8685')
        self.ventana_interfaz.attributes('-alpha', 0.9)

        self.frame = Frame(self.ventana_interfaz, bg='#8a8685')
        self.frame.pack()

        self.label = Label(self.frame, text="Resultado:", bg='#8a8685', fg='white')
        self.label.grid(row=0, column=0)

        self.resultado_var = StringVar()
        self.resultado_entry = Entry(self.frame, textvariable=self.resultado_var, state='disabled')
        #aumentar tamaño de la entrada asi leemos los numeros y errores mas facil
        self.resultado_entry.config(width=30)
        self.resultado_entry.grid(row=0, column=1, columnspan=3)
        

        #lista de botones
        self.botones = [
            '7', '8', '9', '/',
            
            '4', '5', '6', '*',
            
            '1', '2', '3', '-',
            
            '0', '.', '=', '+', 'C'  
            ]

        self.row = 1#fila
        self.column = 0#columna
        for boton in self.botones:#recorre la lista de botones
            self.crear_boton(boton)#crea el boton en la interfaz gráfica








    def crear_boton(self, valor):
        """Crea un botón en la interfaz gráfica."""
        Button(
            self.frame,
            text=valor,
            width=15,
            command=lambda: self.boton_presionado(valor),
            bg='#8a8685',
            fg='white'
            
        ).grid(row=self.row, column=self.column)
        self.column += 1
        if self.column > 3:#si la columna es mayor a 3 se reinicia la columna y se suma 1 a la fila
            self.column = 0#reinicia la columna
            self.row += 1#suma 1 a la fila









    def boton_presionado(self, valor):
        """
        Maneja la acción cuando se presiona un botón en la calculadora.

        Parameters:
            valor (str): El valor del botón presionado.

        Returns:
            None
        """
        if valor == '=':
            self.resultado_var.set(self.modelo.resultado)  
        elif valor == 'C':
            self.resultado_var.set('')  # Borrar todo el contenido
        else:
            self.resultado_var.set(self.resultado_var.get() + valor)





class CalculadoraController:
    """Clase que representa el controlador de la calculadora."""
    def __init__(self, ventana_interfaz):
        """Inicializa el controlador de la calculadora."""
        self.ventana_interfaz = ventana_interfaz
        self.modelo = CalculadoraModel()
        self.vista = CalculadoraView(ventana_interfaz)

        # Conectar la vista con el controlador
        self.vista.boton_presionado = self.boton_presionado




    def boton_presionado(self, valor):
        """
        Maneja la acción cuando se presiona un botón en la calculadora.

        Parameters:
            valor (str): El valor del botón presionado.

        Returns:
            None
        """
        if valor == '=':
            self.modelo.calcular(self.vista.resultado_var.get())
            self.vista.resultado_var.set(self.modelo.resultado)  
        elif valor == 'C':
            self.vista.resultado_var.set('')  # Borrar todo el contenido
        else:
            self.vista.resultado_var.set(self.vista.resultado_var.get() + valor)






#PROBANDO MODULO
#print(__name__) 

"""

aqui se imprime __main__ porque se esta ejecutando el modulo calculadora.py en el modulo  al que importemos
este script ,  se imprimira el nombre del modulo es decir calculadora

"""


if __name__ == "__main__":
    print("modulo calculadora.py ejecutado directamente")#si se ejecuta el modulo calculadora.py se imprime esto :)
    ventana_interfaz = Tk()
    app = CalculadoraController(ventana_interfaz)
    ventana_interfaz.mainloop()
else:
    print("modulo calculadora importado, calculadora.py :)")#si se importa el modulo calculadora.py se imprime esto :) 
