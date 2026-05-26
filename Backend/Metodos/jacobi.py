import numpy as np

def verificar_diagonal_dominante(A):
    """
    Mantenemos esta lógica para informar al frontend si la matriz es apta.
    """
    n = len(A)
    es_dominante = True
    filas_no_dominantes = []

    for i in range(n):
        diagonal = abs(A[i][i])
        suma_otros = sum(abs(A[i][j]) for j in range(n) if i != j)

        if diagonal <= suma_otros:
            es_dominante = False
            filas_no_dominantes.append(i)

    return es_dominante, filas_no_dominantes

def jacobi(A, b, tol, x0=None, max_iter=100):
    n = len(A)
    
    # Validación de diagonal dominante
    dominante, filas_problema = verificar_diagonal_dominante(A)
    
    if x0 is None:
        x0 = np.zeros(n)

    x_actual = np.copy(x0)
    iteraciones_data = [] # Historial para el JSON

    for iteracion in range(max_iter):
        x_nuevo = np.zeros(n)

        for i in range(n):
            # sumatoria = sum(A_ij * x_actual_j) para j != i
            sumatoria = sum(A[i][j] * x_actual[j] for j in range(n) if j != i)
            x_nuevo[i] = (b[i] - sumatoria) / A[i][i]

        # Cálculo del error relativo máximo
        errores = [
            abs((x_nuevo[i] - x_actual[i]) / x_nuevo[i]) if x_nuevo[i] != 0 else 0
            for i in range(n)
        ]
        error_max = max(errores)

        # 2. Captura de datos de la iteración
        fila = {
            "iteracion": iteracion + 1,
            "valores": x_nuevo.tolist(), # Convertimos a lista nativa de Python
            "error": float(error_max)
        }
        iteraciones_data.append(fila)

        # Criterio de parada
        if error_max < tol:
            # Retornamos: solución, iters, historial y estado de dominancia
            return x_nuevo.tolist(), iteracion + 1, iteraciones_data, dominante

        x_actual = x_nuevo.copy()

    return x_actual.tolist(), max_iter, iteraciones_data, dominante