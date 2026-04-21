import sys

def cuenta_regresiva(n):
    if n < 0:
        return
    cuenta_regresiva(n - 1) # Lo hacemos silencioso para no inundar la terminal

def cuenta_regresiva_iter(n):
    """Versión iterativa: usa bucle en vez de la pila de ejecución."""
    while n >= 0:
        n -= 1

print("--- (b) y (c) Provocando el error ---")
limite_actual = sys.getrecursionlimit()
print(f"Límete de recursión por defecto de CPython: {limite_actual}")

try:
    # Si el límite es 1000, pedirle 1500 va a romper la pila
    cuenta_regresiva(limite_actual + 500)
except RecursionError as e:
    print(f"¡Atrapamos el error!: {e}")

print("\n--- (d) Jugando con los límites del SO ---")
sys.setrecursionlimit(50) # Achicamos el límite a propósito
print(f"Nuevo límite: {sys.getrecursionlimit()}")
try:
    cuenta_regresiva(60)
except RecursionError:
    print("Falló en 60 porque achicamos el límite.")
finally:
    sys.setrecursionlimit(limite_actual) # Siempre restaurar el límite original

print("\n--- (e) La solución iterativa es inmune al límite de pila ---")
cuenta_regresiva_iter(100000)
print("Versión iterativa terminó con 100000 sin ningún problema.")