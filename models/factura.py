"""Factura asociada a una reserva del hotel."""

from decimal import Decimal, InvalidOperation, ROUND_HALF_UP


class Factura:
    def __init__(self, numero: str, reserva, *, tasa_impuesto=0):
        if not isinstance(numero, str) or not numero.strip():
            raise ValueError("El número de factura debe ser un texto no vacío.")
        if not callable(getattr(reserva, "calcular_total", None)):
            raise TypeError("La reserva debe proporcionar el método calcular_total().")

        self.__numero = numero.strip()
        self.__reserva = reserva
        self.__tasa_impuesto = self._decimal_no_negativo(tasa_impuesto, "La tasa de impuesto")
        if self.__tasa_impuesto > 1:
            raise ValueError("La tasa de impuesto debe estar entre 0 y 1.")
        self.calcular_totales()

    @property
    def numero(self) -> str:
        return self.__numero

    @property
    def reserva(self):
        return self.__reserva

    @property
    def subtotal(self) -> Decimal:
        return self.__subtotal

    @property
    def impuesto(self) -> Decimal:
        return self.__impuesto

    @property
    def total(self) -> Decimal:
        return self.__total

    def calcular_totales(self) -> None:
        """Toma el importe de la reserva antes del impuesto."""
        importe = self._decimal_no_negativo(self.reserva.calcular_total(), "El subtotal")
        centavo = Decimal("0.01")
        subtotal = importe.quantize(centavo, rounding=ROUND_HALF_UP)
        impuesto = (subtotal * self.__tasa_impuesto).quantize(centavo, rounding=ROUND_HALF_UP)

        self.__subtotal = subtotal
        self.__impuesto = impuesto
        self.__total = subtotal + impuesto

    def mostrar_detalle(self) -> str:
        """Devuelve el resumen de la factura sin imprimirlo."""
        return (
            f"Factura {self.numero}\n"
            f"Subtotal: {self.subtotal:.2f}\n"
            f"Impuesto: {self.impuesto:.2f}\n"
            f"Total: {self.total:.2f}"
        )

    @staticmethod
    def _decimal_no_negativo(valor, campo: str) -> Decimal:
        try:
            numero = Decimal(str(valor))
        except InvalidOperation as error:
            raise ValueError(f"{campo} debe ser un número válido.") from error
        if not numero.is_finite() or numero < 0:
            raise ValueError(f"{campo} debe ser un número finito no negativo.")
        return numero
