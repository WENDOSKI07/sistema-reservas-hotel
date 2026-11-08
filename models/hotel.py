"""Hotel que reúne las habitaciones, los clientes y las reservas."""

from exceptions.hoteleras import ClienteNoEncontradoError, HabitacionNoEncontradaError
from models.reserva import Reserva


class Hotel:
    """Registra habitaciones y clientes, y crea las reservas."""

    def __init__(self, nombre):
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre del hotel no puede estar vacío")
        self.__nombre = nombre.strip()
        # Las listas empiezan vacías y se llenan con los métodos del hotel
        self.__habitaciones = []
        self.__clientes = []
        self.__reservas = []

    @property
    def nombre(self):
        """Permite consultar el nombre del hotel."""
        return self.__nombre

    @property
    def habitaciones(self):
        """Devuelve una copia de la lista de habitaciones."""
        # Entregamos una copia para que nadie cambie la lista original desde afuera
        return list(self.__habitaciones)

    @property
    def clientes(self):
        """Devuelve una copia de la lista de clientes."""
        return list(self.__clientes)

    @property
    def reservas(self):
        """Devuelve una copia de la lista de reservas."""
        return list(self.__reservas)

    def registrar_habitacion(self, habitacion):
        """Agrega al hotel una habitación ya creada."""
        # No pueden existir dos habitaciones con el mismo número
        for registrada in self.__habitaciones:
            if registrada.numero == habitacion.numero:
                raise ValueError(f"Ya existe una habitación con el número {habitacion.numero}")
        self.__habitaciones.append(habitacion)

    def registrar_cliente(self, cliente):
        """Agrega al hotel un cliente ya creado."""
        # No pueden existir dos clientes con el mismo documento
        for registrado in self.__clientes:
            if registrado.documento == cliente.documento:
                raise ValueError(f"Ya existe un cliente con el documento {cliente.documento}")
        self.__clientes.append(cliente)

    def buscar_habitacion(self, numero):
        """Devuelve la habitación con ese número o lanza un error si no existe."""
        numero_buscado = str(numero).strip()
        for habitacion in self.__habitaciones:
            if habitacion.numero == numero_buscado:
                return habitacion
        # Si el for termina sin encontrarla, avisamos con nuestra excepción
        raise HabitacionNoEncontradaError()

    def buscar_cliente(self, documento):
        """Devuelve el cliente con ese documento o lanza un error si no existe."""
        documento_buscado = str(documento).strip()
        for cliente in self.__clientes:
            if cliente.documento == documento_buscado:
                return cliente
        raise ClienteNoEncontradoError()

    def crear_reserva(self, codigo, cliente, habitacion, f_entrada, f_salida, huespedes):
        """Crea la reserva, la confirma, la guarda y la devuelve."""
        # Solo se reserva con clientes y habitaciones registrados en este hotel
        self.buscar_cliente(cliente.documento)
        self.buscar_habitacion(habitacion.numero)

        # Reserva construye su Estadia y valida las fechas y la capacidad
        reserva = Reserva(codigo, cliente, habitacion, f_entrada, f_salida, huespedes)
        reserva.confirmar()

        # Si algo falló arriba, el error sale antes y la reserva no se guarda
        self.__reservas.append(reserva)
        return reserva