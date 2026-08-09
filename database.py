# Conexión y consultas a la base de datos(CRUD)

# Paso1: Configurar la base de datos

# Crear funciones dedicadas exclusivamente para poder interactuar con la base de datos

import mysql.connector # importando el modulo para poder conectar la base de datos

# Definiendo la función que va a hacer la conexión con la base de datos y creación de la table de la base de datos
def inicializar_db():
    conexion_data_base = {
        "host": "127.0.0.1",
        "user": "root",
        "password": "",
        "database": "gestor_finanzas"     
    }
    conexion = mysql.connector.connect(**conexion_data_base)  # Abrir la conexión
    mensajero_sql = conexion.cursor() # Enviar ordenes a la base de datos
    consulta_sql = """CREATE TABLE IF NOT EXISTS transacciones(
        id_transaccion INT AUTO_INCREMENT PRIMARY KEY,
        tipo VARCHAR(25),
        monto DECIMAL(10,2),
        categoria VARCHAR(30),
        fecha DATE,
        descripcion VARCHAR(100))
        """
    mensajero_sql.execute(consulta_sql) # Ejecutar el envio de la creación de la tabla
    mensajero_sql.close() # Cierre de la ejecución de la tabla
    conexion.close() # Cierre de la conexión con la base de datos
    
    
# ________________________________________________________________________________________________

# Función para conectar la base de datos y no estar repitiendo codigo de conexión en cada función
def conectar():
    conexion_data_base = {
        "host": "127.0.0.1",
        "user": "root",
        "password": "",
        "database": "gestor_finanzas"
        }
    conexion = mysql.connector.connect(**conexion_data_base)  # Abrir la conexión
    return conexion

# _______________________________________________________________________________________________________

# Función para agregar datos a la tabla
def agregar_transaccion(tipo, monto, categoria, fecha, descripcion):
      conexion = conectar()
      mensajero_sql = conexion.cursor() # Enviar ordenes a la base de datos
      consulta_sql = """INSERT INTO transacciones(tipo, monto, categoria, fecha, descripcion)
      VALUES(%s, %s, %s, %s, %s)
      """
      valores = (tipo, monto, categoria, fecha, descripcion)
      mensajero_sql.execute(consulta_sql, valores)
      conexion.commit() # Guardamos los cambios de forma permanente
      mensajero_sql.close() # Cierre del mensajero
      conexion.close() # Cierre de la conexión con la base de datos
    

#___________________________________________________________________________________________________        

# Filtrando datos
def obtener_transacciones(filtro_categoria=None):
    conexion = conectar()
    mensajero_sql = conexion.cursor()
    if filtro_categoria is None:
        consulta_sql = """SELECT *
                          FROM transacciones""" 
        mensajero_sql.execute(consulta_sql)                 
    else: 
        consulta_sql = """SELECT *
                              FROM transacciones
                              WHERE categoria = %s"""
        valor_filtro = (filtro_categoria,)
        mensajero_sql.execute(consulta_sql, valor_filtro)  
                        
    registros = mensajero_sql.fetchall() # Obteniendo las filas de la consulta SQL ejecutada previamente
    mensajero_sql.close()
    conexion.close()  
    return registros     

    
# ________________________________________________________________________________________________

# Calcular el balance: Ingresos, gastos y retornar saldo neto

def calcular_balance():
    total_ingreso = 0 # Variable auxiliar para el total_ingresos
    total_gasto = 0 # Variable auxiliar para el total_gastos
    lista_transacciones = obtener_transacciones()
    for id_transaccion, tipo, monto, categoria, fecha, descripcion in lista_transacciones: # Desempaquetando datos(again)
        if tipo == "Ingreso":
            total_ingreso += monto # calculando el ingreso
        elif tipo == "Gasto":
            total_gasto += monto # calculando el gasto y lo colocamos con el signo "+" para que a la hora de obtener el saldo neto no afecte con la regla de los signos
    saldo_neto = total_ingreso - total_gasto 
    return total_ingreso, total_gasto, saldo_neto  
 

# __________________________________________________________________________________________________________

# Eliminación de transacción   
def eliminar_transaccion(id_transaccion):
    conexion = conectar()
    mensajero_sql = conexion.cursor()
    consulta_sql = """DELETE FROM transacciones  
                      WHERE id_transaccion = %s""" # Consulta para eliminar datos
    parametro_seguridad = (id_transaccion,) 
    mensajero_sql.execute(consulta_sql, parametro_seguridad)
    conexion.commit() 
    mensajero_sql.close()
    conexion.close()
                      

# Este bloque protege las ejecuciones. Solamente van a correr si ejecutamos este archivo directamente.                   
if __name__ == "__main__":
    inicializar_db()
    print("Base de datos e interfaz inicializadas correctamente.")                    