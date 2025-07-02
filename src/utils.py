import shutil
import sys

def check_ffmpeg() -> None:
    # Checks if FFmpeg is installed and available in system PATH.
    if shutil.which('ffmpeg') is None:
        print("❌ Error: FFmpeg is not installed or not in PATH.")
        print("🔗 Download FFmpeg: https://ffmpeg.org/download.html")
        sys.exit(1) # Exit the program if FFmpeg is missing