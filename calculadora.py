from tkinter import *




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
            self.resultado = str(eval(operacion))#eval evalua la operacion y la resuelve (OPERACION DE CADENA,STR A NUMERO INT)
        except Exception as e:
            self.resultado = "Error"






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
        self.resultado_entry.grid(row=0, column=1, columnspan=2)

        self.botones = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+', 'C'  
        ]

        self.row = 1
        self.column = 0
        for boton in self.botones:
            self.crear_boton(boton)








    def crear_boton(self, valor):
        """Crea un botón en la interfaz gráfica."""
        Button(
            self.frame,
            text=valor,
            width=5,
            command=lambda: self.boton_presionado(valor),
            bg='#8a8685',
            fg='white'
            
        ).grid(row=self.row, column=self.column)
        self.column += 1
        if self.column > 3:
            self.column = 0
            self.row += 1









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
    ventana_interfaz = Tk()
    app = CalculadoraController(ventana_interfaz)
    ventana_interfaz.mainloop()
else:
    print("modulo calculadora importado, calculadora.py :)")#si se importa el modulo calculadora.py se imprime esto :) 
