def validate_url(url):
    # Aquí puedes agregar la lógica para validar la URL
    # Por ejemplo, verificar si la URL es de un sitio compatible con yt-dlp
    return True  # Cambia esto según la validación

def get_download_options(option):
    options = {
        'video': {
            'format': 'bestvideo[ext=mp4]/bestvideo+bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }],
            'concurrent_fragment_downloads': 5,
        },
        'audio': {
            'format': 'bestaudio[ext=m4a]/bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredformat': 'mp3',
            }],
            'concurrent_fragment_downloads': 5,
        },
        'both': {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }],
            'concurrent_fragment_downloads': 5,
        },
        'combined': {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'merge_output_format': 'mp4',
            'concurrent_fragment_downloads': 5,
        },
    }
    return options.get(option, {})