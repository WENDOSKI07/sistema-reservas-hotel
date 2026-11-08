"""Datos de las personas que hacen reservas en el hotel."""


class Cliente:
    """Guarda los datos de contacto de un cliente del hotel."""

    def __init__(self, documento, nombre, correo):
        # Usamos los setters para que los datos se validen desde el principio
        self.documento = documento
        self.nombre = nombre
        self.correo = correo

    @property
    def documento(self):
        """Permite consultar el documento del cliente."""
        return self.__documento

    @documento.setter
    def documento(self, valor):
        # El documento identifica al cliente, por eso no puede quedar vacío
        if not isinstance(valor, str) or valor.strip() == "":
            raise ValueError("El documento del cliente no puede estar vacío")
        self.__documento = valor.strip()

    @property
    def nombre(self):
        """Permite consultar el nombre del cliente."""
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or valor.strip() == "":
            raise ValueError("El nombre del cliente no puede estar vacío")
        self.__nombre = valor.strip()

    @property
    def correo(self):
        """Permite consultar el correo del cliente."""
        return self.__correo

    @correo.setter
    def correo(self, valor):
        if not isinstance(valor, str) or valor.strip() == "":
            raise ValueError("El correo del cliente no puede estar vacío")
        # Un correo siempre tiene arroba, así detectamos errores de digitación
        if "@" not in valor:
            raise ValueError("El correo del cliente debe contener @")
        self.__correo = valor.strip()

    def mostrar_informacion(self):
        """Devuelve los datos del cliente en un solo texto."""
        return (
            f"Cliente: {self.__nombre} - Documento: {self.__documento} "
            f"- Correo: {self.__correo}"
        )