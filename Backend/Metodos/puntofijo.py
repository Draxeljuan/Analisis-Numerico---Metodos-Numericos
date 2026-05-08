def punto_fijo(g_func, x0, tol, max_iter=100):
    
    # Iteracion actual inicialmente
    # sera el punto inicial dado por el usuario
    x_actual = x0
    iteracion = 0
    
    iteraciones_data = []
    
    
    while iteracion < max_iter:
        iteracion += 1
        # Se evalua la transformada en la raiz actual
        x_siguiente = g_func(x_actual)
        
        # Error relativo: |(x_sig - x_act) / x_sig|
        error_relativo = abs((x_siguiente - x_actual) / x_siguiente) if x_siguiente != 0 else 0
        
        print(f"{iteracion:<5} | {x_actual:<15.8f} | {x_siguiente:<15.8f} | {error_relativo:<15.8f}")
        
        fila = {
            "iteracion": iteracion,
            "x_n": float(x_actual),
            "g(x_n)": float(x_siguiente),
            "error": float(error_relativo)
        }
        
        iteraciones_data.append(fila)
        
        # Si el error relativo es menor al error permitido
        # termina el codigo
        if error_relativo < tol:
            break
        
        # Se actualiza la raiz actual con la hallada
        x_actual = x_siguiente
        
    return x_actual, iteracion, iteraciones_data