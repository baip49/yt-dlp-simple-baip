class Downloader:
    def __init__(self, url):
        self.url = url

    def download_video(self, output_path):
        import yt_dlp

        ydl_opts = {
            'format': 'bestvideo',
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.url])

    def download_audio(self, output_path):
        import yt_dlp

        ydl_opts = {
            'format': 'bestaudio',
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.url])

    def download_both(self, output_path):
        import yt_dlp

        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.url])

    def download_combined(self, output_path):
        import yt_dlp

        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'merge_output_format': 'mp4',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.url])