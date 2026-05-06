import numpy as np


def verificar_diagonal_dominante(A):
    """
    Analizamos si la matriz A (digitada) cumple con la condición de diagonal dominante,
    es decir, para cada fila i, el valor absoluto del elemento diagonal A[i][i] debe ser
    mayor que la suma de los valores absolutos de los otros elementos en esa fila.
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
    if not dominante:
        print("\n" + "!" * 60)
        print(
            f"[!] ADVERTENCIA: La matriz no es estrictamente dominante en las filas: {filas_problema}"
        )
        print(
            "[!] El método podría divergir o tardar muchas más iteraciones en converger."
        )
        print("!" * 60)

    if x0 is None:
        x0 = np.zeros(n)

    x_actual = np.copy(x0)

    # Encabezado de la tabla
    headers = [f"x{i+1}" for i in range(n)] + ["Err Max"]
    print("\n" + "-" * (16 * (n + 2)))
    header_str = f"{'Iter':<5} | " + " | ".join([f"{h:<12}" for h in headers])
    print(header_str)
    print("-" * (16 * (n + 2)))

    for iteracion in range(max_iter):
        x_nuevo = np.zeros(n)

        for i in range(n):
            # Despeje
            # x_i = (b_i - sum(A_ij * x_j)) / A_ii
            sumatoria = sum(A[i][j] * x_actual[j] for j in range(n) if j != i)
            x_nuevo[i] = (b[i] - sumatoria) / A[i][i]

        # Calculo del error relativo
        errores = [
            abs((x_nuevo[i] - x_actual[i]) / x_nuevo[i]) if x_nuevo[i] != 0 else 0
            for i in range(n)
        ]
        error_max = max(errores)

        # Mostrar fila
        valores_fila = " | ".join([f"{val:<12.6f}" for val in x_nuevo])
        print(f"{iteracion+1:<5} | {valores_fila} | {error_max:<12.6f}")

        if error_max < tol:
            print("-" * (16 * (n + 2)))
            return x_nuevo, iteracion + 1

        x_actual = x_nuevo.copy()

    print("-" * (16 * (n + 2)))
    return x_actual, max_iter
