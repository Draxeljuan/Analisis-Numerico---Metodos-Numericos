def punto_fijo(g_func, x0, tol, max_iter=100):
    
    # Iteracion actual inicialmente
    # sera el punto inicial dado por el usuario
    x_actual = x0
    iteracion = 0
    
    print("\n" + "-" * 80)
    print(f"{'Iter':<5} | {'x_n':<15} | {'g(x_n)':<15} | {'Err Relat':<15}")
    print("-" * 80)
    
    while iteracion < max_iter:
        iteracion += 1
        # Se evalua la transformada en la raiz actual
        x_siguiente = g_func(x_actual)
        
        # Error relativo: |(x_sig - x_act) / x_sig|
        error_relativo = abs((x_siguiente - x_actual) / x_siguiente) if x_siguiente != 0 else 0
        
        print(f"{iteracion:<5} | {x_actual:<15.8f} | {x_siguiente:<15.8f} | {error_relativo:<15.8f}")
        
        # Si el error relativo es menor al error permitido
        # termina el codigo
        if error_relativo < tol:
            break
        
        # Se actualiza la raiz actual con la hallada
        x_actual = x_siguiente
        
    print("-" * 80)
    return x_actual, iteracion