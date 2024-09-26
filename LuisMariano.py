from tkinter import *

class Calculadora:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora")
        self.ventana.geometry("300x150")
        self.ventana.resizable(False, False)

        self.var1 = DoubleVar()
        self.var2 = DoubleVar()
        self.operacion = StringVar()

        frame_entrada = Frame(self.ventana)
        frame_entrada.pack(pady=5)

        Label(frame_entrada, text="Número 1:").grid(row=0, column=0)
        self.entry1 = Entry(frame_entrada, textvariable=self.var1)
        self.entry1.grid(row=0, column=1, padx=5)

        Label(frame_entrada, text="Número 2:").grid(row=1, column=0)
        self.entry2 = Entry(frame_entrada, textvariable=self.var2)
        self.entry2.grid(row=1, column=1, padx=5)

        frame_botones = Frame(self.ventana)
        frame_botones.pack(pady=5)

        Radiobutton(frame_botones, text="Suma", variable=self.operacion, value="suma", command=self.calcular).grid(row=0, column=0, padx=5)
        Radiobutton(frame_botones, text="Resta", variable=self.operacion, value="resta", command=self.calcular).grid(row=0, column=1, padx=5)
        Radiobutton(frame_botones, text="Multiplicación", variable=self.operacion, value="multiplicacion", command=self.calcular).grid(row=1, column=0, padx=5)
        Radiobutton(frame_botones, text="División", variable=self.operacion, value="division", command=self.calcular).grid(row=1, column=1, padx=5)

        self.label = Label(self.ventana, text="Resultado", font=("Arial", 14, "bold"))
        self.label.pack(pady=5)

    def calcular(self):
        operacion = self.operacion.get()
        if operacion == "suma":
            resultado = self.var1.get() + self.var2.get()
        elif operacion == "resta":
            resultado = self.var1.get() - self.var2.get()
        elif operacion == "multiplicacion":
            resultado = self.var1.get() * self.var2.get()
        elif operacion == "division":
            resultado = self.var1.get() / self.var2.get()
        self.label.config(text="Resultado: " + str(resultado))

if __name__ == "__main__":
    ventana = Tk()
    calculadora = Calculadora(ventana)
    ventana.mainloop()
