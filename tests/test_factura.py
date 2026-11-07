"""Pruebas de los importes y la salida de la factura."""

from contextlib import redirect_stdout
from decimal import Decimal
from io import StringIO
import unittest

from main import mostrar_factura
from models.factura import Factura


class ReservaDePrueba:
    """Representa una reserva con un importe conocido."""

    def calcular_total(self):
        return Decimal("250.50")


class TestFactura(unittest.TestCase):
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
