"""Factura asociada a una reserva del hotel."""


class Factura:
    def __init__(self, numero: str, reserva):
        if not isinstance(numero, str) or not numero.strip():
            raise ValueError("El número de factura debe ser un texto no vacío.")
        if not callable(getattr(reserva, "calcular_total", None)):
            raise TypeError("La reserva debe proporcionar el método calcular_total().")

        self.__numero = numero.strip()
        self.__reserva = reserva

    @property
    def numero(self) -> str:
        return self.__numero

    @property
    def reserva(self):
        return self.__reserva
