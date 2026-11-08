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

El menú permite cotizar las tres habitaciones de ejemplo indicando las noches.
El importe de la cotización corresponde al alojamiento antes de impuestos.
En Comprobaciones de la actividad se puede intentar crear la clase abstracta
Habitacion y validar las fechas de una estadía.

Para comprobar el manejo de errores, ingresar una salida igual o anterior a la
entrada. El sistema muestra el mensaje de FechasInvalidasError y permite hacer
otra consulta. Las fechas se ingresan en formato AAAA-MM-DD.

Los datos se conservan en memoria durante la ejecución.

El área Clientes permite registrar personas y buscarlas por documento. Consultar
habitaciones permite listar, buscar por número y comparar tarifas. Los clientes
registrados se conservan al volver al menú principal. Si una habitación no existe,
el mensaje se muestra y se regresa al menú principal.

## Organización

| Ubicación | Contenido |
| --- | --- |
| `main.py` | Punto de entrada e integración de los casos de demostración |
| `models/` | Entidades y reglas del dominio hotelero |
| `exceptions/` | Excepciones propias del sistema de reservas |
| `controllers/` | Navegación y coordinación de las operaciones |
| `views/` | Interacción por consola |
| `tests/` | Pruebas unitarias y de integración |
| `docs/` | Ubicación prevista para UML y Documento de Decisiones de Diseño |

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

## Pruebas

```bash
python -m unittest discover -v
```

Las pruebas cubren habitaciones, estadía, excepciones, facturación y navegación
desde main.py. Las pruebas de integración de reservas se omiten temporalmente
cuando faltan Cliente, Hotel o Reserva. Un resultado omitido no acredita que ese
flujo funcione.

## Integración pendiente

En la rama Oscar están integrados los aportes de Stefanny, Stefania y Silvana.
Clientes y habitaciones ya se pueden utilizar desde el menú principal.
Reserva, de Lizeth, requiere correcciones antes de su integración.
Hotel carga esa clase al crear una reserva, por lo que sus registros y búsquedas
pueden usarse mientras se completa esa integración. Una prueba de Hotel y las
cinco pruebas de integración permanecen omitidas hasta disponer de Reserva.

Queda conectar reservas y facturas al menú, completar la
demostración de ocho objetos y de los errores del dominio, y añadir el UML y el
Documento de Decisiones de Diseño a docs/.

## Uso de inteligencia artificial

Se utilizó IA como apoyo para generar y revisar fragmentos de código, explicar
conceptos y preparar pruebas unitarias y de integración. El Documento de
Decisiones de Diseño deberá detallar las herramientas usadas, los aportes,
las correcciones realizadas y la verificación del equipo.

## Trabajo en equipo

Traer la base de `main` antes de empezar y trabajar en una rama propia. Integrar cada aporte mediante un pull request.
