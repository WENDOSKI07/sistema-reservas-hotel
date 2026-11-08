"""Interacción por consola para reservas y facturación."""


class ReservaView:
    def mostrar_menu(self):
        print("\nReservas y facturas")
        print("1. Crear y confirmar reserva")
        print("2. Consultar reservas")
        print("3. Emitir o consultar factura")
        print("4. Cancelar reserva")
        print("0. Volver al menú principal")
        return input("Selecciona una opción: ").strip()

    def pedir_datos_reserva(self):
        print("Primero registra el cliente en el área Clientes")
        codigo = input("Código de reserva: ").strip()
        documento = input("Documento del cliente: ").strip()
        numero = input("Número de habitación: ").strip()
        entrada = input("Entrada (AAAA-MM-DD): ").strip()
        salida = input("Salida (AAAA-MM-DD): ").strip()
        huespedes = input("Cantidad de huéspedes: ").strip()
        return codigo, documento, numero, entrada, salida, huespedes

    def pedir_codigo_reserva(self):
        return input("Código de reserva: ").strip()

    def mostrar_reserva(self, reserva):
        print(reserva.mostrar_informacion())
        print()

    def mostrar_mensaje(self, mensaje):
        print(mensaje)
