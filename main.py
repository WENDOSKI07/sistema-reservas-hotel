"""Punto de entrada del sistema de reservas del hotel."""

from models.factura import Factura
from datetime import date
from models.habitacion import Habitacion
from models.estadia import Estadia
from controllers.menu_controller import MenuController
from models.habitacion_sencilla import HabitacionSencilla
from models.habitacion_suite import HabitacionSuite
from models.habitacion_familiar import HabitacionFamiliar
from views.menu_view import MenuView
from models.hotel import Hotel
from controllers.cliente_controller import ClienteController
from controllers.habitacion_controller import HabitacionController
from views.cliente_view import ClienteView
from views.habitacion_view import HabitacionView


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


def comprobar_clase_abstracta():
    """Intenta crear la clase base para mostrar la restricción de Python."""
    try:
        Habitacion("100", "1", 100000, 2)
    except TypeError:
        return (
            "Python rechazó la creación de Habitacion porque es abstracta. "
            "Se debe crear una habitación sencilla, suite o familiar."
        )
    raise RuntimeError("Habitacion debería impedir la creación de instancias")


def validar_estadia(entrada, salida):
    """Convierte el texto y delega la validación de las fechas al modelo."""
    try:
        fecha_entrada = date.fromisoformat(entrada)
        fecha_salida = date.fromisoformat(salida)
    except ValueError as error:
        raise ValueError("Escribe fechas válidas con el formato AAAA-MM-DD") from error
    estadia = Estadia(fecha_entrada, fecha_salida)
    return f"La estadía tiene {estadia.calcular_noches()} noches"


def main():
    # Estas habitaciones de ejemplo permiten probar la cotización desde el menú
    habitaciones = [
        HabitacionSencilla("101", "1", 100000, 2, "doble"),
        HabitacionSuite("201", "2", 200000, 2, True, "la ciudad"),
        HabitacionFamiliar("301", "3", 150000, 4, 1),
    ]
    hotel = Hotel("Hotel Manizales")
    for habitacion in habitaciones:
        hotel.registrar_habitacion(habitacion)

    clientes = ClienteController(hotel, ClienteView())
    consulta_habitaciones = HabitacionController(hotel, HabitacionView())
    menu = MenuController(
        MenuView(), habitaciones, mostrar_habitaciones,
        comprobar_clase_abstracta, validar_estadia, clientes, consulta_habitaciones,
    )
    menu.iniciar()


if __name__ == "__main__":
    main()
