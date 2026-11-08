"""Reserva que relaciona cliente, habitación y una estadía propia."""

from models.cliente import Cliente
from models.habitacion import Habitacion
from models.estadia import Estadia
from exceptions.hoteleras import CapacidadExcedidaError, HabitacionNoDisponibleError


class Reserva:
    def __init__(self, codigo, cliente, habitacion, fecha_entrada, fecha_salida,
                 cantidad_huespedes):
        if not isinstance(codigo, str) or not codigo.strip():
            raise ValueError("El código de reserva no debe estar vacío")
        if not isinstance(cliente, Cliente):
            raise ValueError("La reserva necesita un cliente válido")
        if not isinstance(habitacion, Habitacion):
            raise ValueError("La reserva necesita una habitación válida")

        # La estadía se crea dentro de la reserva, acá se aplica composición
        estadia = Estadia(fecha_entrada, fecha_salida)
        if type(cantidad_huespedes) is not int or cantidad_huespedes <= 0:
            raise ValueError("La cantidad de huéspedes debe ser un entero positivo")
        if cantidad_huespedes > habitacion.capacidad:
            raise CapacidadExcedidaError()
        if habitacion.estado.lower() != "disponible":
            raise HabitacionNoDisponibleError()

        self.__codigo = codigo.strip()
        self.__cliente = cliente
        self.__habitacion = habitacion
        self.__estadia = estadia
        self.__cantidad_huespedes = cantidad_huespedes
        self.__estado = "pendiente"

    @property
    def codigo(self):
        return self.__codigo

    @property
    def cliente(self):
        return self.__cliente

    @property
    def habitacion(self):
        return self.__habitacion

    @property
    def estadia(self):
        return self.__estadia

    @property
    def cantidad_huespedes(self):
        return self.__cantidad_huespedes

    @property
    def estado(self):
        return self.__estado

    # Conservamos las consultas usadas en la primera versión de Lizeth
    def get_codigo(self):
        return self.codigo

    def get_cliente(self):
        return self.cliente

    def get_habitacion(self):
        return self.habitacion

    def get_cantidad_huespedes(self):
        return self.cantidad_huespedes

    def get_estado(self):
        return self.estado

    def confirmar(self):
        """Ocupa la habitación después de revisar nuevamente su disponibilidad."""
        if self.estado != "pendiente":
            raise ValueError("Solo se puede confirmar una reserva pendiente")
        if self.habitacion.estado.lower() != "disponible":
            raise HabitacionNoDisponibleError()
        self.habitacion.ocupar()
        self.__estado = "confirmada"

    def cancelar(self):
        """Libera la habitación de una reserva confirmada."""
        if self.estado != "confirmada":
            raise ValueError("Solo se pueden cancelar reservas confirmadas")
        self.habitacion.liberar()
        self.__estado = "cancelada"

    def calcular_total(self):
        """Calcula el alojamiento antes del impuesto de la factura."""
        return self.habitacion.calcular_tarifa(self.estadia.calcular_noches())

    def mostrar_informacion(self):
        return (
            f"Código de reserva: {self.codigo}\n"
            f"Cliente: {self.cliente.nombre}\n"
            f"Habitación: {self.habitacion.numero} - Tipo: {self.habitacion.__class__.__name__}\n"
            f"Entrada: {self.estadia.fecha_entrada} | Salida: {self.estadia.fecha_salida}\n"
            f"Huéspedes: {self.cantidad_huespedes} | Estado: {self.estado}\n"
            f"Noches: {self.estadia.calcular_noches()}\n"
            f"Alojamiento antes de impuestos: {self.calcular_total():,.2f}"
        )
