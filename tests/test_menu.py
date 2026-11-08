"""Pruebas del programa por consola desde main.py."""

import os
from pathlib import Path
import subprocess
import sys
import unittest


class TestMenu(unittest.TestCase):
    def test_datos_iniciales_incluyen_ocho_objetos_del_dominio(self):
        from main import crear_hotel
        hotel = crear_hotel()
        self.assertEqual(1 + len(hotel.habitaciones) + len(hotel.clientes), 8)
        self.assertEqual(hotel.reservas, [])

    def test_registrar_reservar_facturar_cancelar_y_reservar_de_nuevo(self):
        salida = self.ejecutar_programa(
            "3\n1\n321\nAna Nueva\nana@example.com\n0\n"
            "5\n1\nR001\n321\n101\n2026-11-10\n2026-11-12\n2\n"
            "3\nR001\n3\nR001\n4\nR001\n"
            "1\nR002\n321\n101\n2026-11-10\n2026-11-12\n2\n"
            "2\n0\n0\n"
        )
        self.assertIn("Cliente registrado correctamente", salida)
        self.assertEqual(salida.count("Reserva confirmada correctamente"), 2)
        self.assertEqual(salida.count("Factura F-R001"), 2)
        self.assertIn("Total: 238000.00", salida)
        self.assertIn("Reserva cancelada", salida)
        self.assertIn("Estado: cancelada", salida)
        self.assertIn("Estado: confirmada", salida)
        self.assertIn("Hasta pronto", salida)

    def test_errores_de_reserva_permiten_continuar(self):
        salida = self.ejecutar_programa(
            "5\n1\nR001\n999\n101\n2026-11-10\n2026-11-12\n2\n"
            "1\nR001\n123\n999\n2026-11-10\n2026-11-12\n2\n"
            "1\nR001\n123\n101\n2026-11-12\n2026-11-10\n2\n"
            "1\nR001\n123\n101\n2026-11-10\n2026-11-12\n3\n"
            "1\nR001\n123\n101\n2026-11-10\n2026-11-12\n2\n"
            "1\nR002\n123\n101\n2026-11-10\n2026-11-12\n2\n"
            "4\nR001\n3\nR001\n0\n0\n"
        )
        for mensaje in (
            "No se encontró un cliente", "No se encontró una habitación",
            "debe ser posterior", "supera la capacidad", "no está disponible",
            "Solo se puede facturar una reserva confirmada", "Hasta pronto",
        ):
            self.assertIn(mensaje, salida)
    def test_registra_cliente_y_lo_encuentra_despues_de_un_error(self):
        salida = self.ejecutar_programa(
            "3\n2\n999\n1\n321\nAna Torres\nana@example.com\n"
            "2\n321\n0\n0\n"
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
