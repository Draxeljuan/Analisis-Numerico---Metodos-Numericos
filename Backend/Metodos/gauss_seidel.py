import numpy as np
from .jacobi import verificar_diagonal_dominante

def gauss_seidel(A, b, tol, x0=None, max_iter=100):
    n = len(b)

    #  Validación de Diagonal Dominante
    dominante, filas_problema = verificar_diagonal_dominante(A)
    
    if x0 is None:
        x0 = np.zeros(n)

    x_actual = x0.copy()
    iteraciones_data = [] # Lista para almacenar el historial de iteraciones

    for it in range(max_iter):
        x_anterior = x_actual.copy()  # Guardamos el estado previo para calcular el error

        for i in range(n):
            # En Gauss-Seidel usamos x_actual que ya contiene los valores 
            # actualizados de las variables anteriores (x_1, x_2... x_{i-1})
            sumatoria = sum(A[i][j] * x_actual[j] for j in range(n) if i != j)
            x_actual[i] = (b[i] - sumatoria) / A[i][i]

        # Cálculo del error relativo máximo
        errores = [
            abs((x_actual[i] - x_anterior[i]) / x_actual[i]) if x_actual[i] != 0 else 0
            for i in range(n)
        ]
        error_max = max(errores)

        # Captura de datos para el frontend
        fila = {
            "iteracion": it + 1,
            "valores": x_actual.tolist(), # Convertimos a lista nativa para JSON
            "error": float(error_max)
        }
        iteraciones_data.append(fila)

        # Criterio de parada
        if error_max < tol:
            return x_actual.tolist(), it + 1, iteraciones_data, dominante

    # Retornamos solución final, total iteraciones, historial y estado de dominancia
    return x_actual.tolist(), max_iter, iteraciones_data, dominante