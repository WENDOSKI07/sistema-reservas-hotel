from abc import ABC, abstractmethod

class Habitacion(ABC): 
    def __init__(self, numero, piso, precioBase, capacidad):
        self.set_numero(numero)
        self.set_piso(piso)
        self.set_precioBase(precioBase)
        self.set_capacidad(capacidad)
        self.__estado = 'Disponible'