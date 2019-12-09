from MP3 import tagMP3Files
from Rename import renameFolderFiles

def main():
    path = input("Enter the directory path: ")
    renameFolderFiles(path)
    tagMP3Files(path)

if __name__ == "__main__":
    main()