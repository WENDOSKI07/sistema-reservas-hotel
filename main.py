"""Punto de entrada del sistema de reservas del hotel."""

from models.factura import Factura
from controllers.menu_controller import MenuController
from models.habitacion_sencilla import HabitacionSencilla
from models.habitacion_suite import HabitacionSuite
from models.habitacion_familiar import HabitacionFamiliar
from views.menu_view import MenuView


def mostrar_habitaciones(habitaciones, noches: int) -> None:
    """Muestra los servicios y el costo de cada habitación para la estadía."""
    for habitacion in habitaciones:
        # Acá usamos polimorfismo, cada habitación responde con su propia tarifa y servicios
        print(habitacion.mostrar_informacion())
        print(habitacion.describir_servicios())
        print(f"Total por {noches} noches: {habitacion.calcular_tarifa(noches):,.2f}")
        print()


def mostrar_factura(codigo: str, reserva, *, tasa_impuesto=Factura.TASA_IMPUESTO) -> None:
    """Genera una factura a partir de una reserva y muestra su detalle."""
    factura = Factura(codigo, reserva, tasa_impuesto=tasa_impuesto)
    factura.mostrar_factura()


def main():
    # Estas habitaciones de ejemplo permiten probar la cotización desde el menú
    habitaciones = [
        HabitacionSencilla("101", "1", 100000, 2, "doble"),
        HabitacionSuite("201", "2", 200000, 2, True, "la ciudad"),
        HabitacionFamiliar("301", "3", 150000, 4, 1),
    ]
    menu = MenuController(MenuView(), habitaciones, mostrar_habitaciones)
    menu.iniciar()


if __name__ == "__main__":
    main()
