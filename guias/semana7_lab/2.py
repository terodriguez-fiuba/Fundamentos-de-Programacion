# --- (a) EXPLICACIÓN TEÓRICA ---
"""
¿Por qué `agregar_elemento` modifica la lista original y `intentar_reemplazar` no?

1. `agregar_elemento` usa `.append()`. Este método viaja a la dirección de memoria 
   del parámetro y altera el objeto físicamente (mutación in-place). 
   El alias "original" de afuera ve el cambio porque mira al mismo objeto.
   
2. `intentar_reemplazar` hace `lista = nueva`. Esto NO modifica el objeto. 
   Simplemente toma la etiqueta local (el parámetro 'lista') y la hace apuntar 
   a una dirección de memoria completamente nueva. La lista 'original' de afuera 
   sigue apuntando a los datos viejos, intacta.
"""

# --- (b) Función Pura (Sin Efecto Secundario) ---
def agregar_elemento_puro(lista, elemento):
    """
    Agrega un elemento al final de una nueva lista.
    Precondición: lista es una lista, elemento es cualquier valor.
    Postcondición: retorna una nueva lista con el elemento al final.
    Efecto secundario: NINGUNO (la lista original no se modifica).
    """
    # Sumar listas crea un objeto completamente nuevo en memoria
    return lista + [elemento]

# --- (c) Función Impura (Con Efecto Secundario) ---
def extender_si_corta(datos, minimo, valor_relleno):
    """
    Extiende la lista hasta alcanzar la longitud mínima si es necesario.
    Precondición: datos es una lista, minimo es un int, valor_relleno cualquier tipo.
    Postcondición: la lista tendrá al menos 'minimo' elementos.
    Efecto secundario: SÍ. Modifica la lista original in-place mediante append.
    """
    # Usamos while porque no sabemos cuántas veces iterar (bucle indeterminado)
    while len(datos) < minimo:
        datos.append(valor_relleno)


# --- PRUEBAS ---
mi_lista = [10, 20]
print(f"Lista base: {mi_lista}")

pura = agregar_elemento_puro(mi_lista, 30)
print(f"Tras agregar puro: Base={mi_lista} | Nueva={pura}")

extender_si_corta(mi_lista, 5, 0)
print(f"Tras extender (in-place): Base={mi_lista}")