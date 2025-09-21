import os
import re

# Solicitar datos al usuario
directorio = input("📂 Introduce la ruta del directorio: ")
patron = input("🔍 Introduce el patrón de texto a buscar (expresión regular): ")
reemplazo = input("✏️ Introduce el texto de reemplazo: ")

# Iterar sobre los archivos del directorio
for nombre_archivo in os.listdir(directorio):
    ruta_completa = os.path.join(directorio, nombre_archivo)

    # Verificar si es un archivo (no una carpeta)
    if os.path.isfile(ruta_completa):
        nuevo_nombre = re.sub(patron, reemplazo, nombre_archivo)

        # Solo renombrar si el nombre cambia
        if nuevo_nombre != nombre_archivo:
            nueva_ruta = os.path.join(directorio, nuevo_nombre)
            os.rename(ruta_completa, nueva_ruta)
            print(f"✅ Renombrado: {nombre_archivo} → {nuevo_nombre}")