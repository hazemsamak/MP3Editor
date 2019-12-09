import os
from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH
from pathlib import Path


def tagMP3File(index, path, filename):
    if '.mp3' in filename:
        song_name = os.path.splitext(filename)[0]
        print('old name'+ song_name)
        if len(song_name.split('.')) > 1:
            song_name = song_name.split('.')[1]

        print(song_name+' -> '+song_name.replace('_', ' '))
        song_name = song_name.replace('_', ' ')


        mp3 = MP3File(path + '/' + filename)


        mp3.song = song_name
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



def tagMP3Files(path):
    index = 1
    for filename in os.listdir(path):

        if os.path.isdir(path + '/' + filename):
            tagMP3Files(path + '/' + filename)
        elif os.path.isfile(path + '/' + filename):
            tagMP3File(index, path, filename)
            index += 1

    return


def main():
    path = input("Enter the directory path where you need to rename: ")
    absolute_path = os.path.abspath(path)
    tagMP3Files(absolute_path)


if __name__ == "__main__":
    main()