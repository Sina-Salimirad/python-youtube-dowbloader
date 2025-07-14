import os
import yt_dlp as ytd

def downloader (url: str, quality: str, directory: str, is_playlist: bool, count:bool = False) -> None:
    output = os.path.join(directory, "%(title)s.%(ext)s")
    options = {
        "outtmpl": output,
        "format": f"bestvideo[height<={quality}][ext=mp4]+bestaudio[ext=m4a]/best[height<={quality}][ext=mp4]",
        "noplaylist": not is_playlist,
        "merge_output_format": "mp4",
        "format_sort": [f"res:{quality}", "vcodec:h264"]
    }

    print(f"Using quality filter: {options['format']}")

    try:
        with ytd.YoutubeDL(options) as downloader:
            downloader.download([url])
        print("Download completed successfully \n")

    except Exception as e:
        print("An error occurred: ", e)
