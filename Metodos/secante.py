def secante(f, x0, x1, tol, max_iter=100):
    # Evaluamos los puntos iniciales
    f_x0 = f(x0)
    f_x1 = f(x1)
    
    iteracion = 0 
    # Inicialmente r va a ser x1 para el primer error
    
    print("\n" + "-" * 115)
    print(f"{'Iter':<5} | {'x0':<12} | {'x1':<12} | {'x2 (r)':<15} | {'f(r)':<15} | {'Err Relat':<12}")
    print("-" * 115)
    
    while iteracion < max_iter:
        iteracion += 1
        
        # Evitar división por cero si f(x1) == f(x0)
        denominador = f_x1 - f_x0
        if denominador == 0:
            print("[!] Error: División por cero en la Secante.")
            return x1, iteracion

        # Se evalua la nueva raiz en esta iteracion
        r = x1 - (f_x1 * (x1 - x0) / denominador)
        f_r = f(r)
        
        # Se calcula el error relativo con los nuevos datos
        error_relativo = abs((r - x1) / r) if r != 0 else 0
        error_str = f"{error_relativo:<12.6f}" if iteracion > 1 else f"{'---':<12}"
        
        print(f"{iteracion:<5} | {x0:<12.6f} | {x1:<12.6f} | {r:<15.6e} | {f_r:<15.6e} | {error_str}")
        
        # Se evalua, si la iteracion es diferente a la primera
        # y el error relativo es menor al digitado por el usuario
        # termina la ejecucion
        if iteracion > 1 and error_relativo < tol:
            break 
        
        # ACTUALIZACIÓN DE VALORES:
        
        x0 = x1
        f_x0 = f_x1
        x1 = r
        f_x1 = f_r
    
    print("-" * 115)
    return x1, iteracion
