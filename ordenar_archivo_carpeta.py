import os
import shutil

ruta= input("Ingrese la ruta de la carpeta a organizar: ")

#tipo de carpetas que vamos a crear

extensiones= {
    ".jpg": "Imágenes",
    ".jpeg": "Imágenes",
    ".png": "Imágenes",
    ".pdf": "PDFs",
    ".odt": "PDFs",
    ".txt": "Documentos_txt"
}

#crear carpetas si no existen
for carpeta in set(extensiones.values()):
    ruta_carpeta= os.path.join(ruta,carpeta)

    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)

#mover archivos segun la extensión
for archivo in os.listdir(ruta):
    ruta_archivo= os.path.join(ruta,archivo)

    if os.path.isfile(ruta_archivo):
        nombre,extension= os.path.splitext(archivo)
        extension= extension.lower()

        if extension in extensiones:
            destino= os.path.join(ruta, extensiones[extension], archivo)
            shutil.move(ruta_archivo, destino)
