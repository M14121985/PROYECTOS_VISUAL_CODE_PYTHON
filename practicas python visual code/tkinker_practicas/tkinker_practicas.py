#from tkinter import *

"""# Crear la ventana principal
ventana = Tk()
ventana.title("Hola Mundo")
ventana.geometry("300x300")

# Etiqueta de saludo
etiqueta = Label(ventana, text="Hola Mundo", font=("Arial", 14))
etiqueta.pack()

# Botón para salir
boton_salir = Button(ventana, text="Salir", command=ventana.quit)
boton_salir.pack()

# Botones adicionales usando grid
boton1 = Button(ventana, text="Presionar", width=10, height=5, bg="blue", fg="white")
boton1.grid(row=0, column=0)

boton2 = Button(ventana, text="Presionar", width=10, height=5, bg="red", fg="white")
boton2.grid(row=0, column=1)

boton3 = Button(ventana, text="Presionar", width=10, height=5, bg="green", fg="white")
boton3.grid(row=0, column=2)
#si usamos metodo pack()
# Campo de entrada
entrada = Entry(ventana)
entrada.pack()

# Iniciar el bucle principal de la ventana
ventana.mainloop()""" 

#no se puede usar grid() para acomodar los botones
from tkinter import *

ventana = Tk()
ventana.title("Hola Mundo")
ventana.geometry("300x300")

etiqueta = Label(ventana, text="Hola Mundo", font=("Arial", 14))
etiqueta.pack()

boton_salir = Button(ventana, text="Salir", command=ventana.quit)
boton_salir.pack()

# Utilizamos pack() para todos los botones
boton1 = Button(ventana, text="Presionar", width=10, height=5, bg="blue", fg="white")
boton1.pack(side=LEFT)

boton2 = Button(ventana, text="Presionar", width=10, height=5, bg="red", fg="white")
boton2.pack(side=LEFT)

boton3 = Button(ventana, text="Presionar", width=10, height=5, bg="green", fg="white")
boton3.pack(side=LEFT)

entrada = Entry(ventana)
entrada.pack()

ventana.mainloop()
