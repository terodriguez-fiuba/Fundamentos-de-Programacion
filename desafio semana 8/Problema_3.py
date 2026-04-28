import struct
import json
import os
from rich.table import Table
from rich.console import Console


# Constantes del formato (reutilizadas del Problema 2)
FORMATO_REGISTRO = '<i32s16s40s'
TAM_REGISTRO     = struct.calcsize(FORMATO_REGISTRO)  # 92
TAM_NOMBRE       = 32
TAM_TELEFONO     = 16
TAM_EMAIL        = 40

# --- (a) Convertir Binario a JSON Lines ---
def binario_a_jsonl(ruta_binaria, ruta_jsonl):
    """
    Lee un archivo binario secuencialmente y exporta cada registro como 
    una línea JSON (JSON Lines).
    """
    with open(ruta_binaria, 'rb') as f, open(ruta_jsonl, 'w', encoding='utf-8') as f_salida:
        while True:
            datos = f.read(TAM_REGISTRO)
            if not datos or len(datos) < TAM_REGISTRO:
                break  # Fin de archivo o registro incompleto
            
            # Desempaquetado usando la lógica del problema anterior
            id, nombre_b, telefono_b, email_b = struct.unpack(FORMATO_REGISTRO, datos)
            nombre   = nombre_b.rstrip(b'\x00').decode('utf-8')
            telefono = telefono_b.rstrip(b'\x00').decode('utf-8')
            email    = email_b.rstrip(b'\x00').decode('utf-8')
            
            # Armamos el diccionario
            contacto = {
                "id": id,
                "nombre": nombre,
                "telefono": telefono,
                "email": email
            }
            
            # Serializamos a JSON y escribimos una nueva línea
            f_salida.write(json.dumps(contacto) + '\n')


# --- (b) Convertir JSON Lines a Binario ---
def jsonl_a_binario(ruta_jsonl, ruta_binaria):
    """
    Lee un archivo JSON Lines línea por línea y reconstruye el archivo binario.
    Las cadenas que exceden el tamaño se truncan, struct se encarga del relleno (padding).
    """
    with open(ruta_jsonl, 'r', encoding='utf-8') as f, open(ruta_binaria, 'wb') as f_salida:
        for linea in f:
            contacto = json.loads(linea)
            
            id = contacto['id']
            # Codificamos a bytes y truncamos (slicing) a la longitud máxima
            nombre_b   = contacto['nombre'].encode('utf-8')[:TAM_NOMBRE]
            telefono_b = contacto['telefono'].encode('utf-8')[:TAM_TELEFONO]
            email_b    = contacto['email'].encode('utf-8')[:TAM_EMAIL]
            
            # Al usar 's' en struct, automáticamente rellena con \x00 los bytes sobrantes
            datos_bin = struct.pack(FORMATO_REGISTRO, id, nombre_b, telefono_b, email_b)
            f_salida.write(datos_bin)


# --- (c) Procesar en Streaming ---
def procesar_streaming(ruta_jsonl, dominio):
    """
    Cuenta cuántos contactos pertenecen a un dominio de email específico.
    Al procesar línea por línea, la memoria RAM usada es constante e ínfima (O(1)).
    """
    contador = 0
    dominio_buscado = dominio.lower()  # Para comparación case-insensitive
    
    with open(ruta_jsonl, 'r', encoding='utf-8') as f:
        for linea in f:
            contacto = json.loads(linea)
            if contacto.get('email', '').endswith(dominio_buscado):
                contador += 1
                
    return contador


# --- (d) Auxiliar: Crear JSON plano con indentación ---
def binario_a_json_indentado(ruta_binaria, ruta_json):
    """
    Lee el archivo binario y exporta todos los registros como una 
    única lista JSON con indentación de 2 espacios, cumpliendo con la consigna d.
    """
    contactos = []
    with open(ruta_binaria, 'rb') as f:
        while True:
            datos = f.read(TAM_REGISTRO)
            if not datos or len(datos) < TAM_REGISTRO:
                break
            
            id, nombre_b, telefono_b, email_b = struct.unpack(FORMATO_REGISTRO, datos)
            contactos.append({
                "id": id,
                "nombre": nombre_b.rstrip(b'\x00').decode('utf-8'),
                "telefono": telefono_b.rstrip(b'\x00').decode('utf-8'),
                "email": email_b.rstrip(b'\x00').decode('utf-8')
            })
            
    with open(ruta_json, 'w', encoding='utf-8') as f_salida:
        json.dump(contactos, f_salida, indent=2, ensure_ascii=False)

# --- Bloque de Prueba ---
if __name__ == "__main__":
    # Suponiendo que 'agenda.bin' fue generado por Problema_2.py
    if os.path.exists("agenda.bin"):
        binario_a_jsonl("agenda.bin", "agenda.jsonl")
        print("Exportado a JSONL con éxito.")
        
        jsonl_a_binario("agenda.jsonl", "agenda_restaurada.bin")
        print("Restaurado a binario con éxito.")
        
        binario_a_json_indentado("agenda.bin", "agenda_indent.json")
        print("Exportado a JSON plano con indentación con éxito.")
        
        cantidad_example = procesar_streaming("agenda.jsonl", "example.com")
        print(f"Contactos con dominio @example.com: {cantidad_example}")

def mostrar_tabla_comparativa():
    """
    Muestra una tabla comparativa de tamaños de los archivos generados.
    """
    tabla = Table(title="Comparación de Tamaños de Archivos")
    tabla.add_column("Formato", justify="left", style="cyan", no_wrap=True)
    tabla.add_column("Tamaño (KB)", justify="right", style="magenta")
    
    formatos = [
        ("Binario con struct", "agenda.bin"),
        ("JSON Lines", "agenda.jsonl"),
        ("JSON plano con indentación", "agenda_indent.json")
    ]
    
    for nombre, ruta in formatos:
        if os.path.exists(ruta):
            tamaño_kb = os.path.getsize(ruta) / 1024
            tabla.add_row(nombre, f"{tamaño_kb:.2f}")
        else:
            tabla.add_row(nombre, "Archivo no encontrado")
    
    console = Console()
    console.print(tabla)

mostrar_tabla_comparativa()

'''e): Reflexión integradora: ¿en qué momento del ciclo de vida de los datos conviene cada formato? Sugerencia: pensar en los siguientes escenarios y proponer el formato apropiado para cada uno: persistencia operativa de la aplicación, exportación para consumo por sistemas externos, backup archivado, intercambio con un programa Java que también consume la agenda, log de auditoría que se escribe constantemente y rara vez se lee.

- Para el escenatrio 1, de la persistencia operativa de la aplicación, el formato struct binario, es el mejor y mas rapido, porque otorga los datos en formato nativo, evitando conversiones. En el caso del segundo escenario, exportacion para consumo por sistemas externos, es mejor usar JSON ya que para transferir datos entre pares es el mas accesible al lenguaje humano y entre lenguajes maquina es altamente soportado. Para el tercer escenario, backup archivado, se recomiendo usar JSON plano con identacion, siendo el mas legible y ademas no sufre modificaciones con el paso del tiempo, es decir si guardas en JSON, sin importar el tiempo que pase siempre seguira conservando su forma, a diferencia de un binario que sus bytes no coincisdiran con el formato original. Para el anteúltimo escenario, intercambio con un programa Java que también consume la agenda, ses ideal usar JSON Lines, porque es el formato mas rapido entre lenguajes de programacion, ya que no requiere de codificación ni decodificación. Por último, para el escenario del log de auditoría que se escribe constantemente y rara vez se lee, el formato JSON Lines es el más adecuado, porque al escribir registros de forma creciente, si el programa se rompe solo se borraria el último registro.'''