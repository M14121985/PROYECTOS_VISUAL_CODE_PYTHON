"""
Este archivo contiene un código que crea una interfaz gráfica de usuario utilizando la biblioteca Tkinter.
La interfaz incluye varios elementos como botones, radio buttons, check buttons, 
campos de entrada de texto, tabla, texto desplazable, slider, selector de estilo y barra de progreso.

"""

from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext

# Crear la ventana principal
ventana = Tk()
ventana.title("Interfaz con Tkinter - VAZQUEZ ZUBIMENDI MATIAS GONZALO")

# Establecer el icono de la ventana
ventana.iconbitmap("icono.ico")

# Dimensiones de la ventana
ancho = 800
alto = 400

# Obtener las dimensiones de la pantalla
ancho_pantalla = ventana.winfo_screenwidth()#obtiene el ancho de la pantalla por medio del metodo winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()#obtiene el alto de la pantalla por medio del metodo winfo_screenheight()

# Calcular la posición del centro
x = (ancho_pantalla // 2) - (ancho // 2)#divide el ancho de la pantalla entre 2 y le resta el ancho de la ventana entre 2
y = (alto_pantalla // 2) - (alto // 2)#divide el alto de la pantalla entre 2 y le resta el alto de la ventana entre 2
# Establecer las dimensiones y la posición de la ventana
ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

# Establecer la transparencia de la ventana (0.0 completamente transparente, 1.0 completamente opaco)
ventana.attributes("-alpha", 0.9)

# Función para cambiar el estado del botón de alternancia
# (oprimido o levantado)
def alternar_boton():
    if boton_alternar.config('relief')[-1] == 'sunken':
        boton_alternar.config(relief="raised")#configura el boton_alternar con relief en raised (levantado)
    else:
        boton_alternar.config(relief="sunken")#configura el boton_alternar con relief en sunken (oprimido)




# Crear y colocar los radio buttons
radio1 = Radiobutton(ventana, text="Radio Button 1", value=1)#crea un radio button con el texto "Radio Button 1" y el valor 1 para que se pueda seleccionar unicamnete uno de los radio buttons
radio1.grid(row=0, column=0, sticky='w')

radio2 = Radiobutton(ventana, text="Radio Button 2", value=2)#crea un radio button con el texto "Radio Button 2" y el valor 2 para que se pueda seleccionar unicamnete uno de los radio buttons
radio2.grid(row=1, column=0, sticky='w')

radio3 = Radiobutton(ventana, text="Radio Button 3", value=3)#crea un radio button con el texto "Radio Button 3" y el valor 3 para que se pueda seleccionar unicamnete uno de los radio buttons
radio3.grid(row=2, column=0, sticky='w')






# Crear y colocar el check button tri-estado
check_tri_estado = Checkbutton(ventana, text="Tri-state check box", tristatevalue=0)#crea un check button con el texto "Tri-state check box" y el valor 0 para que se pueda seleccionar 3 estados
check_tri_estado.grid(row=3, column=0, sticky='w')



# Crear y colocar los botones push
# (botón por defecto, botón de alternancia y botón plano)
boton_defecto = Button(ventana, text="Default Push Button")#crea un boton con el texto "Default Push Button"
boton_defecto.grid(row=0, column=1)

boton_alternar = Button(ventana, text="Toggle Push Button", command=alternar_boton)#crea un boton con el texto "Toggle Push Button" y le asigna la funcion alternar_boton
boton_alternar.grid(row=1, column=1)

boton_plano = Button(ventana, text="Flat Push Button", relief="flat")#crea un boton con el texto "Flat Push Button" y el relief en flat
boton_plano.grid(row=0, column=2)



# Crear y colocar el campo de entrada de texto
entrada_codigo = Entry(ventana)
entrada_codigo.grid(row=1, column=2)



# Crear y colocar el Spinbox para números
spinbox_numero = Spinbox(ventana, from_=0, to=100)
spinbox_numero.grid(row=2, column=2)



# Crear y colocar el campo de entrada para la fecha
entrada_fecha = Entry(ventana)
entrada_fecha.insert(0, "01/01/2000 00:00")
entrada_fecha.grid(row=3, column=2)


# Crear y colocar el check button adicional
check_grupo3 = Checkbutton(ventana, text="Group 3")
check_grupo3.grid(row=0, column=3)


# Crear y colocar la tabla (Treeview)
# (se muestra solo el encabezado)
tabla = ttk.Treeview(ventana, columns=(1, 2), show="headings", height=4)
tabla.grid(row=4, column=0, columnspan=2)



# Definir los encabezados de la tabla
# (se establecen los nombres de las columnas)
tabla.heading(1, text="1")
tabla.heading(2, text="2")


# Crear y colocar el texto desplazable
texto_desplazable = scrolledtext.ScrolledText(ventana, width=40, height=10)
texto_desplazable.grid(row=4, column=2, columnspan=2)


# Crear y colocar el slider
deslizador = Scale(ventana, from_=0, to=100, orient='horizontal')
deslizador.grid(row=5, column=0, columnspan=2, sticky='we')


# Crear y colocar el selector de estilo
etiqueta_estilo = Label(ventana, text="Style:")
etiqueta_estilo.grid(row=6, column=0)


selector_estilo = ttk.Combobox(ventana, values=["--Choose one--"])
selector_estilo.current(0)
selector_estilo.grid(row=6, column=1)


# Crear y colocar el indicador de progreso
barra_progreso = ttk.Progressbar(ventana, length=200, mode='determinate')
barra_progreso['value'] = 24
barra_progreso.grid(row=5, column=2, columnspan=2)




# Iniciar el bucle principal de la interfaz
ventana.mainloop()
