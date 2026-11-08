"""Controla la navegación y valida los datos de la cotización."""

from exceptions.hoteleras import HotelError


class MenuController:
    def __init__(self, vista, habitaciones, mostrar_habitaciones,
                 comprobar_clase_abstracta, validar_estadia):
        self.vista = vista
        self.habitaciones = habitaciones
        self.mostrar_habitaciones = mostrar_habitaciones
        self.comprobar_clase_abstracta = comprobar_clase_abstracta
        self.validar_estadia = validar_estadia

    def iniciar(self):
        while True:
            opcion = self.vista.mostrar_menu()
            if opcion == "0":
                self.vista.mostrar_mensaje("Hasta pronto")
                return
            if opcion == "1":
                self.cotizar_habitaciones()
            elif opcion == "2":
                self.comprobaciones()
            else:
                self.vista.mostrar_mensaje("Opción inválida, selecciona 1, 2 o 0")

    def comprobaciones(self):
        """Permite revisar casos de la actividad sin cerrar el programa."""
        while True:
            opcion = self.vista.mostrar_comprobaciones()
            if opcion == "0":
                return
            try:
                if opcion == "1":
                    self.vista.mostrar_mensaje(self.comprobar_clase_abstracta())
                elif opcion == "2":
                    entrada, salida = self.vista.pedir_fechas()
                    self.vista.mostrar_mensaje(self.validar_estadia(entrada, salida))
                else:
                    self.vista.mostrar_mensaje("Opción inválida, selecciona 1, 2 o 0")
            except (HotelError, ValueError) as error:
                # Capturamos el error para que el usuario pueda corregir y continuar
                self.vista.mostrar_mensaje(str(error))

    def cotizar_habitaciones(self):
        while True:
            try:
                noches = int(self.vista.pedir_noches())
                if noches <= 0:
                    raise ValueError
            except ValueError:
                self.vista.mostrar_mensaje("Escribe un número entero de noches mayor que cero")
                continue
            break

        self.vista.mostrar_mensaje("\nCotización de alojamiento antes de impuestos")
        self.mostrar_habitaciones(self.habitaciones, noches)

