def secante(f, x0, x1, tol, max_iter=100):
    # Evaluamos los puntos iniciales
    f_x0 = f(x0)
    f_x1 = f(x1)
    
    iteracion = 0 
    
    iteraciones_data = []
    
    
    while iteracion < max_iter:
        iteracion += 1
        
        # Evitar división por cero si f(x1) == f(x0)
        denominador = f_x1 - f_x0
        if denominador == 0:
            print("[!] Error: División por cero en la Secante.")
            return x1, iteracion, iteraciones_data

        # Se evalua la nueva raiz en esta iteracion
        r = x1 - (f_x1 * (x1 - x0) / denominador)
        f_r = f(r)
        
        # Se calcula el error relativo con los nuevos datos
        error_relativo = abs((r - x1) / r) if r != 0 else 0
        
        fila = {
            "iteracion": iteracion,
            "x0": float(x0),
            "x1": float(x1),
            "x2 (r)": float(r),
            "f(r)": float(f_r),
            "error": float(error_relativo)
        }
        iteraciones_data.append(fila)
        
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
    
   
    return x1, iteracion, iteraciones_data
