from models.habitacion import Habitacion
from models.estadia import Estadia


class Reserva:
    def __init__(self, codigo, cliente, habitacion,fecha_entrada, fecha_salida, cantidad_huespedes:int):
        self.set_codigo(codigo)
        self.set_cliente(cliente)
        self.set_habitacion(habitacion)
        self.set_cantidad_huespedes(cantidad_huespedes)
        self.estado = "pendiente"  # Estado inicial de la reserva
        self.estadia = Estadia(fecha_entrada, fecha_salida)

    def set_codigo(self, codigo):
        if not isinstance(codigo, str) or not codigo.strip():
            raise ValueError("El código de reserva no debe estar vacío.")
        self.codigo = codigo.strip()

    def get_codigo(self):
        return self.codigo

    #Validar el cliente
    def set_cliente(self, cliente):
        if not hasattr(cliente, 'nombre') or not hasattr(cliente, 'apellido'):
            raise ValueError("El cliente debe tener nombre y apellido.")
        self.cliente = cliente

    def get_cliente(self):
        return self.cliente

    #Validar la habitación
    def set_habitacion(self, habitacion):
        if not isinstance(habitacion, Habitacion):
            raise ValueError("La habitación debe ser una instancia de la clase Habitacion.")
        self.habitacion = habitacion

    def get_habitacion(self):
        return self.habitacion

    #Validar la cantidad de huéspedes
    def set_cantidad_huespedes(self, cantidad_huespedes):
        if not isinstance(cantidad_huespedes, int) or isinstance(cantidad_huespedes, bool) or cantidad_huespedes <= 0:
            raise ValueError("La cantidad de huéspedes debe ser un número entero positivo.")
        
        if cantidad_huespedes > self.habitacion.capacidad:
            raise ValueError(f"La cantidad de huéspedes no puede superar la capacidad de la habitación ({self.habitacion.capacidad}).")
        self.cantidad_huespedes = cantidad_huespedes

    def get_cantidad_huespedes (self):
        return self.cantidad_huespedes

    def get_estado(self):
        return self.estado

    def confirmar(self):
        if self.estado == "pendiente":
            self.estado = "confirmada"
        else:
            raise ValueError("La reserva ya ha sido confirmada o cancelada, no se puede confirmar nuevamente.")

    def cancelar (self):
        if self.estado == "confirmada":
            self.estado = "cancelada"
        else:
            raise ValueError("Solo se pueden cancelar reservas confirmadas.")
        
    def calcular_total(self):
       noches = self.estadia.calcular_noches()
       return self.habitacion.calcular_tarifa(noches)

    def mostrar_informacion(self):
        info = f"Código de reserva: {self.codigo}\n"
        info += f"Cliente: {self.cliente.nombre} {self.cliente.apellido}\n"
        info += f"Habitación: {self.habitacion.numero} - Tipo: {self.habitacion.tipo}\n"
        info += f"Fecha de Entrada: {self.estadia.fecha_entrada}\n"
        info += f"Fecha de Salida: {self.estadia.fecha_salida}\n"
        info += f"Estadia: {self.estadia.calcular_noches()}\n"
        info += f"Huéspedes: {self.cantidad_huespedes}\n"
        info += f"Estado de la Reserva: {self.estado}\n"
        info += f"Total a Pagar: ${self.calcular_total():.2f}\n"
        return info