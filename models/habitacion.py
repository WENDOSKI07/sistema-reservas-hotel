from abc import ABC, abstractmethod

class Habitacion(ABC): 
    def __init__(self, numero, piso, precio_base, capacidad):
        self.numero = numero
        self.piso = piso
        self.precio_base = precio_base
        self.capacidad = capacidad
        self.__estado = 'Disponible'
        
    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, valor):
        if(valor is not None and isinstance (valor, str) and len (valor.strip()) > 0):
            self.__numero = valor
            
        else:
            raise ValueError("Este campo no puede estar vacío. Escribe el número de la habitación.")
    
    @property    
    def piso(self):
        return self.__piso
    
    @piso.setter
    def piso(self, valor):
        if(valor is not None and isinstance (valor, str) and len (valor.strip()) > 0):
            self.__piso = valor     
            
        else:
            raise ValueError("Este campo no puede estar vacío. Escribe el piso.")
     
    @property   
    def precio_base(self):
        return self.__precio_base
    
    @precio_base.setter
    def precio_base(self, valor):
        if (valor is not None and isinstance(valor, (int, float)) and valor >0):
            self.__precioBase = valor
            
        else:
            raise ValueError("El precio base debe ser un número mayor que 0.")
    
    @property    
    def capacidad(self):
        return self.__capacidad
    
    @capacidad.setter
    def set_capacidad(self, valor):
        if (valor is not None  and isinstance(valor, int) and valor >= 1):
            self.__capacidad = valor
            
        else:
            raise ValueError("La capacidad debe ser un número entero de al menos 1.")
    
    @property    
    def estado(self):
        return self.__estado
    
    # Métodos de comportamiento común
    def ocupar(self):
        self.__estado = 'Ocupada'   
        
    def liberar(self):
        self.__estado = 'Disponible'
        
    def mostrar_informacion(self):
        return f"Habitación {self.numero()} (Piso {self.piso()}) - Precio Base: {self.precio_base()} - Capacidad: {self.capacidad()} - Estado: {self.estado()}"

    @abstractmethod
    def calcular_tarifa(self, noches):
        # Este método debe ser redefinido por las clases hijas.
        pass

    @abstractmethod
    def describir_servicios(self):
        # Este método debe ser redefinido por las clases hijas.
        pass