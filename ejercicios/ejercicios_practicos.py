"""
Ejercicios Prácticos de Búsqueda Lineal
=======================================

Este archivo contiene ejercicios prácticos para reforzar el aprendizaje
de algoritmos de búsqueda lineal.

Completa las funciones marcadas con "TODO" y ejecuta las pruebas.
"""

from typing import List, Optional, Any, Tuple
import random


# =============================================================================
# EJERCICIO 1: Búsqueda Lineal con Contador
# =============================================================================

def busqueda_lineal_con_contador(lista: List[Any], objetivo: Any) -> Tuple[Optional[int], int]:
    """
    Implementa búsqueda lineal que retorna el índice y el número de comparaciones.
    
    TODO: Completa esta función
    - Recorre la lista elemento por elemento
    - Cuenta cada comparación realizada
    - Retorna una tupla (índice, número_comparaciones)
    - Si no encuentra el elemento, retorna (None, número_comparaciones)
    
    Args:
        lista: Lista donde buscar
        objetivo: Elemento a buscar
        
    Returns:
        Tupla con (índice del elemento, número de comparaciones)
    """
    # TODO: Implementa aquí tu código
    pass


# =============================================================================
# EJERCICIO 2: Búsqueda de Elemento Más Cercano
# =============================================================================

def buscar_elemento_mas_cercano(lista: List[int], objetivo: int) -> Tuple[int, int]:
    """
    Busca el elemento más cercano al objetivo en la lista.
    
    TODO: Completa esta función
    - Encuentra el elemento con la menor diferencia absoluta al objetivo
    - Retorna una tupla (elemento, índice)
    - Si hay empate, retorna el primero encontrado
    
    Args:
        lista: Lista de enteros donde buscar
        objetivo: Número objetivo
        
    Returns:
        Tupla con (elemento más cercano, índice)
    """
    # TODO: Implementa aquí tu código
    pass


# =============================================================================
# EJERCICIO 3: Búsqueda en Lista Ordenada (Optimizada)
# =============================================================================

def busqueda_lineal_ordenada(lista: List[int], objetivo: int) -> Optional[int]:
    """
    Búsqueda lineal optimizada para listas ordenadas.
    
    TODO: Completa esta función
    - Aprovecha que la lista está ordenada
    - Para si encuentra un elemento mayor al objetivo
    - Retorna el índice del elemento o None si no existe
    
    Args:
        lista: Lista ordenada de enteros
        objetivo: Elemento a buscar
        
    Returns:
        Índice del elemento si existe, None si no
    """
    # TODO: Implementa aquí tu código
    pass


# =============================================================================
# EJERCICIO 4: Búsqueda de Rango
# =============================================================================

def buscar_rango(lista: List[int], minimo: int, maximo: int) -> List[int]:
    """
    Busca todos los elementos en un rango específico.
    
    TODO: Completa esta función
    - Encuentra todos los elementos entre minimo y maximo (inclusive)
    - Retorna una lista con los índices de estos elementos
    
    Args:
        lista: Lista de enteros
        minimo: Valor mínimo del rango
        maximo: Valor máximo del rango
        
    Returns:
        Lista de índices de elementos en el rango
    """
    # TODO: Implementa aquí tu código
    pass


# =============================================================================
# EJERCICIO 5: Búsqueda de Patrón
# =============================================================================

def buscar_patron(lista: List[int], patron: List[int]) -> List[int]:
    """
    Busca un patrón de elementos consecutivos en la lista.
    
    TODO: Completa esta función
    - Encuentra todas las posiciones donde aparece el patrón
    - El patrón debe aparecer consecutivamente
    
    Args:
        lista: Lista donde buscar
        patron: Lista de elementos que forman el patrón
        
    Returns:
        Lista de índices donde comienza el patrón
    """
    # TODO: Implementa aquí tu código
    pass


# =============================================================================
# EJERCICIO 6: Búsqueda de Elemento Único
# =============================================================================

def buscar_elemento_unico(lista: List[Any]) -> Optional[Any]:
    """
    Busca el primer elemento que aparece solo una vez en la lista.
    
    TODO: Completa esta función
    - Encuentra el primer elemento que no tiene duplicados
    - Usa búsqueda lineal para verificar duplicados
    
    Args:
        lista: Lista donde buscar
        
    Returns:
        Primer elemento único encontrado, None si no existe
    """
    # TODO: Implementa aquí tu código
    pass


# =============================================================================
# FUNCIONES DE PRUEBA
# =============================================================================

def probar_ejercicio_1():
    """Prueba el Ejercicio 1: Búsqueda con contador."""
    print("=== PRUEBA EJERCICIO 1: Búsqueda con Contador ===")
    
    lista = [3, 7, 1, 9, 4, 6, 2, 8, 5]
    objetivo = 6
    
    resultado = busqueda_lineal_con_contador(lista, objetivo)
    print(f"Lista: {lista}")
    print(f"Buscando: {objetivo}")
    print(f"Resultado: {resultado}")
    
    # Verificar resultado esperado
    if resultado[0] == 5 and resultado[1] == 6:
        print("✅ ¡Correcto!")
    else:
        print("❌ Incorrecto. Esperado: (5, 6)")
    print()


def probar_ejercicio_2():
    """Prueba el Ejercicio 2: Elemento más cercano."""
    print("=== PRUEBA EJERCICIO 2: Elemento Más Cercano ===")
    
    lista = [1, 3, 7, 12, 15, 20, 25]
    objetivo = 8
    
    resultado = buscar_elemento_mas_cercano(lista, objetivo)
    print(f"Lista: {lista}")
    print(f"Objetivo: {objetivo}")
    print(f"Resultado: {resultado}")
    
    # Verificar resultado esperado
    if resultado[0] == 7 and resultado[1] == 2:
        print("✅ ¡Correcto!")
    else:
        print("❌ Incorrecto. Esperado: (7, 2)")
    print()


def probar_ejercicio_3():
    """Prueba el Ejercicio 3: Búsqueda en lista ordenada."""
    print("=== PRUEBA EJERCICIO 3: Búsqueda en Lista Ordenada ===")
    
    lista = [1, 3, 5, 7, 9, 11, 13, 15]
    objetivo = 7
    
    resultado = busqueda_lineal_ordenada(lista, objetivo)
    print(f"Lista ordenada: {lista}")
    print(f"Buscando: {objetivo}")
    print(f"Resultado: {resultado}")
    
    # Verificar resultado esperado
    if resultado == 3:
        print("✅ ¡Correcto!")
    else:
        print("❌ Incorrecto. Esperado: 3")
    print()


def probar_ejercicio_4():
    """Prueba el Ejercicio 4: Búsqueda de rango."""
    print("=== PRUEBA EJERCICIO 4: Búsqueda de Rango ===")
    
    lista = [1, 5, 3, 8, 2, 9, 4, 7, 6]
    minimo, maximo = 3, 7
    
    resultado = buscar_rango(lista, minimo, maximo)
    print(f"Lista: {lista}")
    print(f"Rango: [{minimo}, {maximo}]")
    print(f"Resultado: {resultado}")
    
    # Verificar resultado esperado
    resultado_esperado = [1, 2, 3, 6, 7]  # índices de elementos en rango
    if set(resultado) == set(resultado_esperado):
        print("✅ ¡Correcto!")
    else:
        print(f"❌ Incorrecto. Esperado: {resultado_esperado}")
    print()


def probar_ejercicio_5():
    """Prueba el Ejercicio 5: Búsqueda de patrón."""
    print("=== PRUEBA EJERCICIO 5: Búsqueda de Patrón ===")
    
    lista = [1, 2, 3, 1, 2, 3, 4, 5, 1, 2, 3]
    patron = [1, 2, 3]
    
    resultado = buscar_patron(lista, patron)
    print(f"Lista: {lista}")
    print(f"Patrón: {patron}")
    print(f"Resultado: {resultado}")
    
    # Verificar resultado esperado
    resultado_esperado = [0, 3, 8]  # posiciones donde comienza el patrón
    if set(resultado) == set(resultado_esperado):
        print("✅ ¡Correcto!")
    else:
        print(f"❌ Incorrecto. Esperado: {resultado_esperado}")
    print()


def probar_ejercicio_6():
    """Prueba el Ejercicio 6: Elemento único."""
    print("=== PRUEBA EJERCICIO 6: Elemento Único ===")
    
    lista = [1, 2, 3, 2, 4, 1, 5, 3, 6]
    
    resultado = buscar_elemento_unico(lista)
    print(f"Lista: {lista}")
    print(f"Resultado: {resultado}")
    
    # Verificar resultado esperado
    if resultado == 4:  # el primer elemento único es 4
        print("✅ ¡Correcto!")
    else:
        print("❌ Incorrecto. Esperado: 4")
    print()


def ejecutar_todas_las_pruebas():
    """Ejecuta todas las pruebas de los ejercicios."""
    print("EJERCICIOS PRÁCTICOS DE BÚSQUEDA LINEAL")
    print("=" * 50)
    print("Completa las funciones marcadas con 'TODO' y ejecuta las pruebas.\n")
    
    probar_ejercicio_1()
    probar_ejercicio_2()
    probar_ejercicio_3()
    probar_ejercicio_4()
    probar_ejercicio_5()
    probar_ejercicio_6()
    
    print("=" * 50)
    print("¡Pruebas completadas!")


if __name__ == "__main__":
    ejecutar_todas_las_pruebas()
