def algoritmo_recursivo(n):
    # Caso base: cuando el tamaño del problema es muy pequeño (por ejemplo, 1)
    if n <= 1:
        return 0  # o algún valor base adecuado
    
    # Dividir el problema en 3 subproblemas de tamaño n/4
    subproblema1 = algoritmo_recursivo(n // 4)
    subproblema2 = algoritmo_recursivo(n // 4)
    subproblema3 = algoritmo_recursivo(n // 4)

    # Trabajo de combinación: O(n^2)
    trabajo_combinacion = n ** 2

    # Resultado total
    return subproblema1 + subproblema2 + subproblema3 + trabajo_combinacion

# Ejemplo de uso
n = 16  # Ejemplo con un tamaño de problema de 16
resultado = algoritmo_recursivo(n)
print(f"Resultado para n={n}: {resultado}")
