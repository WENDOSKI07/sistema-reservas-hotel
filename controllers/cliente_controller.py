"""Conecta el área de clientes con los modelos del hotel."""

from exceptions.hoteleras import HotelError
from models.cliente import Cliente


class ClienteController:
    """Coordina el registro y la búsqueda de clientes."""

    def __init__(self, hotel, vista):
        self.hotel = hotel
        self.vista = vista

    def iniciar(self):
        """Mantiene abierto el área de clientes hasta que se elija volver."""
        while True:
            opcion = self.vista.mostrar_menu()
            if opcion == "0":
                return
            if opcion == "1":
                self.registrar_cliente()
            elif opcion == "2":
                self.buscar_cliente()
            else:
                self.vista.mostrar_mensaje("Opción inválida, selecciona 1, 2 o 0")

    def registrar_cliente(self):
        """Crea el cliente con los datos de la vista y lo registra en el hotel."""
        documento, nombre, correo = self.vista.pedir_datos_cliente()
        try:
            # El modelo valida los datos antes de que el hotel guarde el cliente
            cliente = Cliente(documento, nombre, correo)
            self.hotel.registrar_cliente(cliente)
        except (HotelError, ValueError) as error:
            self.vista.mostrar_mensaje(str(error))
            return

        self.vista.mostrar_mensaje("Cliente registrado correctamente")
        self.vista.mostrar_cliente(cliente)

    def buscar_cliente(self):
        """Consulta el hotel usando el documento ingresado."""
        documento = self.vista.pedir_documento()
        try:
            cliente = self.hotel.buscar_cliente(documento)
        except (HotelError, ValueError) as error:
            # Mostramos el error y dejamos que el usuario siga usando el menú
            self.vista.mostrar_mensaje(str(error))
            return

        self.vista.mostrar_cliente(cliente)
