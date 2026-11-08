"""Pruebas de los errores que pueden ocurrir en el hotel."""

import unittest

from exceptions.hoteleras import (
    HotelError,
    FechasInvalidasError,
    CapacidadExcedidaError,
    HabitacionNoDisponibleError,
    HabitacionNoEncontradaError,
    ClienteNoEncontradoError,
)


class TestExcepcionesHoteleras(unittest.TestCase):
    def test_errores_se_capturan_con_hotel_error(self):
        tipos_error = (
            FechasInvalidasError,
            CapacidadExcedidaError,
            HabitacionNoDisponibleError,
            HabitacionNoEncontradaError,
            ClienteNoEncontradoError,
        )
        # Un mismo except HotelError puede manejar cualquiera de estos errores
        for tipo_error in tipos_error:
            with self.subTest(tipo_error=tipo_error.__name__):
                with self.assertRaises(HotelError):
                    raise tipo_error()

    def test_hotel_error_hereda_de_exception(self):
        self.assertTrue(issubclass(HotelError, Exception))

    def test_mensaje_de_fechas_invalidas(self):
        error = FechasInvalidasError()
        self.assertIn("fecha de salida", str(error))
        self.assertIn("posterior", str(error))

    def test_mensaje_de_capacidad_excedida(self):
        error = CapacidadExcedidaError()
        self.assertIn("huéspedes", str(error))
        self.assertIn("capacidad", str(error))

    def test_mensaje_de_habitacion_no_disponible(self):
        error = HabitacionNoDisponibleError()
        self.assertIn("habitación", str(error))
        self.assertIn("no está disponible", str(error))

    def test_mensaje_de_habitacion_no_encontrada(self):
        error = HabitacionNoEncontradaError()
        self.assertIn("No se encontró una habitación", str(error))
        self.assertIn("número", str(error))

    def test_mensaje_de_cliente_no_encontrado(self):
        error = ClienteNoEncontradoError()
        self.assertIn("No se encontró un cliente", str(error))
        self.assertIn("documento", str(error))
