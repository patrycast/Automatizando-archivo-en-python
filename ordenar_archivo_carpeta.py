import os
import shutil

ruta= input("Ingrese la ruta de la carpeta a organizar: ")

#tipo de carpetas que vamos a crear
tipos=["Imágenes", "PDFs", "Documentos_txt"]

#crear carpetas si no existen
for carpeta in tipos:
    ruta_carpeta= os.path.join(ruta,carpeta)

    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)

#mover archivos segun la extensión
for archivo in os.listdir(ruta):
    if archivo.endswith(".png") or archivo.endswith(".jpg") or archivo.endswith(".jpeg"):
        shutil.move(os.path.join(ruta, archivo), 
            os.path.join(ruta, "Imágenes", archivo))  

    elif archivo.endswith(".pdf") or archivo.endswith(".odt"):
        shutil.move(os.path.join(ruta, archivo),
                    os.path.join(ruta, "PDFs", archivo))      
        
    elif archivo.endswith(".pdf") or archivo.endswith(".txt"):
        shutil.move(os.path.join(ruta, archivo),
                    os.path.join(ruta, "Documentos_txt", archivo)) 