import os
from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH

def renameFile(path, filename):
    if '.mp3' in filename:

        if len(filename.split('.')) > 2:
            new_name = filename.split('.')[-2] + '.mp3'
        else :
            return
        mp3 = MP3File(path +'/'+filename)
        
        print('rename {}'.format(filename))
        print('to {}'.format(new_name))
        # extension = os.path.splitext(filename)[1]
        # new_file_name = filename_without_ext + "_n"
        # new_file_name_with_ext = new_file_name + extension
        # print(new_file_name_with_ext)
        os.rename(os.path.join(path, filename), os.path.join(path, new_name))
def renameFolderFiles(path):
    for filename in os.listdir(path):

        if os.path.isdir(path+'/'+filename):
            renameFolderFiles(path+'/'+filename)
        elif os.path.isfile(path+'/'+filename):
            renameFile(path,filename)

    return

def main():
    path = input("Enter the directory path where you need to rename: ")
    renameFolderFiles(path)

if __name__ == "__main__":
    main()