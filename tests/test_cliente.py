"""Pruebas de la clase Cliente."""

import unittest

from models.cliente import Cliente


class TestCliente(unittest.TestCase):
    """Revisa que el cliente guarde y valide sus datos."""

    def setUp(self):
        # Se ejecuta antes de cada prueba, así cada una empieza con un cliente nuevo
        self.cliente = Cliente("123", "Ana Torres", "ana@correo.com")

    def test_crea_cliente_con_datos_validos(self):
        self.assertEqual(self.cliente.documento, "123")
        self.assertEqual(self.cliente.nombre, "Ana Torres")
        self.assertEqual(self.cliente.correo, "ana@correo.com")

    def test_quita_los_espacios_de_los_datos(self):
        cliente = Cliente(" 456 ", " Luis Gómez ", " luis@correo.com ")
        self.assertEqual(cliente.documento, "456")
        self.assertEqual(cliente.nombre, "Luis Gómez")
        self.assertEqual(cliente.correo, "luis@correo.com")

    def test_documento_vacio_lanza_error(self):
        with self.assertRaises(ValueError):
            Cliente("   ", "Ana Torres", "ana@correo.com")

    def test_nombre_vacio_lanza_error(self):
        with self.assertRaises(ValueError):
            Cliente("123", "", "ana@correo.com")

    def test_correo_vacio_lanza_error(self):
        with self.assertRaises(ValueError):
            Cliente("123", "Ana Torres", "")

    def test_correo_sin_arroba_lanza_error(self):
        with self.assertRaises(ValueError):
            Cliente("123", "Ana Torres", "anacorreo.com")

    def test_setter_cambia_el_correo_si_es_valido(self):
        self.cliente.correo = "nuevo@correo.com"
        self.assertEqual(self.cliente.correo, "nuevo@correo.com")

    def test_setter_rechaza_correo_invalido_y_conserva_el_anterior(self):
        with self.assertRaises(ValueError):
            self.cliente.correo = "sin-arroba"
        # El dato malo no se guardó, el cliente sigue con su correo original
        self.assertEqual(self.cliente.correo, "ana@correo.com")

    def test_mostrar_informacion_devuelve_texto_con_los_datos(self):
        texto = self.cliente.mostrar_informacion()
        self.assertIsInstance(texto, str)
        self.assertIn("Ana Torres", texto)
        self.assertIn("123", texto)
        self.assertIn("ana@correo.com", texto)


if __name__ == "__main__":
    unittest.main()