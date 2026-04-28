'''Consignas:
(a) Implementar binario_a_jsonl(ruta_binaria, ruta_jsonl) que abra el archivo binario, 
recorra todos los registros activos y escriba cada uno como una línea JSON en el archivo de 
salida con el formato {"id": ..., "nombre": "...", "telefono": "...", "email": 
"..."}. Las cadenas se desempaquetan con .rstrip(b'\x00').decode('utf-8') para 
remover el padding.
(b) Implementar jsonl_a_binario(ruta_jsonl, ruta_binaria) que lea el archivo JSON Lines 
línea por línea (sin cargar todo a memoria) y produzca un archivo binario equivalente. Las 
cadenas más largas que el campo se truncan; las más cortas se rellenan automáticamente al 
empaquetar.
(c) Implementar procesar_streaming(ruta_jsonl, dominio): cuenta cuántos contactos del 
archivo JSON Lines tienen su email en el dominio dado, recorriendo línea por línea sin cargar el 
Fundamentos de Programación — Algoritmos y Programación I
Página 16
archivo. Probar con un archivo grande para confirmar que el uso de memoria es constante 
(independiente del tamaño del archivo).
(d) Comparación de tamaños: para una agenda de 10 000 contactos, comparar el tamaño en 
disco de las tres representaciones: binario con struct (920 KB), JSON Lines (≈ 1.2-1.5 MB), 
JSON plano con indentación de 2 espacios (≈ 2 MB o más). Discutir el trade-off entre tamaño y 
portabilidad.
(e) Reflexión integradora: ¿en qué momento del ciclo de vida de los datos conviene cada 
formato? Sugerencia: pensar en los siguientes escenarios y proponer el formato apropiado 
para cada uno: persistencia operativa de la aplicación, exportación para consumo por 
sistemas externos, backup archivado, intercambio con un programa Java que también 
consume la agenda, log de auditoría que se escribe constantemente y rara vez se lee.'''

