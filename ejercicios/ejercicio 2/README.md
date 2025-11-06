# Sistema de Búsqueda Lineal - Empleados

Este proyecto implementa un sistema de búsqueda lineal con una interfaz gráfica para buscar entre 1000 empleados generados aleatoriamente.

## Características

- **1000 empleados** con datos aleatorios (nombre, apellido, departamento, salario, edad, email, teléfono)
- **Búsqueda lineal** implementada desde cero
- **Interfaz gráfica** intuitiva con tkinter
- **Búsqueda flexible** por cualquier campo o en todos los campos
- **Estadísticas en tiempo real** (comparaciones, tiempo de búsqueda)
- **Visualización de resultados** en tabla ordenada

## Archivos del Proyecto

- `empleados.py` - Clases para generar empleados y implementar búsqueda lineal
- `interfaz_grafica.py` - Interfaz gráfica principal
- `README.md` - Este archivo de documentación

## Estructura de Datos

Cada empleado contiene:
- **ID**: Identificador único
- **Nombre**: Nombre del empleado
- **Apellido**: Apellido del empleado
- **Departamento**: Área de trabajo
- **Salario**: Salario anual en euros
- **Edad**: Edad del empleado
- **Email**: Correo electrónico corporativo
- **Teléfono**: Número de teléfono

## Algoritmo de Búsqueda Lineal

El algoritmo implementado:
1. Recorre secuencialmente todos los empleados
2. Compara el valor de búsqueda con cada campo
3. Retorna todos los empleados que coincidan
4. Registra estadísticas de rendimiento

### Complejidad
- **Tiempo**: O(n) donde n es el número de empleados
- **Espacio**: O(1) adicional

## Cómo Usar

### Ejecutar la Aplicación

```bash
python interfaz_grafica.py
```

### Funcionalidades de la Interfaz

1. **Campo de Búsqueda**: Ingresa el término a buscar
2. **Campo Específico**: Selecciona en qué campo buscar o "Todos los campos"
3. **Botón Buscar**: Ejecuta la búsqueda
4. **Botón Limpiar**: Limpia la búsqueda actual
5. **Mostrar Todos**: Muestra todos los 1000 empleados

### Tipos de Búsqueda

- **Búsqueda por Campo Específico**: Busca solo en el campo seleccionado
- **Búsqueda Global**: Busca en todos los campos simultáneamente
- **Búsqueda Parcial**: Encuentra coincidencias parciales (no exactas)

### Ejemplos de Búsqueda

- Buscar "Ana" en "Nombre" → Encuentra todos los empleados llamados Ana
- Buscar "Ventas" en "Departamento" → Encuentra todos los empleados de Ventas
- Buscar "50000" en "Salario" → Encuentra empleados con salarios que contengan 50000
- Buscar "gmail" en "Todos los campos" → Encuentra empleados con gmail en cualquier campo

## Estadísticas Mostradas

- **Total empleados**: Número total de empleados cargados
- **Resultados encontrados**: Número de empleados que coinciden con la búsqueda
- **Comparaciones realizadas**: Número de comparaciones hechas durante la búsqueda
- **Tiempo de búsqueda**: Tiempo transcurrido en segundos

## Requisitos

- Python 3.6+
- tkinter (incluido con Python)
- threading (incluido con Python)
- dataclasses (Python 3.7+)

## Notas Técnicas

- Los empleados se generan con datos aleatorios pero realistas
- La búsqueda es case-insensitive (no distingue mayúsculas/minúsculas)
- La interfaz se actualiza en tiempo real
- El sistema es completamente funcional sin dependencias externas
