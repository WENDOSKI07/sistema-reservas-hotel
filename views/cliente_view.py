"""Entradas y mensajes del área de clientes."""


class ClienteView:
    """Pide los datos y muestra la información de los clientes."""

    def mostrar_menu(self):
        print("\nClientes")
        print("1. Registrar cliente")
        print("2. Buscar cliente por documento")
        print("0. Volver al menú principal")
        return input("Selecciona una opción: ").strip()

    def pedir_datos_cliente(self):
        """Devuelve los datos que necesita el modelo Cliente."""
        documento = input("Documento: ").strip()
        nombre = input("Nombre: ").strip()
        correo = input("Correo: ").strip()
        # La vista recoge el texto, las validaciones las hace el modelo
        return documento, nombre, correo

    def pedir_documento(self):
        """Pide el documento del cliente que se quiere consultar."""
        return input("Documento del cliente: ").strip()

    def mostrar_cliente(self, cliente):
        """Consulta las propiedades del cliente para mostrar sus datos."""
        print(f"Documento: {cliente.documento}")
        print(f"Nombre: {cliente.nombre}")
        print(f"Correo: {cliente.correo}")

    def mostrar_mensaje(self, mensaje):
        print(mensaje)
