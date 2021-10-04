import sys
import os
import glob
import shutil

def main():
    extensions = {
        ".mp3": "Music",
        ".wav": "Music",
        ".mp4": "Videos",
        ".mov": "Videos",
        ".jpg": "Images",
        ".jpeg": "Images",
        ".png": "Images",
        ".pdf": "Documents",
    }

    path = sys.argv[1]
    files = glob.glob(path + '/*')
    for file in files:
        extension = os.path.splitext(file)[-1]
        folder = extensions.get(extension)
        if folder:
            folder = os.path.join(path, folder)
            os.makedirs(folder, exist_ok=True)
            shutil.move(file, folder)

main()