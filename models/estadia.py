"""Fechas y duración del alojamiento de una reserva."""

from datetime import date

from exceptions.hoteleras import FechasInvalidasError


class Estadia:
    """Guarda las fechas de entrada y salida y calcula las noches."""

    def __init__(self, fecha_entrada, fecha_salida):
        # Recibimos fechas ya convertidas, la vista se encarga de pedir el texto
        if type(fecha_entrada) is not date or type(fecha_salida) is not date:
            raise TypeError("La entrada y la salida deben ser fechas de tipo date")

        if fecha_salida <= fecha_entrada:
            raise FechasInvalidasError()

        # Guardamos las fechas después de comprobar que el período sea válido
        self.__fecha_entrada = fecha_entrada
        self.__fecha_salida = fecha_salida

    @property
    def fecha_entrada(self):
        """Permite consultar la fecha de entrada."""
        return self.__fecha_entrada

    @property
    def fecha_salida(self):
        """Permite consultar la fecha de salida."""
        return self.__fecha_salida

    def calcular_noches(self):
        """Devuelve los días que hay entre la entrada y la salida."""
        # Al restar dos fechas obtenemos una duración, days nos da los días
        return (self.__fecha_salida - self.__fecha_entrada).days
