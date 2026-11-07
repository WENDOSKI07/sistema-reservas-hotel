"""Controla la navegación y valida los datos de la cotización."""


class MenuController:
    def __init__(self, vista, habitaciones, mostrar_habitaciones):
        self.vista = vista
        self.habitaciones = habitaciones
        self.mostrar_habitaciones = mostrar_habitaciones

    def iniciar(self):
        while True:
            opcion = self.vista.mostrar_menu()
            if opcion == "0":
                self.vista.mostrar_mensaje("Hasta pronto")
                return
            if opcion == "1":
                self.cotizar_habitaciones()
            else:
                self.vista.mostrar_mensaje("Opción inválida, selecciona 1 o 0")

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

