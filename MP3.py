import os
from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH
from pathlib import Path


def renameFile(index, path, filename):
    if '.mp3' in filename:
        filename_without_ext = os.path.splitext(filename)[0]

        mp3 = MP3File(path + '/' + filename)
        print(os.path.basename(Path(path + '/' + filename).parent))

        mp3.song = filename_without_ext
        mp3.album = os.path.basename(Path(path + '/' + filename).parent)
        mp3.artist = os.path.basename(Path(path + '/' + filename).parent.parent)
        mp3.track = str(index)
        tags = mp3.get_tags()

        # print(tags)
        # By default selected tags in both versions.
        mp3.set_version(VERSION_BOTH)

        # Change to 2.x version.
        # mp3.set_version(VERSION_2)

        # For 1.x version
        # mp3.set_version(VERSION_1)

        # After the tags are edited, you must call the save method.
        mp3.save()



def renameFolderFiles(path):
    index = 1
    for filename in os.listdir(path):

        if os.path.isdir(path + '/' + filename):
            renameFolderFiles(path + '/' + filename)
        elif os.path.isfile(path + '/' + filename):
            renameFile(index, path, filename)
            index += 1

    return


def main():
    path = input("Enter the directory path where you need to rename: ")
    renameFolderFiles(path)


if __name__ == "__main__":
    main()