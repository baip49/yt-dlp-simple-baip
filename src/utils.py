def validate_url(url):
    # Aquí puedes agregar la lógica para validar la URL
    # Por ejemplo, verificar si la URL es de un sitio compatible con yt-dlp
    return True  # Cambia esto según la validación

def get_download_options(option):
    options = {
        'video': {
            'format': 'bestvideo',
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }],
            'concurrent_fragment_downloads': 5,
        },
        'audio': {
            'format': 'bestaudio',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredformat': 'mp3',
            }],
            'concurrent_fragment_downloads': 5,
        },
        'both': {
            'format': 'bestvideo+bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }],
            'concurrent_fragment_downloads': 5,
        },
        'combined': {
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
            'concurrent_fragment_downloads': 5,
        },
    }
    return options.get(option, {})