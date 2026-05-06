import numpy as np
from .jacobi import (
    verificar_diagonal_dominante,
)  # Reutilizamos tu validación de InvenSoft


def gauss_seidel(A, b, tol, x0=None, max_iter=100):
    n = len(b)

    # --- Validación de Diagonal Dominante ---
    dominante, filas_problema = verificar_diagonal_dominante(A)
    if not dominante:
        print("\n" + "!" * 60)
        print(f"[!] ADVERTENCIA: La matriz no es dominante en filas: {filas_problema}")
        print("[!] Gauss-Seidel podría no converger.")
        print("!" * 60)

    if x0 is None:
        x0 = np.zeros(n)

    x_actual = x0.copy()

    # Encabezado de tabla
    headers = [f"x{i+1}" for i in range(n)] + ["Err Max"]
    print("\n" + "-" * (16 * (n + 2)))
    print(f"{'Iter':<5} | " + " | ".join([f"{h:<12}" for h in headers]))
    print("-" * (16 * (n + 2)))

    for it in range(max_iter):
        x_anterior = x_actual.copy()  # Guardamos para calcular el error

        for i in range(n):
            # usamos x_actual que ya tiene los valores
            # actualizados de las variables anteriores (x_1, x_2... x_{i-1})
            sumatoria = sum(A[i][j] * x_actual[j] for j in range(n) if i != j)
            x_actual[i] = (b[i] - sumatoria) / A[i][i]

        # Cálculo del error relativo máximo
        errores = [
            abs((x_actual[i] - x_anterior[i]) / x_actual[i]) if x_actual[i] != 0 else 0
            for i in range(n)
        ]
        error_max = max(errores)

        # Mostrar fila
        valores_fila = " | ".join([f"{val:<12.6f}" for val in x_actual])
        print(f"{it+1:<5} | {valores_fila} | {error_max:<12.6f}")

        if error_max < tol:
            print("-" * (16 * (n + 2)))
            return x_actual, it + 1

    print("-" * (16 * (n + 2)))
    return x_actual, max_iter
