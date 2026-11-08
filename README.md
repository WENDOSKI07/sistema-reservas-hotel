# Sistema de reservas de hotel

Proyecto final de Programación I de la Universidad de Manizales. El sistema
administra alojamiento en habitaciones sencillas, suites y familiares y está
organizado con modelos, vistas y controladores.

## Integrantes

- Silvana Arenas Molina
- Kelly Stefania Martinez Martinez
- Oscar Ricaurte Salamanca
- Stefanny Muñoz Gasca
- Lizeth Lopez Blanco

## Ejecución

Se utiliza Python 3.10 o superior y únicamente módulos de la biblioteca estándar.
Desde la carpeta del proyecto ejecutar:

```bash
python main.py
```

El programa inicia con ocho objetos del dominio, un hotel, cuatro habitaciones
y tres clientes. Cada reserva adicional crea también su propio objeto Estadia.

| Área | Operaciones |
| --- | --- |
| Cotizar habitaciones | Comparar servicios y costo antes de impuestos según las noches |
| Comprobaciones de la actividad | Intentar crear Habitacion y validar fechas de estadía |
| Clientes | Registrar y buscar por documento |
| Consultar habitaciones | Listar, consultar detalles y comparar tarifas |
| Reservas y facturas | Crear, consultar, facturar y cancelar reservas |

Para comprobar el manejo de errores, ingresar una salida igual o anterior a la
entrada. El sistema muestra el mensaje de FechasInvalidasError y permite hacer
otra consulta. Las fechas se ingresan en formato AAAA-MM-DD.

Los datos se conservan en memoria durante la ejecución.
Al cerrar el programa se pierden los registros realizados durante la sesión.

El área Clientes permite registrar personas y buscarlas por documento. Consultar
habitaciones permite listar, buscar por número y comparar tarifas. Los clientes
registrados se conservan al volver al menú principal. Si una habitación no existe,
el mensaje se muestra y se regresa al menú principal.

## Recorrido de prueba por consola

1. En Clientes, registrar un documento nuevo, por ejemplo 321, con nombre y correo.
2. En Reservas y facturas, elegir Crear y confirmar reserva. Usar código R001,
   documento 321, habitación 101, entrada 2026-11-10, salida 2026-11-12 y 2 huéspedes.
3. Elegir Emitir o consultar factura e ingresar R001. El subtotal es 200000,
   el impuesto es 38000 y el total es 238000.
4. Elegir Cancelar reserva e ingresar R001. La habitación vuelve a estar disponible.
5. Crear R002 para la habitación 101 y comprobar que se puede reservar otra vez.

También se pueden usar los clientes iniciales con documentos 123, 456 y 789.
Las habitaciones disponibles al inicio son 101, 102, 201 y 301.

Para comprobar los errores del dominio, usar un documento o habitación inexistente,
invertir las fechas, superar la capacidad de la habitación o intentar reservar
una habitación que ya está ocupada. El programa muestra el mensaje y permite
continuar. La cancelación repetida y la factura de una reserva cancelada se rechazan.

La disponibilidad se controla por estado, disponible u ocupada. Una reserva
confirmada ocupa la habitación hasta su cancelación, aunque las fechas ingresadas
no coincidan con las de otra solicitud. Las fechas sirven para validar el período
y calcular las noches. Las facturas son documentos de la demostración, sin cobros
ni procesamiento de pagos. Una factura emitida antes de cancelar se conserva
como historial dentro de la sesión.

## Organización

| Ubicación | Contenido |
| --- | --- |
| `main.py` | Punto de entrada e integración de los casos de demostración |
| `models/` | Entidades y reglas del dominio hotelero |
| `exceptions/` | Excepciones propias del sistema de reservas |
| `controllers/` | Navegación y coordinación de las operaciones |
| `views/` | Interacción por consola |
| `tests/` | Pruebas unitarias y de integración |
| `docs/` | UML y su fuente editable |

## Programación orientada a objetos

Habitacion es una clase abstracta. HabitacionSencilla, HabitacionSuite y
HabitacionFamiliar heredan sus datos comunes y sobrescriben calcular_tarifa(),
describir_servicios() y mostrar_informacion().

En main.py una colección reúne los tres tipos de habitación. La función
mostrar_habitaciones() los recorre con un solo ciclo y llama a los mismos métodos
para mostrar sus servicios e importes. Cada objeto responde según su propia clase.

Estadia valida las fechas y calcula las noches. Factura recibe una reserva,
consulta calcular_total() y obtiene subtotal, impuesto y total usando Decimal.
La tasa predeterminada del proyecto es del 19 %.

Reserva crea su Estadia internamente y asocia Cliente y Habitacion.
Hotel registra los objetos, comprueba su existencia y confirma la reserva antes
de guardarla. Las excepciones personalizadas heredan de HotelError y se capturan
en los controladores de consola que ejecuta el programa principal.

## Pruebas

```bash
python -m unittest discover -v
```

La ejecución verificada contiene 77 pruebas, todas aprobadas y sin omisiones.
Cubren clientes, habitaciones, estadía, excepciones, hotel, reservas y facturación.
Las pruebas de consola ejecutan main.py con entradas simuladas, incluido el
recorrido completo de registro, reserva, facturación, cancelación y nueva reserva.

## Documentación

- [Diagrama UML en PDF](docs/UML%20de%20clases.pdf)
- [Fuente editable del UML en Mermaid](docs/uml_clases.mmd)

El Documento de Decisiones de Diseño está en revisión local, pendiente de
incorporarse al repositorio.

## Uso de inteligencia artificial

Se utilizó ChatGPT de OpenAI para explicar conceptos, generar código y pruebas,
revisar la integración y preparar documentación. Silvana declaró el uso de Claude
de Anthropic para comprender el UML y revisar su sección. El Documento de
Decisiones en revisión describe ese apoyo, los cambios y la verificación realizada.

## Trabajo en equipo

Traer la base de `main` antes de empezar y trabajar en una rama propia. Integrar cada aporte mediante un pull request.
