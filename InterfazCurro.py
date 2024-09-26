import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont

# Definir colores
color_fondo = "#f2f2f2"
color_boton = "#3498db"
color_texto_boton = "#ffffff"
color_marco = "#ffffff"
color_entrada = "#ffffff"
color_texto_entrada = "#000000"
color_texto = "#000000"

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Eracción de Multas Actuales")
ventana.geometry("800x600")
ventana.configure(bg=color_fondo)

# Definir fuentes (después de crear la ventana)
fuente_titulo = tkfont.Font(family="Arial", size=18, weight="bold")
fuente_subtitulo = tkfont.Font(family="Arial", size=12, weight="bold")
fuente_texto = tkfont.Font(family="Arial", size=10)

# Marco principal
marco_principal = tk.Frame(ventana, bg=color_marco, bd=2, relief="ridge")
marco_principal.pack(fill="both", expand=True, padx=10, pady=10)

# Etiqueta de título
etiqueta_titulo = tk.Label(marco_principal, text="Eracción de Multas Actuales", font=fuente_titulo, bg=color_fondo, fg=color_texto)
etiqueta_titulo.pack(pady=10)

# Etiqueta de subtítulo
etiqueta_subtitulo = tk.Label(marco_principal, text="Información de la Multa", font=fuente_subtitulo, bg=color_fondo, fg=color_texto)
etiqueta_subtitulo.pack(pady=5)

# Marco de información de la multa
marco_informacion_multa = tk.Frame(marco_principal, bg=color_marco, bd=2, relief="ridge")
marco_informacion_multa.pack(fill="both", expand=True, padx=10, pady=10)

# Etiqueta de número de multa
etiqueta_numero_multa = tk.Label(marco_informacion_multa, text="Número de Multa:", font=fuente_texto, bg=color_fondo, fg=color_texto)
etiqueta_numero_multa.grid(row=0, column=0, sticky="w", padx=5, pady=5)

# Entrada de número de multa
entrada_numero_multa = tk.Entry(marco_informacion_multa, width=20, font=fuente_texto, bg=color_entrada, fg=color_texto)
entrada_numero_multa.grid(row=0, column=1, padx=5, pady=5)

# Etiqueta de fecha de multa
etiqueta_fecha_multa = tk.Label(marco_informacion_multa, text="Fecha de Multa:", font=fuente_texto, bg=color_fondo, fg=color_texto)
etiqueta_fecha_multa.grid(row=1, column=0, sticky="w", padx=5, pady=5)

# Entrada de fecha de multa
entrada_fecha_multa = tk.Entry(marco_informacion_multa, width=20, font=fuente_texto, bg=color_entrada, fg=color_texto)
entrada_fecha_multa.grid(row=1, column=1, padx=5, pady=5)

# Etiqueta de hora de multa
etiqueta_hora_multa = tk.Label(marco_informacion_multa, text="Hora de Multa:", font=fuente_texto, bg=color_fondo, fg=color_texto)
etiqueta_hora_multa.grid(row=2, column=0, sticky="w", padx=5, pady=5)

# Entrada de hora de multa
entrada_hora_multa = tk.Entry(marco_informacion_multa, width=20, font=fuente_texto, bg=color_entrada, fg=color_texto)
entrada_hora_multa.grid(row=2, column=1, padx=5, pady=5)

# Etiqueta de monto de multa
etiqueta_monto_multa = tk.Label(marco_informacion_multa, text="Monto de Multa:", font=fuente_texto, bg=color_fondo, fg=color_texto)
etiqueta_monto_multa.grid(row=3, column=0)

# ... (resto de tu código) ...

ventana.mainloop()  # Iniciar el bucle principal de la aplicación



