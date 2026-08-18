🧾Sistema de gestión de finanzas por línea de comandos (CLI) desarrollado en Python y MySQL. Este proyecto permite registrar ingresos y gastos, calcular el saldo neto en tiempo real, filtrar movimientos por categorías y exportar reportes a formato CSV.🧾

✱ Características principales:

● Interfaz Interactiva: Menú en consola con validación de errores numéricos(try/except).

● Registro CRUD: Permite registrar transacciones, consultar el historial, filtrar datos y eliminar registros específicos.

● Calculo de Balance: Suma automáticamente los ingresos, gastos y saldo neto en tiempo real.

● Busca y muestra transacciones específicas asociadas a una categoría o cuenta determinada.

● Exportación de Datos: Generación de reportes automáticos en formato .csv.

● Almacenamiento local seguro utilizando MySQL con consultas parametrizadas para evitar inyecciones SQL.

● Base de datos persistente: Los datos no desaparecen al cerrar el programa. Todo se guarda de forma permanente en una base de datos local con MySQL, utilizando consultas protegidas para cuidar cada registro.


✱ Tecnologías y librerías utilizadas:

● Lenguaje principal: Python 3

● Base de datos: MySQL(gestionado mediante XAMPP)

● Librerías externas:

mysql-connector-python: Conector para enlazar python con la base de datos MySQL.

● Librerías nativas:

csv: Módulo para la manipulación, lectura y escritura de archivos de texto plano en formato CSV.

datetime: Módulo para el manejo y formato de fechas(YYYY-MM-DD)


✱ Estructura del código:

database.py: Dedicado exclusivamente a la lógica de la base de datos, incluyendo la conexión automática, inicialización de tablas y las funciones del CRUD.

main.py: Controla la interfaz de usuario en consola, despliega el menú principal y rutea las opciones seleccionadas.

✱ Instalación 𝐲 configuración:

```bash
   git clone [https://github.com/TU-USUARIO/gestor_finanzas.git](https://github.com/TU-USUARIO/gestor_finanzas.git)
   cd gestor_finanzas
```

1. Configurar la Base de Datos:
Asegúrate de tener el servicio de MySQL activo en tu entorno local (ej. a través de XAMPP).
Crea una base de datos llamada gestor_finanzas. Al ejecutar el programa por primera vez, el sistema creará automáticamente las tablas necesarias.

2. Instalar dependencias:
Es necesario instalar el conector de MySQL para Python:
pip install mysql-connector-python

3. Ejecutar la aplicación:
python main.py

