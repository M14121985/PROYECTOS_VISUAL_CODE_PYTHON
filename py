class Coche:
    def __init__(self, marca, modelo, combustible=100, nivel_aceite=100, kilometraje=0):
        self.marca = marca
        self.modelo = modelo
        self.combustible = combustible
        self.nivel_aceite = nivel_aceite
        self._kilometraje = kilometraje
        self.encendido = False

    def arrancar(self):
        if self.combustible > 0 and self.nivel_aceite > 0:
            print(f"{self.marca} {self.modelo} arrancando...")
            self.encendido = True
        else:
            print("No es posible arrancar. Revise el nivel de combustible y aceite.")

    def apagar(self):
        print(f"{self.marca} {self.modelo} apagado.")
        self.encendido = False

    def acelerar(self):
        if self.encendido:
            if self.combustible > 0:
                print(f"{self.marca} {self.modelo} acelerando...")
                self.combustible -= 10
                self.kilometraje += 10
            else:
                print("No hay suficiente combustible para acelerar.")
        else:
            print("El coche está apagado. Primero arranque el coche.")

    def frenar(self):
        print(f"{self.marca} {self.modelo} frenando...")

    def chequeo_combustible(self):
        print(f"Nivel de combustible de {self.marca} {self.modelo}: {self.combustible}%")

    def chequeo_nivel_aceite(self):
        print(f"Nivel de aceite de {self.marca} {self.modelo}: {self.nivel_aceite}%")

    @property
    def kilometraje(self):
        return self._kilometraje

    @kilometraje.setter
    def kilometraje(self, valor):
        if valor >= 0:
            self._kilometraje = valor
        else:
            raise ValueError("El kilometraje no puede ser negativo.")

    @classmethod
    def mensaje(cls):
        print("Este es un mensaje de la clase Coche.")

    @staticmethod
    def estado_combustible(nivel):
        if nivel > 50:
            return "Nivel de combustible alto."
        elif nivel > 20:
            return "Nivel de combustible medio."
        else:
            return "Nivel de combustible bajo."


class CocheElectrico(Coche):
    def __init__(self, marca, modelo, nivel_energia=100, kilometraje=0):
        super().__init__(marca, modelo, nivel_aceite=0, kilometraje=kilometraje)
        self.nivel_energia = nivel_energia

    def consumo_combustible(self):
        return 0  # Los coches eléctricos no consumen combustible

    def consumo_electrico(self):
        return 20  # Suponiendo un consumo de 20 kW/h por cada 100 km
