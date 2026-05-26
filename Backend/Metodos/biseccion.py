def biseccion(f, a, b, tol, max_iter=100):
    # Validar teorema de Bolzano
    if f(a) * f(b) >= 0:
        return None, 0, [] # Retornamos lista vacía en caso de error

    iteraciones_data = [] # Lista para capturar los datos de la tabla
    iteracion = 0
    m_anterior = 0

    while iteracion < max_iter:
        iteracion += 1
        m = (a + b) / 2
        fm = f(m)
        error_relativo = abs((m - m_anterior) / m) if m != 0 else 0

        # Guardamos la información de esta iteración en un diccionario
        fila = {
            "iteracion": iteracion,
            "a": float(a),
            "b": float(b),
            "m": float(m),
            "fm": float(fm),
            "error": float(error_relativo) if iteracion > 1 else None
        }
        iteraciones_data.append(fila)

        # Criterios de parada
        if (iteracion > 1 and error_relativo < tol) or fm == 0:
            break

        if f(a) * fm < 0:
            b = m
        else:
            a = m
        m_anterior = m

    # Retornamos la raíz, el total de iters y la DATA completa
    return m, iteracion, iteraciones_data