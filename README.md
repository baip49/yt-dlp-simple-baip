# yt-dlp-workspace

Este proyecto es una herramienta para descargar contenido de video y audio utilizando `yt-dlp`. Permite al usuario elegir entre descargar solo el video, solo el audio, ambos en archivos separados o combinados en un solo archivo.

## Estructura del Proyecto

```
yt-dlp-workspace
├── src
│   ├── main.py          # Punto de entrada de la aplicación
│   ├── downloader.py    # Contiene la clase Downloader y métodos de descarga
│   ├── utils.py         # Funciones auxiliares para validación y configuración
│   └── custom_types
│       └── __init__.py  # Definiciones de tipos o interfaces
├── requirements.txt     # Dependencias necesarias
└── README.md            # Documentación del proyecto
```
## Requisitos

Se recomienda utilizar un entorno virtual (venv) para aislar las dependencias del proyecto. Para ejecutar este proyecto, necesitas tener instalados `yt-dlp` y `ffmpeg`. 

1. Crea y activa un entorno virtual:

    En Visual Studio Code:
    ```
    Control + Shift + P
    Seleccionar "Python: Crear ambiente"
    Seleccionar "venv"
    ```

    En Windows:
    ```
    python -m venv venv
    .\venv\Scripts\activate
    ```

    En macOS/Linux:
    ```
    python3 -m venv venv
    source venv/bin/activate
    ```

2. Instala las dependencias ejecutando:
    ```
    pip install -r requirements.txt
    ```

Asegúrate también de que `ffmpeg` esté instalado y accesible desde tu PATH.

## Uso

1. Clona el repositorio o descarga los archivos.
2. Asegúrate de tener `ffmpeg` instalado y accesible en tu PATH.
3. Ejecuta el archivo `main.py` para iniciar la aplicación:

```
python src/main.py
```

4. Sigue las instrucciones en pantalla para seleccionar la opción de descarga deseada.

## Opciones de Descarga

- **Descargar solo video**: Descarga el video sin audio.
- **Descargar solo audio**: Descarga el audio sin video.
- **Descargar ambos (separados)**: Descarga el video y el audio en archivos diferentes.
- **Descargar combinado**: Descarga el video y el audio en un solo archivo.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar este proyecto, por favor abre un issue o un pull request.