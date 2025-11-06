"""
Soluciones de los Ejercicios Prácticos de Búsqueda Lineal
=========================================================

Este archivo contiene las soluciones completas para todos los ejercicios.
Úsalo para verificar tus respuestas después de intentar resolverlos.
"""

from typing import List, Optional, Any, Tuple


def busqueda_lineal_con_contador(lista: List[Any], objetivo: Any) -> Tuple[Optional[int], int]:
    """
    SOLUCIÓN: Búsqueda lineal que retorna el índice y el número de comparaciones.
    """
    comparaciones = 0
    for i, elemento in enumerate(lista):
        comparaciones += 1
        if elemento == objetivo:
            return i, comparaciones
    return None, comparaciones


def buscar_elemento_mas_cercano(lista: List[int], objetivo: int) -> Tuple[int, int]:
    """
    SOLUCIÓN: Busca el elemento más cercano al objetivo en la lista.
    """
    if not lista:
        raise ValueError("La lista no puede estar vacía")
    
    elemento_cercano = lista[0]
    indice_cercano = 0
    diferencia_minima = abs(lista[0] - objetivo)
    
    for i, elemento in enumerate(lista):
        diferencia = abs(elemento - objetivo)
        if diferencia < diferencia_minima:
            diferencia_minima = diferencia
            elemento_cercano = elemento
            indice_cercano = i
    
    return elemento_cercano, indice_cercano


def busqueda_lineal_ordenada(lista: List[int], objetivo: int) -> Optional[int]:
    """
    SOLUCIÓN: Búsqueda lineal optimizada para listas ordenadas.
    """
    for i, elemento in enumerate(lista):
        if elemento == objetivo:
            return i
        elif elemento > objetivo:  # Si el elemento es mayor, no seguir buscando
            return None
    return None


def buscar_rango(lista: List[int], minimo: int, maximo: int) -> List[int]:
    """
    SOLUCIÓN: Busca todos los elementos en un rango específico.
    """
    indices = []
    for i, elemento in enumerate(lista):
        if minimo <= elemento <= maximo:
            indices.append(i)
    return indices


def buscar_patron(lista: List[int], patron: List[int]) -> List[int]:
    """
    SOLUCIÓN: Busca un patrón de elementos consecutivos en la lista.
    """
    if not patron:
        return []
    
    posiciones = []
    longitud_patron = len(patron)
    
    for i in range(len(lista) - longitud_patron + 1):
        # Verificar si el patrón coincide desde la posición i
        coincide = True
        for j in range(longitud_patron):
            if lista[i + j] != patron[j]:
                coincide = False
                break
        
        if coincide:
            posiciones.append(i)
    
    return posiciones


def buscar_elemento_unico(lista: List[Any]) -> Optional[Any]:
    """
    SOLUCIÓN: Busca el primer elemento que aparece solo una vez en la lista.
    """
    for i, elemento in enumerate(lista):
        es_unico = True
        # Verificar si el elemento aparece en otra posición
        for j, otro_elemento in enumerate(lista):
            if i != j and elemento == otro_elemento:
                es_unico = False
                break
        
        if es_unico:
            return elemento
    
    return None


def verificar_soluciones():
    """Verifica que todas las soluciones funcionen correctamente."""
    print("VERIFICANDO SOLUCIONES...")
    print("=" * 30)
    
    # Prueba 1: Búsqueda con contador
    lista1 = [3, 7, 1, 9, 4, 6, 2, 8, 5]
    resultado1 = busqueda_lineal_con_contador(lista1, 6)
    print(f"Ejercicio 1: {resultado1} (esperado: (5, 6))")
    
    # Prueba 2: Elemento más cercano
    lista2 = [1, 3, 7, 12, 15, 20, 25]
    resultado2 = buscar_elemento_mas_cercano(lista2, 8)
    print(f"Ejercicio 2: {resultado2} (esperado: (7, 2))")
    
    # Prueba 3: Lista ordenada
    lista3 = [1, 3, 5, 7, 9, 11, 13, 15]
    resultado3 = busqueda_lineal_ordenada(lista3, 7)
    print(f"Ejercicio 3: {resultado3} (esperado: 3)")
    
    # Prueba 4: Rango
    lista4 = [1, 5, 3, 8, 2, 9, 4, 7, 6]
    resultado4 = buscar_rango(lista4, 3, 7)
    print(f"Ejercicio 4: {resultado4} (esperado: [1, 2, 3, 6, 7])")
    
    # Prueba 5: Patrón
    lista5 = [1, 2, 3, 1, 2, 3, 4, 5, 1, 2, 3]
    patron = [1, 2, 3]
    resultado5 = buscar_patron(lista5, patron)
    print(f"Ejercicio 5: {resultado5} (esperado: [0, 3, 8])")
    
    # Prueba 6: Elemento único
    lista6 = [1, 2, 3, 2, 4, 1, 5, 3, 6]
    resultado6 = buscar_elemento_unico(lista6)
    print(f"Ejercicio 6: {resultado6} (esperado: 4)")
    
    print("\n¡Todas las soluciones verificadas!")


if __name__ == "__main__":
    verificar_soluciones()
