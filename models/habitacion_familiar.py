from models.habitacion import Habitacion

class HabitacionFamiliar(Habitacion):
    VALOR_CAMA_EXTRA = 20000

    def __init__(self, numero, piso, precio_base, capacidad, camas_extra):
        super().__init__(numero, piso, precio_base, capacidad)
        self.camas_extra = camas_extra
        # Valor de recargo interno
    
    @property
    def camas_extra(self):
        return self.__camas_extra

    @camas_extra.setter
    def camas_extra(self, valor):
        if (valor is not None and isinstance(valor, int) and valor >= 0):
            self.__camas_extra = valor
        else:
            raise ValueError("La cantidad de camas extra debe ser un número entero mayor o igual a 0.")

    def calcular_tarifa(self, noches):
        # precio_base + camas_extra x valor_cama_extra
        tarifa_diaria = self.precio_base + (self.camas_extra * HabitacionFamiliar.VALOR_CAMA_EXTRA)
        return tarifa_diaria * noches

    def describir_servicios(self):
        return f"Servicios básicos, {self.camas_extra} camas extra y capacidad ampliada."

    def mostrar_informacion(self):
        return f"{super().mostrar_informacion()} - Camas Extra: {self.camas_extra}"