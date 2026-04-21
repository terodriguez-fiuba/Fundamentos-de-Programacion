import sys

def medir_tamanio(objeto, nombre):
    print(f"{nombre:<15} | Tipo: {type(objeto).__name__:<7} | Tamaño: {sys.getsizeof(objeto)} bytes")

print("--- (a) Escalabilidad de Tipos Simples ---")
medir_tamanio(42, "int pequeño")
medir_tamanio(2**100, "int grande")  # Python maneja ints arbitrariamente grandes, ocupan más bytes.
medir_tamanio(3.14, "float")
medir_tamanio(True, "bool")
medir_tamanio("hola", "str corta")
medir_tamanio("a" * 1000, "str larga")

print("\n--- (b) Overhead de Listas ---")
print(f"{'N Elementos':<12} | {'Lista (Contenedor)':<20} | {'Total (Contenedor + Datos)':<25}")
for n in [0, 1, 10, 100, 1000]:
    lista = list(range(n))
    tam_lista = sys.getsizeof(lista)
    # Sumamos lo que pesa la lista (referencias) + lo que pesa cada entero en memoria
    tam_total = tam_lista + sum(sys.getsizeof(e) for e in lista)
    print(f"{n:<12} | {tam_lista:<20} | {tam_total:<25}")

print("\n--- (c) Tupla vs Lista ---")
lista_100 = list(range(100))
tupla_100 = tuple(range(100))
medir_tamanio(lista_100, "Lista 100 obj")
medir_tamanio(tupla_100, "Tupla 100 obj")
# Explicación: La tupla ahorra bytes porque al ser inmutable, el Sistema Operativo 
# sabe exactamente cuánto va a medir para siempre. La lista necesita reservar un 
# "buffer" extra oculto por si le metés más elementos en el futuro.

print("\n--- (d) El Truco de la Sobreasignación (Over-allocation) ---")
lista_concat = [1, 2, 3] + [4]
lista_append = [1, 2, 3]
lista_append.append(4)

medir_tamanio(lista_concat, "Concatenada")
medir_tamanio(lista_append, "Con Append")
# Explicación: Al hacer concatenación (+), Python crea un array del tamaño exacto necesario (4).
# Al hacer .append(), Python detecta que la lista está creciendo dinámicamente y pide 
# memoria al SO "por las dudas" (ej. para 8 elementos), así el próximo append es instantáneo (O(1)).