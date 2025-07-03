def source() -> list[dict]:
    storage = []

    while True: 
        url = input("Youtube 'video' or 'playlist' URL: ").strip()
        quality = input("Enter the quality (240, 360, 480, 720, 1080): ").strip()
        directory = input("If you want to create a directory, Type a name (Optional): ") or ""

        item = {
            "url": url,
            "quality": quality,
            "directory": directory
        }

        storage.append(item)

        is_Continue = input("Do you want to add a new url? (Y/n)").strip().lower()

        if(is_Continue == "n"):
            break

    try:
        with open("source.txt", "w") as f:
            f.write(str(storage))

            print("source file created successfully.")
    except:
        print("An error occurred")

    return storage