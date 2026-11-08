"""Pruebas de las fechas y la duración de una estadía."""

from datetime import date, datetime
import unittest

from exceptions.hoteleras import FechasInvalidasError
from models.estadia import Estadia


class TestEstadia(unittest.TestCase):
    def test_guarda_las_fechas_y_calcula_las_noches(self):
        entrada = date(2026, 11, 7)
        salida = date(2026, 11, 10)
        estadia = Estadia(entrada, salida)

        self.assertEqual(estadia.fecha_entrada, entrada)
        self.assertEqual(estadia.fecha_salida, salida)
        self.assertEqual(estadia.calcular_noches(), 3)

    def test_calcula_noches_entre_meses_y_anios(self):
        casos = [
            (date(2026, 11, 30), date(2026, 12, 2), 2),
            (date(2026, 12, 31), date(2027, 1, 2), 2),
            (date(2024, 2, 28), date(2024, 3, 1), 2),
        ]
        # Probamos cambios de mes, de año y el día adicional de un año bisiesto
        for entrada, salida, noches in casos:
            with self.subTest(entrada=entrada, salida=salida):
                estadia = Estadia(entrada, salida)
                self.assertEqual(estadia.calcular_noches(), noches)

    def test_rechaza_salida_igual_o_anterior_a_la_entrada(self):
        entrada = date(2026, 11, 7)
        for salida in (entrada, date(2026, 11, 6)):
            with self.subTest(salida=salida):
                with self.assertRaises(FechasInvalidasError):
                    Estadia(entrada, salida)

    def test_rechaza_datos_que_no_sean_fechas_date(self):
        fecha_valida = date(2026, 11, 7)
        for valor in ("2026-11-07", None, 7, datetime(2026, 11, 7)):
            with self.subTest(valor=valor):
                with self.assertRaises(TypeError):
                    Estadia(valor, fecha_valida)
                with self.assertRaises(TypeError):
                    Estadia(fecha_valida, valor)

    def test_impide_cambiar_las_fechas_directamente(self):
        estadia = Estadia(date(2026, 11, 7), date(2026, 11, 10))

        # Así evitamos que después de crearla se deje una salida inválida
        with self.assertRaises(AttributeError):
            estadia.fecha_entrada = date(2026, 11, 12)
        with self.assertRaises(AttributeError):
            estadia.fecha_salida = date(2026, 11, 6)

        self.assertEqual(estadia.calcular_noches(), 3)
