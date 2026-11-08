"""Pruebas de la clase Hotel."""

from datetime import date
import unittest

from exceptions.hoteleras import ClienteNoEncontradoError, HabitacionNoEncontradaError
from models.cliente import Cliente
from models.habitacion_sencilla import HabitacionSencilla
from models.habitacion_suite import HabitacionSuite
from models.hotel import Hotel


class TestHotel(unittest.TestCase):
    """Revisa el registro, las búsquedas y la creación de reservas."""

    def setUp(self):
        # Cada prueba empieza con un hotel que ya tiene un cliente y una habitación
        self.hotel = Hotel("Hotel Manizales")
        self.cliente = Cliente("123", "Ana Torres", "ana@correo.com")
        self.habitacion = HabitacionSencilla("101", "1", 100000, 2, "doble")
        self.hotel.registrar_cliente(self.cliente)
        self.hotel.registrar_habitacion(self.habitacion)

    # Constructor

    def test_crea_hotel_con_nombre_valido(self):
        self.assertEqual(self.hotel.nombre, "Hotel Manizales")

    def test_nombre_vacio_lanza_error(self):
        with self.assertRaises(ValueError):
            Hotel("   ")

    # Registrar habitaciones y clientes

    def test_registrar_habitacion_la_agrega(self):
        suite = HabitacionSuite("201", "2", 200000, 4, True, "montaña")
        self.hotel.registrar_habitacion(suite)
        self.assertEqual(len(self.hotel.habitaciones), 2)
        self.assertIn(suite, self.hotel.habitaciones)

    def test_registrar_habitacion_repetida_lanza_error(self):
        repetida = HabitacionSencilla("101", "1", 90000, 1, "sencilla")
        with self.assertRaises(ValueError):
            self.hotel.registrar_habitacion(repetida)

    def test_registrar_cliente_lo_agrega(self):
        otro = Cliente("456", "Luis Gómez", "luis@correo.com")
        self.hotel.registrar_cliente(otro)
        self.assertIn(otro, self.hotel.clientes)

    def test_registrar_cliente_repetido_lanza_error(self):
        repetido = Cliente("123", "Otra Persona", "otra@correo.com")
        with self.assertRaises(ValueError):
            self.hotel.registrar_cliente(repetido)

    def test_las_listas_no_se_cambian_desde_afuera(self):
        # La propiedad entrega una copia, así que cambiarla no toca la lista del hotel
        copia = self.hotel.habitaciones
        copia.clear()
        self.assertEqual(len(self.hotel.habitaciones), 1)

    # Búsquedas

    def test_buscar_habitacion_la_encuentra(self):
        encontrada = self.hotel.buscar_habitacion(" 101 ")
        self.assertIs(encontrada, self.habitacion)

    def test_buscar_habitacion_inexistente_lanza_excepcion(self):
        with self.assertRaises(HabitacionNoEncontradaError):
            self.hotel.buscar_habitacion("999")

    def test_buscar_cliente_lo_encuentra(self):
        encontrado = self.hotel.buscar_cliente("123")
        self.assertIs(encontrado, self.cliente)

    def test_buscar_cliente_inexistente_lanza_excepcion(self):
        with self.assertRaises(ClienteNoEncontradoError):
            self.hotel.buscar_cliente("000")

    def test_el_hotel_sigue_funcionando_despues_de_un_error(self):
        try:
            self.hotel.buscar_cliente("000")
        except ClienteNoEncontradoError:
            pass
        # Después de atrapar el error se puede seguir buscando con normalidad
        self.assertIs(self.hotel.buscar_cliente("123"), self.cliente)

    # Crear reservas

    def test_crear_reserva_la_guarda_y_la_devuelve(self):
        reserva = self.hotel.crear_reserva(
            "R001", self.cliente, self.habitacion,
            date(2026, 11, 10), date(2026, 11, 12), 2,
        )
        self.assertIn(reserva, self.hotel.reservas)
        # Dos noches a 100000 cada una
        self.assertEqual(reserva.calcular_total(), 200000)

    def test_crear_reserva_con_cliente_no_registrado_lanza_excepcion(self):
        desconocido = Cliente("789", "Sin Registro", "sin@correo.com")
        with self.assertRaises(ClienteNoEncontradoError):
            self.hotel.crear_reserva(
                "R002", desconocido, self.habitacion,
                date(2026, 11, 10), date(2026, 11, 12), 1,
            )
        # La reserva fallida no debe quedar guardada
        self.assertEqual(len(self.hotel.reservas), 0)

    def test_crear_reserva_con_habitacion_no_registrada_lanza_excepcion(self):
        no_registrada = HabitacionSencilla("305", "3", 80000, 1, "sencilla")
        with self.assertRaises(HabitacionNoEncontradaError):
            self.hotel.crear_reserva(
                "R003", self.cliente, no_registrada,
                date(2026, 11, 10), date(2026, 11, 12), 1,
            )
        self.assertEqual(len(self.hotel.reservas), 0)


if __name__ == "__main__":
    unittest.main()