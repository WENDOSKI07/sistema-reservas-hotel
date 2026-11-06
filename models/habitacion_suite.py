from models.habitacion import Habitacion

class HabitacionSuite(Habitacion):

    def __init__(self, numero, piso, precioBase, capacidad, tieneJacuzzi, vista):
        super().__init__(numero, piso, precioBase, capacidad)
        self.set_tieneJacuzzi(tieneJacuzzi) # Ajustado para que coincida con el nombre del método de abajo
        self.set_vista(vista)
        # Valores de recargo internos del sistema
        self.__recargoJacuzzi = 50000
        self.__recargoVista = 30000

    def get_tieneJacuzzi(self):
        return self.__tieneJacuzzi

    def set_tieneJacuzzi(self, tieneJacuzzi):
        if isinstance(tieneJacuzzi, bool):
            self.__tieneJacuzzi = tieneJacuzzi
        else:
            raise ValueError("El valor de jacuzzi debe ser Verdadero (True) o Falso (False).")

    def get_vista(self):
        return self.__vista

    def set_vista(self, vista):
        if (vista is not None and isinstance(vista, str) and len(vista.strip()) > 0):
            self.__vista = vista
        else:
            raise ValueError("La descripción de la vista no puede estar vacía.")

    # Se sobrescriben los métodos
    def calcularTarifa(self, noches):
        tarifaDiaria = self.get_precioBase()
        if self.get_tieneJacuzzi():
            tarifaDiaria += self.__recargoJacuzzi
        if self.get_vista():
            tarifaDiaria += self.__recargoVista
        return tarifaDiaria * noches

    def describir_servicios(self):
        servicios = "Servicios básicos"
        if self.get_tieneJacuzzi():
            servicios += ", jacuzzi"
        if self.get_vista():
            servicios += f", excelente vista a {self.get_vista()}"
        return servicios + "."

    def mostrar_informacion(self):
        jacuzzi_texto = "Sí" if self.get_tieneJacuzzi() else "No"
        return f"{super().mostrar_informacion()} - Jacuzzi: {jacuzzi_texto} - Vista: {self.get_vista()}"