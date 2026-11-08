"""Coordina las consultas de habitaciones del hotel."""


class HabitacionController:
    """Une la vista de habitaciones con el modelo Hotel."""

    def __init__(self, hotel, vista):
        # Recibe objetos ya creados: el hotel con sus datos y la vista de consola
        self.__hotel = hotel
        self.__vista = vista

    def iniciar(self):
        """Mantiene abierto el área de habitaciones hasta que se elija volver."""
        while True:
            opcion = self.__vista.mostrar_menu()
            if opcion == "0":
                return
            if opcion == "1":
                self.listar_habitaciones()
            elif opcion == "2":
                self.mostrar_detalle()
            elif opcion == "3":
                self.mostrar_recorrido()
            else:
                self.__vista.mostrar_mensaje("Opción inválida, selecciona 1, 2, 3 o 0")

    def listar_habitaciones(self):
        """Pide al hotel sus habitaciones y se las entrega a la vista."""
        habitaciones = self.__hotel.habitaciones
        if len(habitaciones) == 0:
            self.__vista.mostrar_mensaje("El hotel todavía no tiene habitaciones registradas")
            return
        self.__vista.mostrar_habitaciones(habitaciones)

    def mostrar_detalle(self):
        """Busca una habitación por número y muestra su información."""
        numero = self.__vista.pedir_numero()
        # Si el número no existe, Hotel lanza HabitacionNoEncontradaError
        # El controlador no la atrapa: la captura el menú principal, como acordó el equipo
        habitacion = self.__hotel.buscar_habitacion(numero)
        self.__vista.mostrar_detalle(habitacion)

    def mostrar_recorrido(self):
        """Muestra servicios y tarifa de todas las habitaciones con polimorfismo."""
        noches = self.__vista.pedir_noches()
        self.__vista.mostrar_mensaje(f"\nTarifas para {noches} noche(s)")
        # Una sola lista y un solo for: cada habitación responde según su tipo, sin if
        for habitacion in self.__hotel.habitaciones:
            servicios = habitacion.describir_servicios()
            tarifa = habitacion.calcular_tarifa(noches)
            self.__vista.mostrar_tarifa(habitacion.numero, servicios, tarifa)