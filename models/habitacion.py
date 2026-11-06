from abc import ABC, abstractmethod

class Habitacion(ABC): 
    def __init__(self, numero, piso, precioBase, capacidad):
        self.set_numero(numero)
        self.set_piso(piso)
        self.set_precioBase(precioBase)
        self.set_capacidad(capacidad)
        self.__estado = 'Disponible'
    
    def get_numero(self):
        return self.__numero
    
    def set_numero(self, numero):
        if(numero is not None and isinstance (numero, str) and len (numero.strip()) > 0):
            self.__numero = numero
            
        else:
            raise ValueError("Este campo no puede estar vacío. Escribe el número de la habitación.")
        
    def get_piso(self):
        return self.__piso
    
    def set_piso(self, piso):
        if(piso is not None and isinstance (piso, str) and len (piso.strip()) > 0):
            self.__piso = piso      
            
        else:
            raise ValueError("Este campo no puede estar vacío. Escribe el piso.")
        
    def get_precioBase(self):
        return self.__precioBase
    
    def set_precioBase(self, precioBase):
        if (precioBase is not None and isinstance(precioBase, (int, float)) and precioBase >0):
            self.__precioBase = precioBase
            
        else:
            raise ValueError("El precio base debe ser un número mayor que 0.")
        
    def get_capacidad(self):
        return self.__capacidad
    
    def set_capacidad(self, capacidad):
        if (capacidad is not None  and isinstance(capacidad, int) and capacidad >= 1):
            self.__capacidad = capacidad
            
        else:
            raise ValueError("La capacidad debe ser un número entero de al menos 1.")