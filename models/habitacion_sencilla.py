from models.habitacion import Habitacion

class HabitacionSencilla(Habitacion):

    def __init__(self, numero, piso, precio_base, capacidad, tipo_cama):
        super().__init__(numero, piso, precio_base, capacidad)
        self.tipo_cama = tipo_cama

    @property
    def tipo_cama(self):
        return self.__tipo_cama

    @tipo_cama.setter
    def tipo_cama(self, valor):
        if (valor is not None and isinstance(valor, str) and len(valor.strip()) > 0):
            self.__tipo_cama = valor
        else:
            raise ValueError("El tipo de cama no puede estar vacío.")

    def calcular_tarifa(self, noches):
        return self.precio_base * noches

    def describir_servicios(self):
        return f"Servicios básicos y cama tipo {self.tipo_cama}."

    def mostrar_informacion(self):
        return f"{super().mostrar_informacion()} - Tipo de Cama: {self.tipo_cama}"