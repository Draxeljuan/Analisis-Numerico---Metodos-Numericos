# conversor.py
from sympy import SympifyError, sympify, symbols, lambdify

class ConvertirAFuncion:
    def __init__(self):
        # No hay necesidad de inicializar nada en este apartado
        pass

    def preparar_funciones(self, funcion_str, incognita="x"):
        """
        Recibe la cadena de la función y la variable, 
        y retorna la función ejecutable y la simbólica.
        """
        try:
            # Limpieza básica para compatibilidad de sintaxis
            entrada_limpia = funcion_str.replace("^", "**")

            # Definimos el símbolo dinámicamente
            x = symbols(incognita)

            # Expresión simbólica para derivadas (Newton-Raphson)
            expresion = sympify(entrada_limpia)

            # Función ejecutable optimizada con NumPy
            funcion_ejecutable = lambdify(
                incognita, expresion, modules=["numpy", "math"]
            )

            return funcion_ejecutable, expresion

        except (SympifyError, SyntaxError, TypeError) as e:
            # Lanzamos una excepción que el API pueda capturar
            raise ValueError(f"La función ingresada no es válida: {e}")