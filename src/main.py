# main.py

import sys
from downloader import Downloader
import os

def main():
    print("Bienvenido a la herramienta de descarga de videos.")
    url = input("Por favor, ingresa la URL del video: ")
    
    print("Selecciona una opción de descarga:")
    print("1. Solo video")
    print("2. Solo audio")
    print("3. Video y audio (archivos separados)")
    print("4. Video y audio (combinados en un solo archivo)")
    
    option = input("Ingresa el número de la opción deseada: ")
    # output_path = input("Ingresa la ruta de salida para guardar el archivo: ")
    user_home = os.path.expanduser("~")
    output_path = os.path.join(user_home, "downloads", "ytdl")

    downloader = Downloader(url)
    
    if option == '1':
        downloader.download_video(output_path)
    elif option == '2':
        downloader.download_audio(output_path)
    elif option == '3':
        downloader.download_both(output_path)
    elif option == '4':
        downloader.download_combined(output_path)
    else:
        print("Opción no válida. Saliendo...")
        sys.exit(1)

if __name__ == "__main__":
    main()