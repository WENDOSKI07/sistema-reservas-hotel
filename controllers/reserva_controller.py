"""Coordina reservas y facturas usando los objetos del hotel."""

from datetime import date
from models.factura import Factura
from exceptions.hoteleras import HotelError


class ReservaController:
    def __init__(self, hotel, vista):
        self.hotel = hotel
        self.vista = vista
        self.facturas = {}

    def iniciar(self):
        while True:
            opcion = self.vista.mostrar_menu()
            if opcion == "0":
                return
            try:
                if opcion == "1":
                    self.crear_reserva()
                elif opcion == "2":
                    self.consultar_reservas()
                elif opcion == "3":
                    self.emitir_factura()
                elif opcion == "4":
                    self.cancelar_reserva()
                else:
                    self.vista.mostrar_mensaje("Opción inválida, selecciona 1, 2, 3, 4 o 0")
            except (HotelError, ValueError) as error:
                # El error se muestra y el usuario puede intentar otra operación
                self.vista.mostrar_mensaje(str(error))

    def crear_reserva(self):
        codigo, documento, numero, entrada, salida, huespedes = self.vista.pedir_datos_reserva()
        cliente = self.hotel.buscar_cliente(documento)
        habitacion = self.hotel.buscar_habitacion(numero)
        try:
            fecha_entrada = date.fromisoformat(entrada)
            fecha_salida = date.fromisoformat(salida)
            cantidad = int(huespedes)
        except ValueError as error:
            raise ValueError("Usa fechas AAAA-MM-DD y una cantidad entera de huéspedes") from error

        reserva = self.hotel.crear_reserva(
            codigo, cliente, habitacion, fecha_entrada, fecha_salida, cantidad,
        )
        self.vista.mostrar_mensaje("Reserva confirmada correctamente")
        self.vista.mostrar_reserva(reserva)

    def consultar_reservas(self):
        if not self.hotel.reservas:
            self.vista.mostrar_mensaje("Todavía no hay reservas registradas")
            return
        for reserva in self.hotel.reservas:
            self.vista.mostrar_reserva(reserva)

    def buscar_reserva(self):
        codigo = self.vista.pedir_codigo_reserva()
        for reserva in self.hotel.reservas:
            if reserva.codigo == codigo:
                return reserva
        raise ValueError("No se encontró una reserva con ese código")

    def emitir_factura(self):
        reserva = self.buscar_reserva()
        if reserva.estado != "confirmada":
            raise ValueError("Solo se puede facturar una reserva confirmada")
        # Conservamos la factura para que consultarla otra vez no la duplique
        if reserva.codigo not in self.facturas:
            self.facturas[reserva.codigo] = Factura("F-" + reserva.codigo, reserva)
        factura = self.facturas[reserva.codigo]
        self.vista.mostrar_mensaje(factura.mostrar_detalle())

    def cancelar_reserva(self):
        reserva = self.buscar_reserva()
        reserva.cancelar()
        self.vista.mostrar_mensaje("Reserva cancelada, la habitación vuelve a estar disponible")
        if reserva.codigo in self.facturas:
            self.vista.mostrar_mensaje("La factura emitida queda como historial de la reserva cancelada")
