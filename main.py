import os
from conversor import ConvertirAFuncion
from Metodos.Biseccion import biseccion
from Metodos.NewtonR import newton_raphson


def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


def mostrar_guia_sintaxis():
    print("\n" + "=" * 60)
    print(f"{'CONCEPTO':<25} | {'SINTAXIS PYTHON/SYMPY':<25}")
    print("-" * 60)
    guias = [
        ("Potencia (x²)", "x**2 o x^2"),
        ("Raíz Cuadrada (√x)", "sqrt(x)"),
        ("Exponencial (e^x)", "exp(x)"),
        ("Logaritmo Natural (ln)", "log(x)"),
        ("Seno", "sin(x)"),
        ("Coseno", "cos(x)"),
        ("Tangente", "tan(x)"),
        ("Pi (π)", "pi"),
        ("Número e", "exp(x)"),
        ("Multiplicación", "x*y"),
        ("División", "x/y"),
    ]

    for concepto, sintaxis in guias:
        print(f"{concepto:<25} | {sintaxis:<25}")

    print("-" * 60)
    print("Ejemplo de función compleja: exp(-x) - log(x) + sin(x**2)")
    print("=" * 60 + "\n")


def ejecutar():
    # Se limpia la pantalla (CMD) al iniciar el programa
    limpiar_pantalla()
    print("=== MÉTODOS NUMÉRICOS ===")

    # Objeto para convertir la entrada del usuario en una funcion valida
    # para los métodos numéricos
    conversor = ConvertirAFuncion()
    conversor.definir_incognita()
    mostrar_guia_sintaxis()
    conversor.solicitar_entrada()
    f_ejecutable, f_simbolica = conversor.preparar_funciones()

    tol = float(input("Ingrese la tolerancia (ej. 0.0001): "))
    max_it = input("Máximo de iteraciones (Enter para 100): ")
    max_it = int(max_it) if max_it.strip() else 100

    print("1. Bisección\n2. Newton-Raphson")
    opcion = input("Seleccione método: ")

    if opcion == "1":
        try:
            f_ejecutable, _ = conversor.preparar_funciones()
            # 1. Ingresar intervalo y tolerancia
            print("\n--- Configuración del Intervalo ---")
            a = float(input("Ingrese el límite inferior (a): "))
            b = float(input("Ingrese el límite superior (b): "))

            # 2. Llamada al método
            resultado, iteraciones = biseccion(f_ejecutable, a, b, tol, max_it)

            # 3. Mostrar resultados
            if resultado is not None:
                print("\n" + "=" * 30)

                print(f"Raíz aproximada encontrada: {resultado}")
                print(f"Iteraciones realizadas: {iteraciones}")

                print("=" * 30)
            else:
                print(
                    "\n[!] Error: El intervalo no es válido para bisección (f(a)*f(b) >= 0)."
                )

        except Exception as e:
            print(f"\n[!] Ocurrió un error inesperado: {e}")

    elif opcion == "2":
        try:
            # 1. Ingresar aproximación inicial y tolerancia
            x_inicial = float(input("Ingrese la aproximación inicial (x0): "))
            # 2. Llamada al método
            resultado, iteraciones = newton_raphson(
                f_ejecutable, f_simbolica, x_inicial, tol, max_it
            )
            # 3. Mostrar resultados
            print("\n" + "=" * 30)

            print(f"Raíz aproximada encontrada: {resultado}")
            print(f"Iteraciones realizadas: {iteraciones}")

            print("=" * 30)

        except Exception as e:
            print(f"\n[!] Ocurrió un error inesperado: {e}")


if __name__ == "__main__":
    ejecutar()
