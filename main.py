"""Punto de entrada del sistema de reservas del hotel."""

from models.factura import Factura


def mostrar_factura(numero: str, reserva, *, tasa_impuesto=0) -> None:
    """Genera una factura a partir de una reserva y muestra su detalle."""
    factura = Factura(numero, reserva, tasa_impuesto=tasa_impuesto)
    print(factura.mostrar_detalle())


def main():
    print("Sistema de reservas del hotel")


if __name__ == "__main__":
    main()
