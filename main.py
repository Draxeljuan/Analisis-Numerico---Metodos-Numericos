import os
import numpy as np
from conversor import ConvertirAFuncion
from Metodos.biseccion import biseccion
from Metodos.newtonr import newton_raphson
from Metodos.secante import secante
from Metodos.puntofijo import punto_fijo
from Metodos.falsaposicion import falsa_posicion
from Metodos.jacobi import jacobi
from Metodos.gauss_seidel import gauss_seidel


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


def menu_sistemas_lineales():
    print("\n--- CONFIGURACIÓN DE SISTEMA LINEAL  ---")
    try:
        n = int(input("Ingrese el número de ecuaciones (n): "))

        print(f"\nIngreso de la Matriz de Coeficientes A ({n}x{n}):")
        A = []
        for i in range(n):
            while True:
                fila_str = input(
                    f"Fila {i+1} (ingresa los {n} valores separados por espacio): "
                )
                fila = [float(x) for x in fila_str.split()]
                if len(fila) == n:
                    A.append(fila)
                    break
                print(f"[!] Error: Debes ingresar exactamente {n} valores.")

        print(f"\nIngreso del Vector de Términos Independientes b ({n} valores):")
        while True:
            b_str = input(f"Ingrese los {n} valores de b separados por espacio: ")
            b = [float(x) for x in b_str.split()]
            if len(b) == n:
                break
            print(f"[!] Error: Debes ingresar exactamente {n} valores.")

        tol = float(input("\nIngrese la tolerancia (ej. 0.001): "))
        max_iter = int(input("Ingrese el número máximo de iteraciones: "))

        # Selección de Método
        print("\n¿Qué método desea aplicar?")
        print("1. Jacobi")
        print("2. Gauss-Seidel")
        metodo = input("Seleccione: ")

        # Ejecución del método
        A_np = np.array(A)
        b_np = np.array(b)

        if metodo == "1":
            print("\n Ejecutando Jacobi...")
            resultado, it = jacobi(A_np, b_np, tol, max_iter=max_iter)
        elif metodo == "2":
            print("\n Ejecutando Gauss-Seidel...")
            resultado, it = gauss_seidel(A_np, b_np, tol, max_iter=max_iter)
        else:
            print("[!] Opción inválida.")
            return

        print(f"\n Convergencia alcanzada en {it} iteraciones.")
        print(f"Solución: {resultado}")

    except ValueError:
        print("\n[!] ERROR: Datos numéricos inválidos.")


def menu_principal():
    while True:
        limpiar_pantalla()
        print("=========================================")
        print("       SISTEMA DE MÉTODOS NUMÉRICOS      ")
        print("=========================================")
        print("\n1. Métodos para Ecuaciones No Lineales ")
        print("2. Métodos para Sistemas Lineales")
        print("s. Salir")

        opcion = input("\nSelecciona una opción: ").lower()

        if opcion == "1":
            ejecutar_no_lineales()
        elif opcion == "2":
            ejecutar_lineales()
        elif opcion == "s":
            print("\nSaliendo del programa")
            break
        else:
            print("\n[!] Opción no válida. Por favor, selecciona 1, 2 o s.")
            input("Presiona Enter para intentar de nuevo...")


def ejecutar_no_lineales():
    # Se limpia la pantalla (CMD) al iniciar el programa
    limpiar_pantalla()
    print("=== MÉTODOS NUMÉRICOS ===")

    while True:

        try:

            # Objeto para convertir la entrada del usuario en una funcion valida
            # para los métodos numéricos
            conversor = ConvertirAFuncion()
            conversor.definir_incognita()
            mostrar_guia_sintaxis()
            conversor.solicitar_entrada()
            f_ejecutable, f_simbolica = conversor.preparar_funciones()

            tol_input = input("Ingrese la tolerancia (ej. 0.0001): ")
            tol = float(tol_input)
            max_it = input("Máximo de iteraciones (Enter para 100): ")
            max_it = int(max_it) if max_it.strip() else 100

            print(
                "1. Bisección\n2. Newton-Raphson\n3. Secante\n4. Punto Fijo\n5. Falsa Posicion"
            )
            opcion = input("Seleccione método: ")

            if opcion == "1":
                try:
                    # f_ejecutable, _ = conversor.preparar_funciones()
                    # Ingresar intervalo
                    print("\n--- Configuración del Intervalo ---")
                    a = float(input("Ingrese el límite inferior (a): "))
                    b = float(input("Ingrese el límite superior (b): "))

                    # Llamada al método
                    resultado, iteraciones = biseccion(f_ejecutable, a, b, tol, max_it)

                    # Mostrar resultados
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
                    # Ingresar aproximación inicial y tolerancia
                    x_inicial = float(input("Ingrese la aproximación inicial (x0): "))
                    # Llamada al método
                    resultado, iteraciones = newton_raphson(
                        f_ejecutable,
                        f_simbolica,
                        x_inicial,
                        tol,
                        conversor.incognita,
                        max_it,
                    )
                    # Mostrar resultados
                    print("\n" + "=" * 30)

                    print(f"Raíz aproximada encontrada: {resultado}")
                    print(f"Iteraciones realizadas: {iteraciones}")

                    print("=" * 30)

                except Exception as e:
                    print(f"\n[!] Ocurrió un error inesperado: {e}")

            elif opcion == "3":
                try:
                    # Ingresa intervalo
                    x0 = float(input("Ingrese el límite inferior (X0): "))
                    x1 = float(input("Ingrese el límite superior (X1): "))

                    # Llamada al metodo
                    resultado, iteraciones = secante(f_ejecutable, x0, x1, tol, max_it)

                    # Mostrar resultados
                    print("\n" + "=" * 30)

                    print(f"Raíz aproximada encontrada: {resultado}")
                    print(f"Iteraciones realizadas: {iteraciones}")

                    print("=" * 30)

                except Exception as e:
                    print(f"\n[!] Ocurrió un error inesperado: {e}")

            elif opcion == "4":
                try:
                    # Ingresa punto o aproximacion inicial
                    x_inicial = float(input("Ingrese la aproximación inicial (x0): "))

                    # Llamamos al metodo
                    resultado, iteraciones = punto_fijo(
                        f_ejecutable, x_inicial, tol, max_it
                    )

                    # Mostrar resultados
                    print("\n" + "=" * 30)

                    print(f"Raíz aproximada encontrada: {resultado}")
                    print(f"Iteraciones realizadas: {iteraciones}")

                    print("=" * 30)

                except Exception as e:
                    print(f"\n[!] Ocurrió un error inesperado: {e}")

            elif opcion == "5":
                try:
                    # Ingresar intervalo
                    print("\n--- Configuración del Intervalo ---")
                    a = float(input("Ingrese el límite inferior (a): "))
                    b = float(input("Ingrese el límite superior (b): "))

                    # Llamar al metodo
                    resultado, iteraciones = falsa_posicion(
                        f_ejecutable, a, b, tol, max_it
                    )

                    # Mostrar resultados
                    if resultado is not None:
                        print("\n" + "=" * 30)

                        print(f"Raíz aproximada encontrada: {resultado}")
                        print(f"Iteraciones realizadas: {iteraciones}")

                        print("=" * 30)
                    else:
                        print(
                            "\n[!] Error: El intervalo no es válido para falsa posicion (f(a)*f(b) >= 0)."
                        )

                except Exception as e:
                    print(f"\n[!] Ocurrió un error inesperado: {e}")

            else:
                print("Entrada Invalida")

        except ValueError:
            print("\n" + "!" * 50)
            print("Por favor, ingresa solo valores numéricos donde se requiera.")
            print("!" * 50 + "\n")
            input("Presiona Enter para intentar de nuevo...")

        except KeyboardInterrupt:
            print("\n\nSaliendo del programa de forma segura...")
            break

        except Exception as e:
            # Este atrapa cualquier otro error inesperado para que no se cierre la consola
            print("\n" + "!" * 50)
            print(f" OCURRIÓ UN ERROR INESPERADO: {e}")
            print("!" * 50 + "\n")
            input("Presiona Enter para volver al menú principal...")


def ejecutar_lineales():

    while True:
        try:
            limpiar_pantalla()
            print("=== MÉTODOS PARA SISTEMAS LINEALES ===")

            menu_sistemas_lineales()

            if input("\n¿Deseas resolver otro sistema lineal? (s/n): ").lower() != "s":
                break
        except Exception as e:
            print(f"[!] Error: {e}")
            input("Presiona Enter para reintentar...")


if __name__ == "__main__":
    menu_principal()
