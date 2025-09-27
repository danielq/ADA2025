# Función para combinar dos sublistas de empleados ordenadas por salario
def merge(left, right):
    result = []
    i = j = 0
    
    # Comparar los salarios de los empleados en ambas sublistas y agregar el menor a 'result'
    while i < len(left) and j < len(right):
        if left[i]['salario'] < right[j]['salario']:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Agregar los empleados restantes de 'left' o 'right'
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# Función principal de Merge Sort con impresión de cada paso de la división
def merge_sort(arr, level=0):
    print(f"{'  ' * level}División Nivel {level}: {arr}")
    
    # Caso base: Si la lista tiene 1 o 0 elementos, ya está ordenada
    if len(arr) <= 1:
        return arr
    
    # Dividir la lista en dos mitades
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Llamada recursiva para ordenar ambas mitades
    left = merge_sort(left, level + 1)
    right = merge_sort(right, level + 1)
    
    # Combinar las dos mitades ordenadas
    merged = merge(left, right)
    
    print(f"{'  ' * level}Combinación Nivel {level}: {merged}")
    
    return merged

# Lista de empleados con nombre, apellido y salario
empleados = [
    {'nombre': 'Ana', 'apellido': 'Gómez', 'salario': 55000},
    {'nombre': 'Carlos', 'apellido': 'Martínez', 'salario': 70000},
    {'nombre': 'Luis', 'apellido': 'Pérez', 'salario': 45000},
    {'nombre': 'Marta', 'apellido': 'Díaz', 'salario': 62000},
    {'nombre': 'Juan', 'apellido': 'Hernández', 'salario': 55000},
    {'nombre': 'Sofía', 'apellido': 'García', 'salario': 80000},
    {'nombre': 'David', 'apellido': 'Lopez', 'salario': 60000}
]

# Ordenar los empleados por salario
print("Lista original de empleados:")
for empleado in empleados:
    print(empleado)

sorted_empleados = merge_sort(empleados)

# Mostrar el resultado final
print("\nLista final de empleados ordenados por salario:")
for empleado in sorted_empleados:
    print(empleado)
