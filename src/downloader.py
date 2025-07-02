import os
import yt_dlp as ytd

def download_video(url: str, storage_path: str,quality:str, is_playlist: bool = False) -> None:
    """Downloads a single video or a full playlist from YouTube."""
    options = {
        "outtmpl": os.path.join(storage_path, "%(title)s.%(ext)s"),  # Corrected key from "output" to "outtmpl"
        "format": f"bestvideo[height<={quality}]+bestaudio/best[height<={quality}]",
        "merge_output_format": "mp4",
        "noplaylist": not is_playlist,  # Prevents playlist download if it's a single video
    }

    try:
        with ytd.YoutubeDL(options) as downloader:
            downloader.download([url])
        print("✅ Download completed successfully!\n")

    except Exception as e:
        print(f"❌ Error downloading {'playlist' if is_playlist else 'video'}: {e}")

def download_single_video(video_url: str, storage_path: str, quality:str) -> None:
    """Wrapper function to download a single video."""
    download_video(video_url, storage_path, quality, is_playlist=False)

def download_playlist(playlist_url: str, storage_path: str, quality:str) -> None:
    """Wrapper function to download a playlist."""
    download_video(playlist_url, storage_path, quality, is_playlist=True)
