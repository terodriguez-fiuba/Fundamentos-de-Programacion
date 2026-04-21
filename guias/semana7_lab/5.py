def factorial(n, profundidad=1):
    """
    Retorna n! para n >= 0.
    Caso base: n == 0 -> 1
    """
    sangria = "  " * profundidad
    if n == 0:
        print(f"{sangria}factorial({n}) — profundidad {profundidad} [caso base]")
        return 1
    
    print(f"{sangria}factorial({n}) — profundidad {profundidad}")
    return n * factorial(n - 1, profundidad + 1)

def suma_lista(datos, profundidad=1):
    """
    Retorna la suma de elementos de una lista.
    Caso base: lista vacía -> 0
    """
    sangria = "  " * profundidad
    if not datos:
        print(f"{sangria}suma_lista([]) — profundidad {profundidad} [caso base]")
        return 0
    
    print(f"{sangria}suma_lista({datos}) — profundidad {profundidad}")
    # En Python, datos[1:] crea una lista nueva sin el primer elemento
    return datos[0] + suma_lista(datos[1:], profundidad + 1)

def potencia(base, exponente, profundidad=1):
    """
    Retorna base^exponente para exponente >= 0.
    Caso base: exponente == 0 -> 1
    """
    sangria = "  " * profundidad
    if exponente == 0:
        print(f"{sangria}potencia({base}, {exponente}) — profundidad {profundidad} [caso base]")
        return 1
    
    print(f"{sangria}potencia({base}, {exponente}) — profundidad {profundidad}")
    return base * potencia(base, exponente - 1, profundidad + 1)

print("--- Traza de Factorial ---")
print(f"Resultado final: {factorial(4)}\n")

print("--- Traza de Suma de Lista ---")
print(f"Resultado final: {suma_lista([3, 7, 2, 5])}\n")

print("--- Traza de Potencia ---")
print(f"Resultado final: {potencia(2, 4)}\n")