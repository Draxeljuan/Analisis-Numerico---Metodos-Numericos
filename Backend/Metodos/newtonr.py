from sympy import diff, symbols, lambdify

def newton_raphson(f_func, f_expr, x_inicial, tol, incognita, max_iter=100):
    """
    Versión para API: Retorna (raíz, total_iteraciones, historial_datos).
    """
    # 1. Preparación de la derivada simbólica
    x_sym = symbols(incognita)
    df_expr = diff(f_expr, x_sym)
    df_func = lambdify(x_sym, df_expr, modules=["numpy", "math"])

    x = x_inicial
    iteracion = 0
    iteraciones_data = [] # Lista para el historial JSON

    while iteracion < max_iter:
        iteracion += 1

        fx = float(f_func(x))
        dfx = float(df_func(x))

        # Validación técnica: Evitar división por cero
        if dfx == 0:
            # Retornamos lo acumulado hasta ahora con un indicador de error
            return None, iteracion, iteraciones_data

        # Aplicación de la fórmula: 
        r = x - (fx / dfx)

        # Cálculo del Error Relativo: 
        error_relativo = abs((r - x) / r) if r != 0 else 0

        # Guardamos la fila antes de actualizar x para el siguiente ciclo
        fila = {
            "iteracion": iteracion,
            "x_n": float(x),
            "f_x": float(fx),
            "df_x": float(dfx),
            "error": float(error_relativo)
        }
        iteraciones_data.append(fila)

        # Criterio de parada
        if error_relativo < tol:
            return r, iteracion, iteraciones_data

        # Actualización para la siguiente vuelta
        x = r

    return x, iteracion, iteraciones_data
