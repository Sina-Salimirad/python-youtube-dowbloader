import os
from utils import check_ffmpeg
from downloader import download_single_video, download_playlist
from config import DEFAULT_STORAGE_PATH

if __name__ == "__main__":
    check_ffmpeg() # Ensure FFmpeg is installed
    url = input("Enter YouTube video or playlist URL: ").strip()
    qulity = input("Enter the Quality [240, 360, 480, 720, 1080]: ")
    folder = input("Enter new name for folder: ") or ""
    DEFAULT_STORAGE_PATH = DEFAULT_STORAGE_PATH + folder
    os.makedirs(DEFAULT_STORAGE_PATH, exist_ok=True)


    if "playlist?list" in url:
        download_playlist(url, DEFAULT_STORAGE_PATH, qulity)
    else:
        download_single_video(url, DEFAULT_STORAGE_PATH, qulity)