from source import source
from controller import controller

if __name__ == "__main__":
    print("YoutubeDownloader is running, v1.1")
    data = source()
    
    controller(data)    