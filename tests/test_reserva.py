"""Pruebas de las validaciones y los cambios de estado de una reserva."""

from datetime import date
import unittest

from models.cliente import Cliente
from models.habitacion_sencilla import HabitacionSencilla
from models.hotel import Hotel
from models.reserva import Reserva
from exceptions.hoteleras import FechasInvalidasError, HabitacionNoDisponibleError


class TestReserva(unittest.TestCase):
    def setUp(self):
        self.cliente = Cliente("123", "Ana", "ana@example.com")
        self.habitacion = HabitacionSencilla("101", "1", 100000, 2, "doble")
        self.entrada = date(2026, 11, 10)
        self.salida = date(2026, 11, 12)

    def crear(self, codigo="R001", huespedes=2):
        return Reserva(codigo, self.cliente, self.habitacion,
                       self.entrada, self.salida, huespedes)

    def test_confirma_cancela_y_muestra_datos_del_uml(self):
        reserva = self.crear()
        self.assertEqual(reserva.estado, "pendiente")
        reserva.confirmar()
        self.assertEqual(self.habitacion.estado, "Ocupada")
        self.assertEqual(reserva.estado, "confirmada")
        self.assertIn("Cliente: Ana", reserva.mostrar_informacion())
        reserva.cancelar()
        self.assertEqual(reserva.estado, "cancelada")
        self.assertEqual(self.habitacion.estado, "Disponible")

    def test_rechaza_huespedes_no_enteros_positivos(self):
        for cantidad in (0, -1, True, 1.5, "2"):
            with self.subTest(cantidad=cantidad):
                with self.assertRaises(ValueError):
                    self.crear(huespedes=cantidad)

    def test_revisa_fechas_antes_de_capacidad(self):
        with self.assertRaises(FechasInvalidasError):
            Reserva("R001", self.cliente, self.habitacion,
                    self.salida, self.entrada, 3)

    def test_confirmar_revisa_si_otra_reserva_ocupo_la_habitacion(self):
        primera = self.crear()
        segunda = self.crear("R002")
        primera.confirmar()
        with self.assertRaises(HabitacionNoDisponibleError):
            segunda.confirmar()
        self.assertEqual(segunda.estado, "pendiente")

    def test_cancelar_dos_veces_no_libera_una_reserva_nueva(self):
        primera = self.crear()
        primera.confirmar()
        primera.cancelar()
        segunda = self.crear("R002")
        segunda.confirmar()
        with self.assertRaises(ValueError):
            primera.cancelar()
        self.assertEqual(self.habitacion.estado, "Ocupada")

    def test_no_permite_reasignar_los_datos_de_la_reserva(self):
        reserva = self.crear()
        for atributo, valor in (("estado", "cancelada"), ("habitacion", None),
                                ("cantidad_huespedes", 10), ("estadia", None)):
            with self.subTest(atributo=atributo):
                with self.assertRaises(AttributeError):
                    setattr(reserva, atributo, valor)

    def test_codigo_repetido_no_registra_ni_ocupa_otra_habitacion(self):
        hotel = Hotel("Hotel de prueba")
        otra = HabitacionSencilla("102", "1", 90000, 1, "individual")
        hotel.registrar_cliente(self.cliente)
        hotel.registrar_habitacion(self.habitacion)
        hotel.registrar_habitacion(otra)
        hotel.crear_reserva("R001", self.cliente, self.habitacion,
                            self.entrada, self.salida, 2)
        with self.assertRaises(ValueError):
            hotel.crear_reserva(" R001 ", self.cliente, otra,
                                self.entrada, self.salida, 1)
        self.assertEqual(len(hotel.reservas), 1)
        self.assertEqual(otra.estado, "Disponible")

    def test_hotel_utiliza_los_objetos_registrados(self):
        hotel = Hotel("Hotel de prueba")
        hotel.registrar_cliente(self.cliente)
        hotel.registrar_habitacion(self.habitacion)
        copia = HabitacionSencilla("101", "1", 1, 100, "individual")
        reserva = hotel.crear_reserva("R001", self.cliente, copia,
                                       self.entrada, self.salida, 2)
        self.assertIs(reserva.habitacion, self.habitacion)
        self.assertEqual(reserva.calcular_total(), 200000)
