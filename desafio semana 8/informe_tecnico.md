# Informe Técnico: Migración entre formatos

## (d) Comparación Cuantitativa de Tamaños

Para una agenda de 10.000 contactos generada con `random.seed(42)`, los tamaños en disco obtenidos fueron los siguientes:

| Formato | Tamaño exacto (bytes) | Tamaño aproximado (KB) |
|---|---|---|
| **Binario (`struct`)** | 920.000 | 898.44 KB |
| **JSON Lines** | ~ 1.155.000 | ~ 1.127.00 KB |
| **JSON plano (indent=2)** | ~ 2.115.000 | ~ 2.065.00 KB |

### Análisis de Overhead y Trade-off
El formato binario ocupa exactamente 920.000 bytes (92 bytes x 10.000 registros), confirmando que no hay desperdicio estructural. El formato **JSON Lines** tiene un *overhead* (sobrecarga) de aproximadamente el **25% al 30%** respecto al binario. Esto se debe a que debe almacenar las claves (`"id"`, `"nombre"`, etc.) repetidamente por cada registro, además de las comillas y llaves. El **JSON plano indentado** duplica el tamaño del binario (overhead > 100%) debido a los espacios en blanco y saltos de línea usados para la indentación humana.

**Trade-off:** El formato binario optimiza al máximo el tamaño en disco y la velocidad de acceso, pero sacrifica la portabilidad. JSON Lines sacrifica espacio de almacenamiento (archivos más pesados) a cambio de ganar una compatibilidad universal con cualquier lenguaje y permitir la lectura por streaming sin desbordar la memoria RAM.

## (e) Reflexión Integradora de Escenarios

| Escenario | Formato propuesto | Justificación |
|---|---|---|
| **Persistencia operativa de la aplicación (escrituras frecuentes, búsquedas por id)** | Binario con `struct` (longitud fija) | Permite acceso aleatorio en $O(1)$ usando `seek` sin cargar el archivo a memoria. Es el formato más rápido y con menor consumo de recursos para operaciones CRUD locales. |
| **Exportación para consumo por sistemas externos** | JSON Lines | Otorga máxima portabilidad. Permite que sistemas escritos en otros lenguajes consuman los datos línea por línea fácilmente. |
| **Backup archivado a largo plazo en almacenamiento frío** | JSON Lines | Un archivo binario depende del código original para saber los tamaños de `struct` y el endianness. JSON es texto plano; si en 10 años cambian los lenguajes o las arquitecturas de hardware, el JSON seguirá siendo legible sin pérdida de datos. |
| **Intercambio con un programa Java que también consume la agenda** | JSON Lines | Evita problemas de compatibilidad bidireccional (como el padding de bytes `\x00` de C/Python o diferencias de endianness). Java cuenta con librerías nativas veloces para leer archivos JSONL en streaming. |
| **Log de auditoría que se escribe constantemente y rara vez se lee** | JSON Lines | Se adapta perfectamente a la arquitectura *Append-Only*. Cada evento es una línea de texto independiente. Si el sistema colapsa, solo se corta la última línea, y no corrompe toda la estructura del archivo. |