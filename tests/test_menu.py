"""Pruebas del programa por consola desde main.py."""

import os
from pathlib import Path
import subprocess
import sys
import unittest


class TestMenu(unittest.TestCase):
    def test_registra_cliente_y_lo_encuentra_despues_de_un_error(self):
        salida = self.ejecutar_programa(
            "3\n2\n999\n1\n123\nAna Torres\nana@example.com\n"
            "2\n123\n0\n0\n"
        )
        self.assertIn("No se encontró un cliente", salida)
        self.assertIn("Cliente registrado correctamente", salida)
        self.assertEqual(salida.count("Nombre: Ana Torres"), 2)
        self.assertIn("Hasta pronto", salida)

    def test_error_de_habitacion_regresa_al_menu_y_permite_consultar(self):
        salida = self.ejecutar_programa("4\n2\n999\n4\n2\n101\n0\n0\n")
        self.assertIn("No se encontró una habitación", salida)
        self.assertIn("Habitación 101", salida)
        self.assertIn("Hasta pronto", salida)

    def ejecutar_programa(self, entradas):
        """Abre el programa con respuestas simuladas del usuario."""
        resultado = subprocess.run(
            [sys.executable, "main.py"],
            cwd=Path(__file__).resolve().parents[1],
            input=entradas,
            capture_output=True,
            text=True,
            encoding="utf-8",
            env=os.environ | {"PYTHONIOENCODING": "utf-8"},
            timeout=10,
        )
        self.assertEqual(resultado.returncode, 0, resultado.stderr)
        return resultado.stdout

    def test_cotiza_los_tres_tipos_y_permite_salir(self):
        salida = self.ejecutar_programa("1\n2\n0\n")

        # Los importes incluyen los recargos propios de cada tipo de habitación
        for importe in ("200,000.00", "560,000.00", "340,000.00"):
            self.assertIn(importe, salida)
        self.assertIn("Hasta pronto", salida)

    def test_rechaza_opciones_y_noches_invalidas_y_continua(self):
        salida = self.ejecutar_programa("9\n1\ntexto\n0\n-1\n2\n0\n")

        self.assertIn("Opción inválida", salida)
        self.assertEqual(salida.count("Escribe un número entero"), 3)
        self.assertIn("200,000.00", salida)
        self.assertIn("Hasta pronto", salida)

    def test_comprueba_clase_abstracta(self):
        salida = self.ejecutar_programa("2\n1\n0\n0\n")
        self.assertIn("porque es abstracta", salida)
        self.assertIn("Hasta pronto", salida)

    def test_fechas_invalidas_permiten_una_nueva_consulta(self):
        salida = self.ejecutar_programa(
            "2\n2\n2026-11-12\n2026-11-10\n"
            "2\ntexto\n2026-11-12\n"
            "2\n2026-11-10\n2026-11-12\n0\n0\n"
        )
        self.assertIn("debe ser posterior", salida)
        self.assertIn("Escribe fechas válidas", salida)
        self.assertIn("La estadía tiene 2 noches", salida)
        self.assertIn("Hasta pronto", salida)
