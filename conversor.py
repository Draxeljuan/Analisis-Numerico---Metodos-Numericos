# conversor.py
from sympy import SympifyError, sympify, symbols, lambdify


class ConvertirAFuncion:
    def __init__(self):
        self.entrada_str = ""
        self.incognita = "x"  # Valor por defecto
        self.expresion = None

    def definir_incognita(self):
        # Le permitimos al usuario definir la incógnita (por ejemplo, x, y, z)
        valor = input("Ingrese la incógnita (ej. x): ").strip()
        self.incognita = valor if valor else "x"

    def solicitar_entrada(self):
        # Solicitamos la función al usuario
        self.entrada_str = input("Ingresa la función f(x) o transformada g(x): ")

    def preparar_funciones(self):

        try:
            # Limpiamos la entrada para que SymPy entienda ^ como potencia
            entrada_limpia = self.entrada_str.replace("^", "**")

            # Creamos la expresión simbólica (la que sirve para derivar)
            self.expresion = sympify(entrada_limpia)

            # Creamos la función ejecutable (la que sirve para evaluar números, usamos numpy o math)
            funcion_ejecutable = lambdify(
                self.incognita, self.expresion, modules=["numpy", "math"]
            )

            # Retornamos ambas
            return funcion_ejecutable, self.expresion

        except (SympifyError, SyntaxError, TypeError) as e:
            print(f"\n[!] Error de Sintaxis. La Funcion no es Valida: {e}")
            return None, None
