"""Entradas y mensajes del área de habitaciones."""


class HabitacionView:
    """Pide los datos y muestra la información de las habitaciones."""

    def mostrar_menu(self):
        """Muestra las opciones y devuelve la que elija el usuario."""
        print("\nHabitaciones")
        print("1. Listar habitaciones")
        print("2. Ver detalle de una habitación")
        print("3. Comparar tarifas de todas las habitaciones")
        print("0. Volver al menú principal")
        return input("Selecciona una opción: ").strip()

    def pedir_numero(self):
        """Pide el número de la habitación que se quiere consultar."""
        return input("Número de la habitación: ").strip()

    def pedir_noches(self):
        """Pide las noches y repite la pregunta hasta recibir un entero mayor que cero."""
        while True:
            texto = input("Número de noches: ").strip()
            # isdigit revisa que el texto tenga solo números, así int() no falla
            if texto.isdigit() and int(texto) > 0:
                return int(texto)
            print("Escribe un número entero de noches mayor que cero")

    def mostrar_habitaciones(self, habitaciones):
        """Muestra una línea con la información de cada habitación."""
        print("\nHabitaciones del hotel")
        for habitacion in habitaciones:
            # Cada tipo de habitación arma su propio texto con mostrar_informacion
            print(habitacion.mostrar_informacion())

    def mostrar_detalle(self, habitacion):
        """Muestra la información y los servicios de una habitación."""
        print()
        print(habitacion.mostrar_informacion())
        print(f"Servicios: {habitacion.describir_servicios()}")

    def mostrar_tarifa(self, numero, servicios, tarifa):
        """Muestra el resultado del recorrido polimórfico de una habitación."""
        print(f"Habitación {numero}: {servicios} Tarifa: ${tarifa:,.0f}")

    def mostrar_mensaje(self, mensaje):
        """Muestra cualquier aviso que le envíe el controlador."""
        print(mensaje)