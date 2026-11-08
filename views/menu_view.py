"""Entradas y mensajes del menú principal."""


class MenuView:
    def mostrar_menu(self):
        print("\nSistema de reservas del hotel")
        print("1. Cotizar habitaciones")
        print("0. Salir")
        return input("Selecciona una opción: ").strip()

    def pedir_noches(self):
        return input("¿Cuántas noches deseas alojarte? ").strip()

    def mostrar_mensaje(self, mensaje):
        print(mensaje)

