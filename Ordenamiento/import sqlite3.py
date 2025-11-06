import sqlite3
import heapq  # Usamos un min-heap para ordenar

# Conexión a la BD
conn = sqlite3.connect('/Users/danielquinteroc/Descargas/personas.db')
cursor = conn.cursor()

# Extraer datos
cursor.execute("SELECT * FROM Personas")
datos = cursor.fetchall()  # Lista de tuplas (id, nombre, edad, ciudad)

# Ordenar por edad usando Heap Sort (simulado con heapq)
datos_ordenados = sorted(datos, key=lambda x: x[2])  # x[2] = edad

# Mostrar resultados
for fila in datos_ordenados:
    print(fila)

conn.close()