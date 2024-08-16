import os

def eliminar_prefijo_video(ruta):
    """
    Elimina el prefijo "VIDEO-" de todas las carpetas que lo tengan en la ruta especificada.

    Args:
        ruta (str): Ruta de la carpeta desde donde iniciar la búsqueda.
    """

    for root, dirs, files in os.walk(ruta):
        for dir in dirs:
            if dir.startswith("VIDEO-"):
                nueva_ruta = os.path.join(root, dir)
                nuevo_nombre = dir[6:]  # Eliminamos los primeros 6 caracteres
                nueva_ruta_final = os.path.join(root, nuevo_nombre)
                os.rename(nueva_ruta, nueva_ruta_final)
                print(f"Nombre de carpeta cambiado: {nueva_ruta} -> {nueva_ruta_final}")

# Ruta donde iniciar la búsqueda (puedes cambiarla)
ruta_inicial = os.getcwd()
# Ejecutar la función
eliminar_prefijo_video(ruta_inicial)