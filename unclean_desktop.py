import os
import tqdm
from user_info import username

# reverse function clean_desktop
def unclean_desktop():
    # get the path to the desktop
    desktop = f'/Users/{username}/Desktop'
    # get the list of files in the desktop
    files = os.listdir(desktop)
    # loop through the files
    # same for with tqdm
    # filter files in only folders
    folders = [file for file in files if os.path.isdir(os.path.join(desktop, file))]
    for folder in tqdm.tqdm(folders):
        # get the path to the folder
        folder_path = os.path.join(desktop, folder)
        # get the list of files in the folder
        files = os.listdir(folder_path)
        # loop through the files
        for file in files:
            # get the path to the file
            file_path = os.path.join(folder_path, file)
            # move the file out of the folder
            os.rename(file_path, os.path.join(desktop, file))
        # remove folder
        os.rmdir(os.path.join(desktop, folder))

# call the function
unclean_desktop()
