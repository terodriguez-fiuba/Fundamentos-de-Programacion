import copy

print("=== EXPERIMENTO 1: Inmutables ===")
# (a) Enteros
x = 10
y = x
print(f"Predicción (x is y): True. Realidad: {x is y}")
y = y + 1
print(f"Predicción post-suma (x is y): False. Realidad: {x is y}")
print(f"¿Cambió x?: {x} (No cambió, los enteros son inmutables)\n")

# (b) Cadenas
s1 = "hola"
s2 = s1
s2 = s2 + " mundo"
print(f"Original: {s1} | Modificada: {s2}. Las cadenas también son inmutables.\n")

# (c) Caché de CPython
a, b = 256, 256
print(f"a (256) is b (256): {a is b} -> True por la caché de CPython [-5, 256]")
p, q = 257, 257
print(f"p (257) is q (257): {p is q} -> False, se instancian en direcciones distintas.\n")


print("=== EXPERIMENTO 2: Mutables ===")
# (d) Aliasing clásico
lista1 = [1, 2, 3]
lista2 = lista1
lista2.append(4)
print(f"Predicción: lista1 cambió. Realidad: lista1 = {lista1}")
print(f"Verificación id: lista1({id(lista1)}) == lista2({id(lista2)})\n")

# (e) Igualdad vs Identidad
lista3 = [1, 2, 3]
lista4 = [1, 2, 3]
print(f"lista3 == lista4: {lista3 == lista4} (Tienen el mismo valor adentro)")
print(f"lista3 is lista4: {lista3 is lista4} (Son objetos distintos en el Heap)\n")

# (f) Tuplas (Mutabilidad bloqueada)
tupla1 = (10, 20)
tupla2 = tupla1
try:
    tupla2[0] = 99
except TypeError as e:
    print(f"Error esperado en tupla: {e}\n")


print("=== EXPERIMENTO 3: Aliasing en listas anidadas ===")
# (g) Copia superficial (El peligro)
matriz = [[1, 2], [3, 4]]
copia_sup = matriz[:]
copia_sup[0][0] = 99
print(f"Matriz original tras copia superficial: {matriz} -> ¡Se arruinó el 1!\n")

# (h) Copia profunda (La solución)
matriz_nueva = [[1, 2], [3, 4]]
copia_prof = copy.deepcopy(matriz_nueva)
copia_prof[0][0] = 99
print(f"Matriz original tras copia profunda: {matriz_nueva} -> ¡Quedó intacta!")