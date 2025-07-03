import os
import yt_dlp as ytd

def downloader (url: str, quality: str, directory: str, is_playlist: bool, count:bool = False) -> None:
    output = os.path.join(directory, "%(title)s.%(ext)s")
    options = {
        "outtmpl": output,
        "quality": f"bestvideo[height<={quality}]+bestaudio/best[height<={quality}]",
        "format": "mp4",
        "noplaylist": is_playlist
    }

    try:
        with ytd.YoutubeDL(options) as downloader:
            downloader.download([url])
        print("Download completed successfully \n")

    except Exception as e:
        print("An error occurred: ", e)
