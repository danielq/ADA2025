"""
Implementaciones de Algoritmos de Búsqueda Lineal en Python
==========================================================

Este archivo contiene diferentes implementaciones de búsqueda lineal
con ejemplos prácticos y análisis de complejidad.

Autor: Asistente de Programación
Fecha: 2025
"""

from typing import List, Optional, Any, Tuple
import time


def busqueda_lineal_basica(lista: List[Any], objetivo: Any) -> Optional[int]:
    """
    Búsqueda lineal básica que retorna el índice del primer elemento encontrado.
    
    Args:
        lista: Lista donde buscar
        objetivo: Elemento a buscar
        
    Returns:
        Índice del elemento si se encuentra, None si no existe
        
    Complejidad temporal: O(n)
    Complejidad espacial: O(1)
    """
    for i, elemento in enumerate(lista):
        if elemento == objetivo:
            return i
    return None


def busqueda_lineal_todas_ocurrencias(lista: List[Any], objetivo: Any) -> List[int]:
    """
    Búsqueda lineal que retorna todos los índices donde aparece el elemento.
    
    Args:
        lista: Lista donde buscar
        objetivo: Elemento a buscar
        
    Returns:
        Lista de índices donde aparece el elemento
        
    Complejidad temporal: O(n)
    Complejidad espacial: O(k) donde k es el número de ocurrencias
    """
    indices = []
    for i, elemento in enumerate(lista):
        if elemento == objetivo:
            indices.append(i)
    return indices


def busqueda_lineal_ultima_ocurrencia(lista: List[Any], objetivo: Any) -> Optional[int]:
    """
    Búsqueda lineal que retorna el índice de la última ocurrencia del elemento.
    
    Args:
        lista: Lista donde buscar
        objetivo: Elemento a buscar
        
    Returns:
        Índice de la última ocurrencia, None si no existe
        
    Complejidad temporal: O(n)
    Complejidad espacial: O(1)
    """
    ultimo_indice = None
    for i, elemento in enumerate(lista):
        if elemento == objetivo:
            ultimo_indice = i
    return ultimo_indice


def busqueda_lineal_objetos(lista: List[dict], clave: str, valor: Any) -> Optional[int]:
    """
    Búsqueda lineal en una lista de diccionarios por una clave específica.
    
    Args:
        lista: Lista de diccionarios
        clave: Clave a buscar en los diccionarios
        valor: Valor a buscar
        
    Returns:
        Índice del primer diccionario que contiene la clave-valor, None si no existe
        
    Complejidad temporal: O(n)
    Complejidad espacial: O(1)
    """
    for i, diccionario in enumerate(lista):
        if diccionario.get(clave) == valor:
            return i
    return None


def busqueda_lineal_condicion(lista: List[Any], condicion) -> Optional[int]:
    """
    Búsqueda lineal usando una función de condición personalizada.
    
    Args:
        lista: Lista donde buscar
        condicion: Función que retorna True si el elemento cumple la condición
        
    Returns:
        Índice del primer elemento que cumple la condición, None si no existe
        
    Complejidad temporal: O(n)
    Complejidad espacial: O(1)
    """
    for i, elemento in enumerate(lista):
        if condicion(elemento):
            return i
    return None


def busqueda_lineal_mejorado(lista: List[Any], objetivo: Any) -> Tuple[Optional[int], int]:
    """
    Búsqueda lineal mejorada que también retorna el número de comparaciones realizadas.
    
    Args:
        lista: Lista donde buscar
        objetivo: Elemento a buscar
        
    Returns:
        Tupla con (índice del elemento, número de comparaciones)
        
    Complejidad temporal: O(n)
    Complejidad espacial: O(1)
    """
    comparaciones = 0
    for i, elemento in enumerate(lista):
        comparaciones += 1
        if elemento == objetivo:
            return i, comparaciones
    return None, comparaciones


def medir_tiempo_busqueda(funcion, *args, **kwargs):
    """
    Función auxiliar para medir el tiempo de ejecución de una función de búsqueda.
    
    Args:
        funcion: Función de búsqueda a medir
        *args: Argumentos posicionales para la función
        **kwargs: Argumentos con nombre para la función
        
    Returns:
        Tupla con (resultado de la función, tiempo de ejecución en segundos)
    """
    inicio = time.time()
    resultado = funcion(*args, **kwargs)
    fin = time.time()
    return resultado, fin - inicio


def ejemplo_uso_basico():
    """Ejemplo básico de uso de las funciones de búsqueda lineal."""
    print("=== EJEMPLO BÁSICO DE BÚSQUEDA LINEAL ===\n")
    
    # Lista de ejemplo
    numeros = [3, 7, 1, 9, 4, 6, 2, 8, 5, 1]
    print(f"Lista: {numeros}")
    print(f"Tamaño de la lista: {len(numeros)}")
    
    # Búsqueda básica
    objetivo = 6
    indice = busqueda_lineal_basica(numeros, objetivo)
    print(f"\nBúsqueda de {objetivo}:")
    print(f"Índice encontrado: {indice}")
    
    # Búsqueda de todas las ocurrencias
    objetivo = 1
    indices = busqueda_lineal_todas_ocurrencias(numeros, objetivo)
    print(f"\nTodas las ocurrencias de {objetivo}:")
    print(f"Índices: {indices}")
    
    # Búsqueda de última ocurrencia
    ultimo_indice = busqueda_lineal_ultima_ocurrencia(numeros, objetivo)
    print(f"Última ocurrencia en índice: {ultimo_indice}")
    
    # Búsqueda con condición
    def es_par(x):
        return x % 2 == 0
    
    indice_par = busqueda_lineal_condicion(numeros, es_par)
    print(f"\nPrimer número par en índice: {indice_par}")


def ejemplo_uso_objetos():
    """Ejemplo de búsqueda en lista de objetos/diccionarios."""
    print("\n=== EJEMPLO CON OBJETOS ===\n")
    
    # Lista de estudiantes
    estudiantes = [
        {"nombre": "Ana", "edad": 20, "carrera": "Ingeniería"},
        {"nombre": "Carlos", "edad": 22, "carrera": "Medicina"},
        {"nombre": "María", "edad": 19, "carrera": "Ingeniería"},
        {"nombre": "Luis", "edad": 21, "carrera": "Derecho"},
        {"nombre": "Sofia", "edad": 20, "carrera": "Ingeniería"}
    ]
    
    print("Lista de estudiantes:")
    for i, estudiante in enumerate(estudiantes):
        print(f"{i}: {estudiante}")
    
    # Búsqueda por nombre
    indice = busqueda_lineal_objetos(estudiantes, "nombre", "María")
    print(f"\nBúsqueda por nombre 'María': índice {indice}")
    
    # Búsqueda por carrera
    indice = busqueda_lineal_objetos(estudiantes, "carrera", "Ingeniería")
    print(f"Primer estudiante de Ingeniería: índice {indice}")
    
    # Búsqueda por edad usando condición
    def edad_mayor_20(estudiante):
        return estudiante["edad"] > 20
    
    indice = busqueda_lineal_condicion(estudiantes, edad_mayor_20)
    print(f"Primer estudiante mayor de 20 años: índice {indice}")


def ejemplo_analisis_rendimiento():
    """Ejemplo de análisis de rendimiento de búsqueda lineal."""
    print("\n=== ANÁLISIS DE RENDIMIENTO ===\n")
    
    import random
    
    # Generar listas de diferentes tamaños
    tamanos = [100, 1000, 10000]
    
    for tamano in tamanos:
        # Generar lista aleatoria
        lista = [random.randint(1, 1000) for _ in range(tamano)]
        objetivo = random.choice(lista)  # Asegurar que el objetivo existe
        
        # Medir tiempo de búsqueda
        resultado, tiempo = medir_tiempo_busqueda(busqueda_lineal_mejorado, lista, objetivo)
        indice, comparaciones = resultado
        
        print(f"Lista de tamaño {tamano}:")
        print(f"  Tiempo: {tiempo:.6f} segundos")
        print(f"  Comparaciones: {comparaciones}")
        print(f"  Índice encontrado: {indice}")
        print()


def ejemplo_casos_especiales():
    """Ejemplos de casos especiales en búsqueda lineal."""
    print("\n=== CASOS ESPECIALES ===\n")
    
    # Lista vacía
    print("1. Lista vacía:")
    resultado = busqueda_lineal_basica([], 5)
    print(f"   Resultado: {resultado}")
    
    # Lista con un solo elemento
    print("\n2. Lista con un elemento:")
    resultado = busqueda_lineal_basica([42], 42)
    print(f"   Buscar 42 en [42]: {resultado}")
    
    # Elemento no encontrado
    print("\n3. Elemento no encontrado:")
    resultado = busqueda_lineal_basica([1, 2, 3, 4, 5], 99)
    print(f"   Buscar 99 en [1,2,3,4,5]: {resultado}")
    
    # Lista con elementos duplicados
    print("\n4. Lista con duplicados:")
    lista_duplicados = [1, 2, 3, 2, 4, 2, 5]
    todas_ocurrencias = busqueda_lineal_todas_ocurrencias(lista_duplicados, 2)
    print(f"   Todas las ocurrencias de 2 en {lista_duplicados}: {todas_ocurrencias}")


def main():
    """Función principal que ejecuta todos los ejemplos."""
    print("ALGORITMOS DE BÚSQUEDA LINEAL EN PYTHON")
    print("=" * 50)
    
    # Ejecutar ejemplos
    ejemplo_uso_basico()
    ejemplo_uso_objetos()
    ejemplo_analisis_rendimiento()
    ejemplo_casos_especiales()
    
    print("\n" + "=" * 50)
    print("¡Todos los ejemplos completados!")


if __name__ == "__main__":
    main()
