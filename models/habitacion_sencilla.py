from models.habitacion import Habitacion

class HabitacionSencilla(Habitacion):

    def __init__(self, numero, piso, precioBase, capacidad, tipoCama):
        super().__init__(numero, piso, precioBase, capacidad)
        self.set_tipoCama(tipoCama)

    def get_tipoCama(self):
        return self.__tipoCama

    def set_tipoCama(self, tipoCama):
        if (tipoCama is not None and isinstance(tipoCama, str) and len(tipoCama.strip()) > 0):
            self.__tipoCama = tipoCama
        else:
            raise ValueError("El tipo de cama no puede estar vacío.")

    def calcular_tarifa(self, noches):
        return self.get_precioBase() * noches

    def describir_servicios(self):
        return f"Servicios básicos y cama tipo {self.get_tipoCama()}."

    def mostrar_informacion(self):
        return f"{super().mostrar_informacion()} - Tipo de Cama: {self.get_tipoCama()}"