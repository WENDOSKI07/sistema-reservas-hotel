"""Errores propios del sistema de reservas del hotel."""


class HotelError(Exception):
    """Agrupa los errores del hotel para capturarlos desde el menú."""


# Las clases del modelo lanzan estos errores cuando detectan el problema
# El menú los captura para mostrar el mensaje y permitir que el usuario continúe
class FechasInvalidasError(HotelError):
    """Se usa cuando la salida no es posterior a la entrada."""

    def __init__(self):
        super().__init__("La fecha de salida debe ser posterior a la fecha de entrada")


class CapacidadExcedidaError(HotelError):
    """Se usa cuando la cantidad de huéspedes supera la capacidad."""

    def __init__(self):
        super().__init__("La cantidad de huéspedes supera la capacidad de la habitación")


class HabitacionNoDisponibleError(HotelError):
    """Se usa cuando se intenta reservar una habitación ocupada."""

    def __init__(self):
        super().__init__("La habitación no está disponible para reservar")


class HabitacionNoEncontradaError(HotelError):
    """Se usa cuando el número buscado no pertenece a ninguna habitación."""

    def __init__(self):
        super().__init__("No se encontró una habitación con el número indicado")


class ClienteNoEncontradoError(HotelError):
    """Se usa cuando el documento buscado no está registrado."""

    def __init__(self):
        super().__init__("No se encontró un cliente con el documento indicado")
