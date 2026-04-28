def biseccion(f, a, b, tol, max_iter=100):
    # Validar teorema de Bolzano
    if f(a) * f(b) >= 0:
        return None, "Error de signo"

    iteracion = 0
    m_anterior = 0

    # Imprimir encabezado de la tabla
    print("\n" + "-" * 105)
    print(
        f"{'Iter':<5} | {'a':<12} | {'b':<12} | {'m':<12} | {'f(m)':<15} | {'Err Relat':<12}"
    )
    print("-" * 105)

    while iteracion < max_iter:
        iteracion += 1
        # Punto medio (raiz aproximada)
        m = (a + b) / 2
        # Evaluar f(m) (o la raiz aproximada en la función)
        fm = f(m)

        # Cálculo del Error Relativo
        error_relativo = abs((m - m_anterior) / m) if m != 0 else 0

        # En la primera iteración el error relativo no es muy confiable (se deja ---),
        # pero a partir de la segunda se toma normalmente
        error_str = f"{error_relativo:<12.6f}" if iteracion > 1 else f"{'---':<12}"

        print(
            f"{iteracion:<5} | {a:<12.6f} | {b:<12.6f} | {m:<12.6f} | {fm:<15.6e} | {error_str}"
        )

        # Criterio de parada (excepto en la primera iteración)
        if iteracion > 1 and error_relativo < tol:
            break

        # Si f(m) es exactamente cero, hemos encontrado la raíz
        if fm == 0:
            break

        # Si f(a) y f(m) tienen signos opuestos, la raíz está entre a y m, entonces actualizamos b = m
        # De lo contrario, la raíz está entre m y b, entonces actualizamos a = m
        if f(a) * fm < 0:
            b = m
        else:
            a = m

        # Actualizamos el valor anterior de m para el cálculo del error relativo en la siguiente iteración
        m_anterior = m

    print("-" * 105)
    return m, iteracion
