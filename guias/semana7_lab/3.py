import random

def ordenamiento_seleccion(datos):
    """Ordena in-place (Efecto Secundario: modifica la lista original)."""
    for i in range(len(datos) - 1):
        pos_min = i
        for j in range(i + 1, len(datos)):
            if datos[j] < datos[pos_min]:
                pos_min = j
        datos[i], datos[pos_min] = datos[pos_min], datos[i]

def ordenar_sin_modificar(datos):
    """Ordena una copia pura (Sin efecto secundario)."""
    copia = datos[:]
    for i in range(len(copia) - 1):
        pos_min = i
        for j in range(i + 1, len(copia)):
            if copia[j] < copia[pos_min]:
                pos_min = j
        copia[i], copia[pos_min] = copia[pos_min], copia[i]
    return copia

# --- Pruebas Empíricas ---
random.seed(42)
lista_base = [random.randint(1, 50) for _ in range(10)]

# (b) In-place (Mismo ID, datos mutados)
copia_para_inplace = lista_base[:]
print(f"--- In-place (ordenamiento_seleccion) ---")
print(f"Antes:   id={id(copia_para_inplace)} | {copia_para_inplace}")
ordenamiento_seleccion(copia_para_inplace)
print(f"Después: id={id(copia_para_inplace)} | {copia_para_inplace}\n")

# (c) Pura (Distinto ID, original intacta)
print(f"--- Función Pura (ordenar_sin_modificar) ---")
print(f"Original: id={id(lista_base)} | {lista_base}")
lista_nueva = ordenar_sin_modificar(lista_base)
print(f"Nueva:    id={id(lista_nueva)} | {lista_nueva}")
print(f"¿Original mutó?: {lista_base != lista_base}\n") # Da False, sigue igual

"""
(e) Tabla Comparativa: Python Custom vs Built-in

| Tipo de Función       | Custom (nuestra)        | Built-in (Python) | ¿Efecto Secundario? | ¿Mismo id()? |
|-----------------------|-------------------------|-------------------|---------------------|--------------|
| Modifica in-place     | ordenamiento_seleccion()| lista.sort()      | SÍ (Muta original)  | SÍ           |
| Retorna copia nueva   | ordenar_sin_modificar() | sorted(lista)     | NO (Función pura)   | NO           |

Conclusión: `.sort()` ahorra memoria pero destruye el orden original. 
`sorted()` protege la variable original delegando el trabajo a una nueva posición en el Heap.
"""