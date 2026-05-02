def falsa_posicion(f, a, b, tol, max_it=100):
    
    # Validar teorema de Bolzano
    if f(a) * f(b) >= 0:
        return None, "Error de signo"
    
    # Evaluar los puntos iniciales
    f_a = f(a)
    f_b = f(b)
    
    # Inicializamos las iteraciones
    iteracion = 0
    r_anterior = 0
    
    # Imprimir encabezado de la tabla
    print("\n" + "-" * 105)
    print(
        f"{'Iter':<5} | {'a':<12} | {'b':<12} | {'r':<12} | {'f(r)':<15} | {'Err Relat':<12}"
    )
    print("-" * 105)
    
    while iteracion < max_it:
        
        iteracion += 1
        
        # Calculamos la raiz en esta iteracion
        r = (a * f(b) - b * f(a)) / (f(b) - f(a))
        
        # Evaluamos la raiz en la funcion
        f_r = f(r)
        
        error_relativo = abs((r - r_anterior) / r) if r != 0 else 0
        
        # En la primera iteración el error relativo no es muy confiable (se deja ---),
        # pero a partir de la segunda se toma normalmente
        error_str = f"{error_relativo:<12.6f}" if iteracion > 1 else f"{'---':<12}"

        print(
            f"{iteracion:<5} | {a:<12.6f} | {b:<12.6f} | {r:<12.6f} | {f_r:<15.6e} | {error_str}"
        )
        
        # Criterio de parada (excepto en la primera iteración)
        if iteracion > 1 and error_relativo < tol:
            break
        
        # Si f(a) y f(r) tienen signos opuestos, la raíz está entre a y m, entonces actualizamos b = m
        # De lo contrario, la raíz está entre m y b, entonces actualizamos a = m
        if f(a) * f_r < 0:
            b = r
        else:
            a = r
            
        # Actualizamos el valor de r_anterior
        
        r_anterior = r
        
    print("-" * 105)
    return r, iteracion
         
        