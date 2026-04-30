# Arquitectura de Capas para una Agenda Real

El ciclo de vida de los datos en una aplicación moderna rara vez utiliza un solo formato. Para nuestro sistema de agenda, proponemos una arquitectura dividida en cuatro capas, aprovechando los beneficios de `struct` y `JSON Lines`:

### 1. Capa Operativa
*   **Formato elegido:** Binario con registros de longitud fija (`struct`).
*   **Justificación:** Durante el uso normal de la aplicación, necesitamos realizar búsquedas por ID y modificaciones instantáneas. Al usar este formato, podemos localizar cualquier registro en $O(1)$ desplazando el puntero del archivo (`seek`) e interactuando directamente con el sistema de bloques del SO.

### 2. Capa de Exportación
*   **Formato elegido:** JSON Lines.
*   **Justificación:** Semanalmente, el equipo de Marketing necesita procesar los contactos. Mediante la función `binario_a_jsonl()`, generamos un extracto de los datos en formato estándar y portable. Esto independiza al equipo de Marketing de nuestra implementación interna en Python.

### 3. Capa de Respaldo (Backup)
*   **Formato elegido:** JSON Lines (comprimido en .gz).
*   **Justificación:** Los backups se envían a un almacenamiento frío (ej. Amazon S3). No guardamos copias binarias porque si el esquema (el tamaño del `struct`) evoluciona en futuras versiones del sistema, los backups binarios viejos quedarían ilegibles sin migraciones complejas. Usamos JSON Lines para garantizar legibilidad histórica, y lo comprimimos para mitigar el *trade-off* del tamaño.

### 4. Capa de Auditoría
*   **Formato elegido:** JSON Lines (Log Append-Only).
*   **Justificación:** Cada vez que se elimina o modifica un contacto, se escribe una nueva línea JSON en un archivo de log (`eventos.jsonl`). Se elige este formato porque es tolerante a interrupciones: si el servidor se apaga repentinamente en medio de una escritura, la estructura del documento no se corrompe (a diferencia de un JSON plano con llaves de cierre `]`). Si fuera necesario hacer análisis masivos, se puede usar `procesar_streaming()` para iterarlo línea por línea.