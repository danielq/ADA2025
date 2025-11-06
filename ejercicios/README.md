# Algoritmos de Búsqueda Lineal en Python

Este repositorio contiene implementaciones completas y ejercicios prácticos de algoritmos de búsqueda lineal en Python.

## 📁 Archivos Incluidos

### 1. `busqueda_lineal.py`
Archivo principal con implementaciones completas de diferentes variantes de búsqueda lineal:

- **Búsqueda lineal básica**: Encuentra el primer elemento que coincide
- **Búsqueda de todas las ocurrencias**: Retorna todos los índices donde aparece el elemento
- **Búsqueda de última ocurrencia**: Encuentra la última aparición del elemento
- **Búsqueda en objetos**: Busca en listas de diccionarios por clave-valor
- **Búsqueda con condición**: Usa funciones personalizadas para la búsqueda
- **Búsqueda mejorada**: Incluye contador de comparaciones

### 2. `ejercicios_practicos.py`
Ejercicios para practicar y reforzar el aprendizaje:

- **Ejercicio 1**: Búsqueda con contador de comparaciones
- **Ejercicio 2**: Búsqueda del elemento más cercano
- **Ejercicio 3**: Búsqueda optimizada en listas ordenadas
- **Ejercicio 4**: Búsqueda de elementos en un rango
- **Ejercicio 5**: Búsqueda de patrones consecutivos
- **Ejercicio 6**: Búsqueda del primer elemento único

### 3. `soluciones.py`
Soluciones completas para todos los ejercicios prácticos.

## 🚀 Cómo Usar

### Ejecutar el archivo principal
```bash
python busqueda_lineal.py
```

### Practicar con ejercicios
1. Abre `ejercicios_practicos.py`
2. Completa las funciones marcadas con "TODO"
3. Ejecuta el archivo para ver las pruebas
4. Compara tus resultados con `soluciones.py`

### Verificar soluciones
```bash
python soluciones.py
```

## 📊 Análisis de Complejidad

### Complejidad Temporal
- **Mejor caso**: O(1) - El elemento está en la primera posición
- **Caso promedio**: O(n/2) - El elemento está en el medio
- **Peor caso**: O(n) - El elemento no existe o está al final

### Complejidad Espacial
- **Todas las variantes**: O(1) - Solo usa espacio constante
- **Excepción**: Búsqueda de todas las ocurrencias usa O(k) donde k es el número de ocurrencias

## 🔍 Características de la Búsqueda Lineal

### Ventajas
- ✅ Simple de implementar
- ✅ Funciona con listas no ordenadas
- ✅ No requiere espacio adicional (excepto algunas variantes)
- ✅ Funciona con cualquier tipo de datos

### Desventajas
- ❌ Complejidad O(n) en el peor caso
- ❌ No aprovecha listas ordenadas
- ❌ Puede ser lenta para listas grandes

## 📝 Ejemplos de Uso

### Búsqueda Básica
```python
lista = [3, 7, 1, 9, 4, 6, 2, 8, 5]
indice = busqueda_lineal_basica(lista, 6)
print(f"Elemento 6 encontrado en índice: {indice}")
```

### Búsqueda en Objetos
```python
estudiantes = [
    {"nombre": "Ana", "edad": 20},
    {"nombre": "Carlos", "edad": 22}
]
indice = busqueda_lineal_objetos(estudiantes, "nombre", "Ana")
print(f"Ana encontrada en índice: {indice}")
```

### Búsqueda con Condición
```python
def es_par(x):
    return x % 2 == 0

lista = [1, 2, 3, 4, 5, 6]
indice = busqueda_lineal_condicion(lista, es_par)
print(f"Primer número par en índice: {indice}")
```

## 🎯 Cuándo Usar Búsqueda Lineal

### Usa búsqueda lineal cuando:
- La lista no está ordenada
- Necesitas encontrar todas las ocurrencias
- La lista es pequeña
- Necesitas flexibilidad en los criterios de búsqueda

### Considera alternativas cuando:
- La lista está ordenada (usa búsqueda binaria)
- La lista es muy grande
- Necesitas búsquedas muy frecuentes

## 📚 Conceptos Clave

1. **Iteración secuencial**: Recorre la lista elemento por elemento
2. **Comparación directa**: Compara cada elemento con el objetivo
3. **Terminación temprana**: Para cuando encuentra el elemento
4. **Flexibilidad**: Puede adaptarse a diferentes criterios de búsqueda

## 🔧 Mejoras y Optimizaciones

1. **Listas ordenadas**: Para si encuentra un elemento mayor al objetivo
2. **Contador de comparaciones**: Útil para análisis de rendimiento
3. **Búsqueda bidireccional**: Busca desde ambos extremos
4. **Búsqueda con sentinela**: Usa un elemento especial para evitar verificaciones de límite

## 📖 Recursos Adicionales

- [Algoritmos de Búsqueda - Wikipedia](https://es.wikipedia.org/wiki/Algoritmo_de_búsqueda)
- [Complejidad Computacional - Khan Academy](https://es.khanacademy.org/computing/computer-science/algorithms)
- [Estructuras de Datos en Python - Real Python](https://realpython.com/python-data-structures/)

---

¡Disfruta aprendiendo sobre algoritmos de búsqueda lineal! 🚀
