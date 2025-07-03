import os
from download import downloader
from constants import DEFAULT_STORAGE_PATH

def controller(data) -> None:
    for d in data:
        directory = os.path.join(DEFAULT_STORAGE_PATH, d["directory"])
        os.makedirs(directory, exist_ok=True)
        print(directory, "is created")
        
        if ("playlist?list" in d["url"]):
            downloader(d["url"], d["quality"], directory, is_playlist=True, count=True) # Download a playlist
        else:
            downloader(d["url"], d["quality"], directory, is_playlist=False) # Download a video
 