"""Pruebas del recorrido de una reserva hasta su factura."""

from datetime import date
from decimal import Decimal
from importlib.util import find_spec
import unittest

from exceptions.hoteleras import (
    CapacidadExcedidaError,
    FechasInvalidasError,
    HabitacionNoDisponibleError,
)
from models.factura import Factura
from models.habitacion_sencilla import HabitacionSencilla


# Estas pruebas necesitan las clases reales que están desarrollando las compañeras
MODELOS_DISPONIBLES = all(
    find_spec(nombre) is not None
    for nombre in ("models.cliente", "models.hotel", "models.reserva")
)


@unittest.skipUnless(
    MODELOS_DISPONIBLES,
    "Pendiente integrar Cliente, Hotel y Reserva",
)
class TestIntegracionReservas(unittest.TestCase):
    def setUp(self):
        from models.cliente import Cliente
        from models.hotel import Hotel

        self.hotel = Hotel("Hotel de prueba")
        self.cliente = Cliente("123", "Ana Torres", "ana@example.com")
        self.habitacion = HabitacionSencilla("101", "1", 100000, 2, "doble")
        self.hotel.registrar_cliente(self.cliente)
        self.hotel.registrar_habitacion(self.habitacion)

    def crear_reserva(self, codigo="R001", huespedes=2):
        """Reserva dos noches con una habitación y un cliente registrados."""
        return self.hotel.crear_reserva(
            codigo, self.cliente, self.habitacion,
            date(2026, 11, 10), date(2026, 11, 12), huespedes,
        )

    def test_reserva_calcula_alojamiento_y_factura(self):
        reserva = self.crear_reserva()
        factura = Factura("F001", reserva)

        self.assertEqual(reserva.calcular_total(), 200000)
        self.assertEqual(factura.subtotal, Decimal("200000.00"))
        self.assertEqual(factura.impuesto, Decimal("38000.00"))
        self.assertEqual(factura.total, Decimal("238000.00"))

    def test_confirmar_impide_reservar_la_misma_habitacion(self):
        self.crear_reserva()

        with self.assertRaises(HabitacionNoDisponibleError):
            self.crear_reserva(codigo="R002")

    def test_cancelar_libera_la_habitacion(self):
        reserva = self.crear_reserva()
        reserva.cancelar()

        nueva_reserva = self.crear_reserva(codigo="R002")
        self.assertEqual(nueva_reserva.calcular_total(), 200000)

    def test_rechazar_capacidad_no_ocupa_la_habitacion(self):
        with self.assertRaises(CapacidadExcedidaError):
            self.crear_reserva(huespedes=3)

        # Después del rechazo todavía debe ser posible hacer una reserva válida
        reserva = self.crear_reserva()
        self.assertEqual(reserva.calcular_total(), 200000)

    def test_rechazar_fechas_no_ocupa_la_habitacion(self):
        with self.assertRaises(FechasInvalidasError):
            self.hotel.crear_reserva(
                "R001", self.cliente, self.habitacion,
                date(2026, 11, 12), date(2026, 11, 10), 2,
            )

        reserva = self.crear_reserva()
        self.assertEqual(reserva.calcular_total(), 200000)
