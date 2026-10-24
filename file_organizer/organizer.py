import shutil
from pathlib import Path

CATEGORIES = {
    "Images": [
        ".jpg",
        ".jpeg",
        ".png",
        ".webp",
        ".heic",
        ".jfif",
        ".gif",
        ".bmp",
        ".svg",
    ],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx", ".xlsm", ".csv"],
    "Video": [".mp4", ".mkv", ".avi", ".mov", ".webm"],
    "Music": [".mp3", ".wav", ".m4a", ".aac", ".flac"],
    "Compressed": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Programs": [".exe", ".msi"],
    "Code": [".py", ".ipynb", ".tsx", ".html", ".htm", ".json"],
    "Torrents": [".torrent"],
    "Playlists": [".m3u8", ".m3u", ".mpd"],
    "Subtitles": [".srt"],
    "Ebooks": [".epub"],
}

SKIP_FILES = {"desktop.ini", "thumbs.db"}
DRY_RUN = False

def get_unique_destination(destination):
    if not destination.exists():
        return destination

    counter = 1
    while True:
        new_name = f"{destination.stem} ({counter}){destination.suffix}"
        new_destination = destination.parent / new_name
        if not new_destination.exists():
            return new_destination
        counter += 1


EXTENSION_TO_CATEGORY = {}
for category, extensions in CATEGORIES.items():
    for ext in extensions:
        EXTENSION_TO_CATEGORY[ext] = category


folder = Path(r"C:\Users\musta\Downloads")
for item in folder.iterdir():
    if item.is_file():
        if item.name.lower() in SKIP_FILES:
            continue
        category = EXTENSION_TO_CATEGORY.get(item.suffix.lower(), "Others")
        destination = folder / category / item.name
        destination = get_unique_destination(destination)
        print(item.name, "->", destination)
        if not DRY_RUN:
            destination.parent.mkdir(exist_ok=True)
            shutil.move(item, destination)
