# Resumen Definitivo y Glosario (Semana 7)
## Este es el "machete" conceptual con las definiciones técnicas exactas que necesitás manejar para la materia.

### 1. El Mapa de la Memoria
    
- Segmento Text (Código): Donde viven las instrucciones de tu programa (bytecode). Es de solo lectura.

- Segmento Data: Donde viven las variables globales y la caché del sistema (como los enteros pequeños de Python).

- Heap (Montículo - Memoria Dinámica): Donde Python guarda el "cuerpo" físico de absolutamente todos los objetos que creás (listas, diccionarios, enteros). Crece y se achica mientras el programa corre.

- Stack (Pila de Ejecución): Donde viven los nombres de las variables y las funciones. Crece en dirección contraria al Heap. Si chocan, hay un Stack Overflow.

### 2. Tipos de Datos

- Variables y Referencias
        En C: Una variable es una "caja" que guarda el dato adentro.

        En Python: Una variable es una etiqueta (referencia) que guarda la dirección de memoria de donde está el objeto en el Heap.

- Identidad (id()): Es la "dirección postal" única de un objeto en la memoria física.

### 3. Tipos de Objetos

- Operadores de Comparación
    Igualdad (==): Compara contenido. Pregunta: "¿Las cosas que están adentro valen lo mismo?"

    Identidad (is): Compara direcciones. Pregunta: "¿Son exactamente el mismo objeto en la memoria?" (Compara si tienen el mismo id()).

### 4. Mutabilidad

- Inmutables (int, float, str, tuple): Objetos que nacen sellados. Si les hacés una operación (ej. x = x + 1), Python crea un objeto completamente nuevo y mueve la etiqueta.

- Mutables (list, dict, set): Objetos que se pueden abrir y cambiar por dentro (.append(), .pop(), [0] = x) sin cambiar su dirección de memoria original.

### 5. Aliasing y Copias

- Aliasing: Ocurre cuando dos variables distintas apuntan al mismo id(). Peligroso con objetos mutables porque modificar uno modifica el otro.

- Copia Superficial (lista[:] o .copy()): Crea una lista nueva, pero si adentro hay sublistas, solo copia sus referencias. Es un peligro para matrices.

- Copia Profunda (copy.deepcopy()): Clona absolutamente todo, capa por capa. Crea un universo de datos completamente independiente.

### 6. Paso de Argumentos y Funciones

- Paso por asignación: En Python, cuando pasás una variable a una función, le pasás la referencia (la dirección), no el dato copiado.

- Efecto Secundario (Side Effect): Cuando una función modifica un argumento mutable o interactúa con el mundo exterior (ej. imprime en pantalla o modifica una variable global). Si vas a hacerlo, siempre hay que avisarlo en el docstring de la función.

- Función Pura: Una función que recibe datos, los procesa y retorna una respuesta nueva, dejando el universo exactamente como estaba (sin efectos secundarios).