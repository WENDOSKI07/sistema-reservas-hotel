"""Entradas y mensajes del menú principal."""


class MenuView:
    def mostrar_menu(self):
        print("\nSistema de reservas del hotel")
        print("1. Cotizar habitaciones")
        print("2. Comprobaciones de la actividad")
        print("0. Salir")
        return input("Selecciona una opción: ").strip()

    def pedir_noches(self):
        return input("¿Cuántas noches deseas alojarte? ").strip()

    def mostrar_comprobaciones(self):
        print("\nComprobaciones de la actividad")
        print("1. Intentar crear una habitación sin elegir un tipo")
        print("2. Validar fechas de una estadía")
        print("0. Volver al menú principal")
        return input("Selecciona una opción: ").strip()

    def pedir_fechas(self):
        print("Usa el formato AAAA-MM-DD, por ejemplo 2026-11-10")
        entrada = input("Fecha de entrada: ").strip()
        salida = input("Fecha de salida: ").strip()
        return entrada, salida

    def mostrar_mensaje(self, mensaje):
        print(mensaje)

