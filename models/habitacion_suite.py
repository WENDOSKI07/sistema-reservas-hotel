from models.habitacion import Habitacion

class HabitacionSuite(Habitacion):
    RECARGO_JACUZZI = 50000
    RECARGO_VISTA = 30000

    def __init__(self, numero, piso, precio_base, capacidad, tiene_jacuzzi, vista):
        super().__init__(numero, piso, precio_base, capacidad)
        self.tiene_jacuzzi = tiene_jacuzzi
        self.vista = vista
        
    @property    
    def tiene_jacuzzi(self):
        return self.__tiene_jacuzzi

    @tiene_jacuzzi.setter
    def tiene_jacuzzi(self, valor):
        if isinstance(valor, bool):
            self.__tiene_jacuzzi = valor
        else:
            raise ValueError("El valor de jacuzzi debe ser Verdadero (True) o Falso (False).")

    @property
    def vista(self):
        return self.__vista

    @vista.setter
    def vista(self, valor):
        if (valor is not None and isinstance(valor, str) and len(valor.strip()) > 0):
            self.__vista = valor
        else:
            raise ValueError("La descripción de la vista no puede estar vacía.")

    # Se sobrescriben los métodos
    def calcular_tarifa(self, noches):
        tarifa_diaria = self.precio_base
        if self.tiene_jacuzzi:
            tarifa_diaria += HabitacionSuite.RECARGO_JACUZZI
        if self.vista:
            tarifa_diaria += HabitacionSuite.RECARGO_VISTA
        return tarifa_diaria * noches

    def describir_servicios(self):
        servicios = "Servicios básicos"
        if self.tiene_jacuzzi:
            servicios += ", jacuzzi"
        if self.vista:
            servicios += f", excelente vista a {self.vista}"
        return servicios + "."

    def mostrar_informacion(self):
        jacuzzi_texto = "Sí" if self.tiene_jacuzzi else "No"
        return f"{super().mostrar_informacion()} - Jacuzzi: {jacuzzi_texto} - Vista: {self.vista}"