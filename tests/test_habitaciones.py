"""Pruebas unitarias para la jerarquía de modelos de Habitacion."""

import unittest
from models.habitacion import Habitacion
from models.habitacion_sencilla import HabitacionSencilla
from models.habitacion_suite import HabitacionSuite
from models.habitacion_familiar import HabitacionFamiliar

class TestHabitacion(unittest.TestCase):
    """Verifica el comportamiento de la clase abstracta y sus validaciones comunes."""

    def test_impide_instanciar_clase_abstracta(self):
        with self.assertRaises(TypeError):
            Habitacion("101", "1", 100000, 2)

    def test_valida_precio_base_negativo(self):
        with self.assertRaises(ValueError):
            HabitacionSencilla("102", "1", -50000, 2, "Doble")

    def test_valida_capacidad_invalida(self):
        with self.assertRaises(ValueError):
            HabitacionSuite("202", "2", 200000, 0, True, "Ciudad")

    def test_cambia_estado_al_ocupar_y_liberar(self):
        habitacion = HabitacionSencilla("101", "1", 100000, 2, "Doble")
        self.assertEqual(habitacion.estado, "Disponible")
        
        habitacion.ocupar()
        self.assertEqual(habitacion.estado, "Ocupada")
        
        habitacion.liberar()
        self.assertEqual(habitacion.estado, "Disponible")


class TestHabitacionSencilla(unittest.TestCase):
    """Pruebas específicas para el modelo de habitación básica."""

    def test_calcula_tarifa_sin_recargos(self):
        habitacion = HabitacionSencilla("101", "1", 100000, 2, "Doble")
        tarifa_total = habitacion.calcular_tarifa(3)
        self.assertEqual(tarifa_total, 300000)

    def test_valida_tipo_cama_vacio(self):
        with self.assertRaises(ValueError):
            HabitacionSencilla("103", "1", 100000, 2, "")


class TestHabitacionSuite(unittest.TestCase):
    """Pruebas específicas para el modelo Suite y sus recargos."""

    def test_calcula_tarifa_con_jacuzzi_y_vista(self):
        habitacion = HabitacionSuite("201", "2", 200000, 2, True, "Mar")
        # Base (200000) + Jacuzzi (50000) + Vista (30000) = 280000 por noche
        tarifa_total = habitacion.calcular_tarifa(2)
        self.assertEqual(tarifa_total, 560000)

    def test_descripcion_incluye_servicios_adicionales(self):
        habitacion = HabitacionSuite("201", "2", 200000, 2, True, "Mar")
        descripcion = habitacion.describir_servicios()
        self.assertIn("jacuzzi", descripcion)
        self.assertIn("Mar", descripcion)


class TestHabitacionFamiliar(unittest.TestCase):
    """Pruebas específicas para el modelo Familiar y camas adicionales."""

    def test_calcula_tarifa_por_camas_extra(self):
        habitacion = HabitacionFamiliar("301", "3", 150000, 4, 2)
        # Base (150000) + (2 camas * 20000) = 190000 por noche
        tarifa_total = habitacion.calcular_tarifa(3)
        self.assertEqual(tarifa_total, 570000)

    def test_valida_camas_extra_negativas(self):
        with self.assertRaises(ValueError):
            HabitacionFamiliar("302", "3", 150000, 4, -1)


if __name__ == '__main__':
    unittest.main()