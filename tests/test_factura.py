"""Pruebas de los importes y la salida de la factura."""

from contextlib import redirect_stdout
from decimal import Decimal
from io import StringIO
import unittest
from unittest.mock import Mock

from main import mostrar_factura
from models.factura import Factura


class ReservaDePrueba:
    """Representa una reserva con un importe conocido."""

    def calcular_total(self):
        return Decimal("250.50")


class TestFactura(unittest.TestCase):
    def test_rechaza_codigo_invalido(self):
        for codigo in ("", "   ", None, 123):
            with self.subTest(codigo=codigo):
                with self.assertRaises(ValueError):
                    Factura(codigo, ReservaDePrueba())

    def test_rechaza_reserva_sin_calcular_total(self):
        with self.assertRaises(TypeError):
            Factura("F001", object())

    def test_rechaza_importes_invalidos(self):
        for importe in (-1, "abc", "NaN", "Infinity"):
            with self.subTest(importe=importe):
                reserva = Mock()
                reserva.calcular_total.return_value = importe
                with self.assertRaises(ValueError):
                    Factura("F001", reserva)

    def test_rechaza_tasas_invalidas(self):
        for tasa in (-1, 19, "abc", "NaN", "Infinity"):
            with self.subTest(tasa=tasa):
                with self.assertRaises(ValueError):
                    Factura("F001", ReservaDePrueba(), tasa_impuesto=tasa)

    def test_permite_factura_sin_impuesto(self):
        factura = Factura("F001", ReservaDePrueba(), tasa_impuesto=0)
        self.assertEqual(factura.impuesto, Decimal("0.00"))
        self.assertEqual(factura.total, Decimal("250.50"))

    def test_recalcula_si_cambia_el_total_de_la_reserva(self):
        reserva = Mock()
        reserva.calcular_total.return_value = Decimal("100")
        factura = Factura("F001", reserva)

        reserva.calcular_total.return_value = Decimal("200")
        factura.calcular_totales()

        self.assertEqual(factura.subtotal, Decimal("200.00"))
        self.assertEqual(factura.impuesto, Decimal("38.00"))
        self.assertEqual(factura.total, Decimal("238.00"))

    def test_conserva_importes_si_falla_el_recalculo(self):
        reserva = Mock()
        reserva.calcular_total.return_value = Decimal("100")
        factura = Factura("F001", reserva)
        reserva.calcular_total.return_value = -1

        with self.assertRaises(ValueError):
            factura.calcular_totales()

        self.assertEqual(factura.subtotal, Decimal("100.00"))
        self.assertEqual(factura.impuesto, Decimal("19.00"))
        self.assertEqual(factura.total, Decimal("119.00"))

    def test_aplica_impuesto_y_redondea_a_centavos(self):
        factura = Factura(codigo="F001", reserva=ReservaDePrueba())

        self.assertEqual(factura.codigo, "F001")
        self.assertEqual(factura.subtotal, Decimal("250.50"))
        self.assertEqual(factura.impuesto, Decimal("47.60"))
        self.assertEqual(factura.total, Decimal("298.10"))

    def test_mostrar_factura_aplica_la_tasa_del_modelo(self):
        salida = StringIO()

        with redirect_stdout(salida):
            mostrar_factura("F001", ReservaDePrueba())

        self.assertIn("Factura F001", salida.getvalue())
        self.assertIn("Impuesto: 47.60", salida.getvalue())
        self.assertIn("Total: 298.10", salida.getvalue())
