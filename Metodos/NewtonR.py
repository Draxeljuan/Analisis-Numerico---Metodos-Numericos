from sympy import diff, symbols, lambdify


def newton_raphson(f_func, f_expr, x_inicial, tol, incognita, max_iter=100):
    # f_func: función ejecutable
    # f_expr: expresión simbólica de sympy para derivar

    x_sym = symbols(incognita)  # Asumimos 'x'
    df_expr = diff(f_expr, x_sym)
    df_func = lambdify(x_sym, df_expr)

    x = x_inicial
    iteracion = 0

    print("\n" + "-" * 100)
    print(
        f"{'Iter':<5} | {'x_n':<15} | {'f(x_n)':<15} | {'df(x_n)':<15} | {'Error Rel':<15}"
    )
    print("-" * 100)

    while iteracion < max_iter:
        iteracion += 1

        fx = f_func(x)
        dfx = df_func(x)

        if dfx == 0:
            return None, "Error: Derivada cero. El método no puede continuar."

        # Nueva raiz: r = x - f(x)/df(x)
        r = x - (fx / dfx)

        # Error relativo: |(r - x) / r|
        error_relativo = abs((r - x) / r) if r != 0 else 0

        if error_relativo < tol:

            # Imprimir la última iteración antes de retornar

            x = r  # Actualizamos x para mostrar el valor final en la tabla

            print(
                f"{iteracion:<5} | {x:<15.8f} | {fx:<15.6e} | {dfx:<15.6e} | {error_relativo:<15.8f}"
            )

            return r, iteracion

        # Actualización para la siguiente vuelta: x = r
        x = r

        # Imprimir fila con formato decimal
        print(
            f"{iteracion:<5} | {x:<15.8f} | {fx:<15.6e} | {dfx:<15.6e} | {error_relativo:<15.8f}"
        )

    # Retorna el resultado final, ya sea porque se llego a la raiz
    # o porque se alcanzó el máximo de iteraciones
    print("-" * 100)
    return x, max_iter
