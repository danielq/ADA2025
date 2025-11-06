import sqlite3

def particionar(lista, baja, alta, columna):
    """Función de particionamiento para QuickSort."""
    pivote = lista[alta][columna]  # Elegir el último elemento como pivote
    i = baja - 1

    for j in range(baja, alta):
        if lista[j][columna] <= pivote:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]  # Intercambiar

    lista[i + 1], lista[alta] = lista[alta], lista[i + 1]  # Posición final del pivote
    return i + 1

def quick_sort(lista, baja, alta, columna):
    """QuickSort recursivo."""
    if baja < alta:
        pi = particionar(lista, baja, alta, columna)
        quick_sort(lista, baja, pi - 1, columna)  # Ordenar sublista izquierda
        quick_sort(lista, pi + 1, alta, columna)  # Ordenar sublista derecha

# Conexión a la BD y extracción de datos
conn = sqlite3.connect('/Users/danielquintero/Desktop/proyectos 2025/FADA/RA 2/algoritmos de ordenamiento/algoritmos de ordenamiento/sqlite/personas.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM Personas")
datos = cursor.fetchall()  # Lista de tuplas: (id, nombre, edad, ciudad)

# Ordenar por edad (columna=2)
quick_sort(datos, 0, len(datos) - 1, 2)  # 2 = índice de la columna "edad"

# Mostrar resultados
print("=== Datos ordenados por edad (QuickSort) ===")
for fila in datos:
    print(fila)

# Opcional: Guardar en una nueva tabla
cursor.execute("CREATE TABLE IF NOT EXISTS Personas_QuickSorted AS SELECT * FROM Personas WHERE 1=0")
for fila in datos:
    cursor.execute("INSERT INTO Personas_QuickSorted VALUES (?, ?, ?, ?)", fila)
conn.commit()
conn.close()