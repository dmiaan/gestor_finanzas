# Interfaz de línea de comandos(CLI) 

# Haciendo una importación de las funciones del archivo database 
from database import agregar_transaccion, calcular_balance, obtener_transacciones

# Importando el modulo datetime para colocar fechas
from datetime import date

import csv # Con este modulo leemos, modificamos y recorremos las filas de datos de texto plano

# Creando el menu de la interfaz
menu = {
    1: "Registrar usuario",
    2: "Registrar gasto",
    3: "Ver balance Actual y Historial",
    4: "Filtrar por cuentas",
    5: "Exportar Reporte a CSV",
    6: "Salir"
} 

# Mostrando el menu y solicitar opciones al usuario
while True:
    for opcion, nombre_opcion in menu.items(): # Recorriendo los elementos del diccionario
        print(f"{opcion}: {nombre_opcion}")
    # Creamos un try and except para que el programa no se deje de ejecutar si el usuario introduce un caracter en vez de números    
    try:
        elige_opcion = int(input("Elige una opcion:")) # Pidiendole al usuario que seleccione una opción
    except ValueError:
        print("Entrada invalida, debes ingresar solamente números")
        continue
    
    # Aplicando condicionales que funcionan como un enrutador de opciones con "database.py"
    if elige_opcion == 1:
        try:
            tipo_finanza = input("¿Qué tipo de finanza es? ")
            monto = float(input("¿Cuál es el monto? "))
            categoria = input("¿Cuál es la categoría? ")
            fecha = input("Indiqueme la fecha en este formato: YYYY-MM-DD ")
            descripcion = input("¿Cuál es la descripción? ")
            agregar_transaccion(tipo_finanza, monto, categoria, fecha, descripcion)
            print("La transacción se guardo con exito")
        except ValueError:
            print("Entrada invalida, debes ingresar solamente números")
            continue
            
    elif elige_opcion == 2:
        try:
            gasto = float(input("¿Cuánto es el gasto ?"))
            categoria = input("¿Cuál es la categoría? ")
            fecha = input("Indiqueme la fecha en este formato: YYYY-MM-DD ")
            descripcion = input("¿Cuál es la descripción? ")
            agregar_transaccion("Gasto", gasto, categoria, fecha, descripcion)
            print("El gasto se ha guardado con exito ")
        except ValueError:
            print("Entrada invalida, debes ingresar solamente números")
            continue   
    elif elige_opcion == 3:
        ingreso, gasto, saldo_neto = calcular_balance()
        print(f"Total ingresos: {ingreso:.2f}")
        print(f"Total gastos: {gasto:.2f}")
        print(f"Saldo neto: {saldo_neto:.2f}")
    elif elige_opcion == 4:
        categoria_buscada = input("¿Qué categoría de cuenta deseas filtrar? ") 
        lista_filtrada = obtener_transacciones(categoria_buscada)
        if len(lista_filtrada) == 0:
            print("No hay transacciones para mostrar en esta cuenta")
        else:
            for id_transaccion, tipo, monto, categoria, fecha, descripcion in lista_filtrada:
                print(f"Identificador: {id_transaccion}\nTipo de transacción {tipo}\nCantidad de dinero disponible: {monto}\nCategoría a la que pertenece: {categoria}\nLa fecha cuándo ocurrió: {fecha}\nDescripción colocada: {descripcion}") 
    elif elige_opcion == 5:
        informacion_recolectada = obtener_transacciones()
        if len(informacion_recolectada) == 0:
            print("No hay datos para exportar.")
        else:
            reporte = input("¿Con qué nombre deseas guardar este reporte? ")
            reporte_fi = f"{reporte}.csv" # Creando el archivo csv para el reporte
            with open(reporte_fi, "w", newline="") as reporte_finanzas: # Utilizamos el with open para manipular el archivo
               escritor = csv.writer(reporte_finanzas)
               escritor.writerow(["identificador", "tipo", "monto", "categoria", "fecha", "descripcion"])
               escritor.writerows(informacion_recolectada)
        print("Reporte creado con exito.")   
    elif elige_opcion == 6:
        print("¡Gracias por usar el sistema! Cerrando aplicación...") 
        break
    else:
        print("La opción seleccionada no es valida")
                       
            
        
        
        
         
        
            
    
        
    
    