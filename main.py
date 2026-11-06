"""Punto de entrada del sistema de reservas del hotel."""

from models.factura import Factura


def mostrar_habitaciones(habitaciones, noches: int) -> None:
    """Muestra los servicios y el costo de cada habitación para la estadía."""
    for habitacion in habitaciones:
        # Cada tipo de habitación calcula su tarifa y describe sus servicios
        print(habitacion.mostrar_informacion())
        print(habitacion.describir_servicios())
        print(f"Total por {noches} noches: {habitacion.calcular_tarifa(noches):,.2f}")
        print()


def mostrar_factura(numero: str, reserva, *, tasa_impuesto=Factura.TASA_IMPUESTO) -> None:
    """Genera una factura a partir de una reserva y muestra su detalle."""
    factura = Factura(numero, reserva, tasa_impuesto=tasa_impuesto)
    print(factura.mostrar_detalle())


def main():
    print("Sistema de reservas del hotel")


if __name__ == "__main__":
    main()
