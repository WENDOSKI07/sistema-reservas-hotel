from models.habitacion import Habitacion

class HabitacionFamiliar(Habitacion):

    def __init__(self, numero, piso, precioBase, capacidad, camasExtra):
        super().__init__(numero, piso, precioBase, capacidad)
        self.set_camasExtra(camasExtra)
        # Valor de recargo interno
        self.__valor_camaExtra = 20000

    def get_camasExtra(self):
        return self.__camasExtra

    def set_camasExtra(self, camasExtra):
        if (camasExtra is not None and isinstance(camasExtra, int) and camasExtra >= 0):
            self.__camasExtra = camasExtra
        else:
            raise ValueError("La cantidad de camas extra debe ser un número entero mayor o igual a 0.")

    def calcular_tarifa(self, noches):
        # preciBase + camasExtra x valorCamaExtra
        tarifaDiaria = self.get_precioBase() + (self.get_camasExtra() * self.__valor_camaExtra)
        return tarifaDiaria * noches

    def describir_servicios(self):
        return f"Servicios básicos, {self.get_camasExtra()} camas extra y capacidad ampliada."

    def mostrar_informacion(self):
        return f"{super().mostrar_informacion()} - Camas Extra: {self.get_camasExtra()}"