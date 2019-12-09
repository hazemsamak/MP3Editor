from MP3 import tagMP3Files
from Rename import renameFolderFiles
import os

def main():
    path = input("Enter the directory path: ")
    absolute_path = os.path.abspath(path)
    renameFolderFiles(absolute_path)
    tagMP3Files(path)

if __name__ == "__main__":
    main()