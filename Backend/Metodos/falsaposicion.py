def falsa_posicion(f, a, b, tol, max_it=100):
    
    # Validar teorema de Bolzano
    if f(a) * f(b) >= 0:
        return None, 0, []
    
    # Evaluar los puntos iniciales
    f_a = f(a)
    f_b = f(b)
    
    # Inicializamos las iteraciones
    iteracion = 0
    r_anterior = 0
    
    # Lista para capturar los datos de la tabla
    iteraciones_data = []
    
    
    while iteracion < max_it:
        
        iteracion += 1
        
        # Calculamos la raiz en esta iteracion
        r = (a * f(b) - b * f(a)) / (f(b) - f(a))
        
        # Evaluamos la raiz en la funcion
        f_r = f(r)
        
        error_relativo = abs((r - r_anterior) / r) if r != 0 else 0
        
        
        fila = {
            "iteracion": iteracion,
            "a": float(a),
            "b": float(b),
            "m": float(r),
            "fm": float(f_r),
            "error": float(error_relativo) if iteracion > 1 else None
        }
        iteraciones_data.append(fila)
        
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
        
    # Retornamos raiz, total de iteraciones y Data de las iteraciones
    return r, iteracion, iteraciones_data
         
        