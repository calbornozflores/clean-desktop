import os
import tqdm
from user_info import username
from datetime import datetime

# create a function that creates folders with dates and movve files into them based on their creation date
def clean_desktop():
    # get the path to the desktop
    desktop = f'/Users/{username}/Desktop'
    # get the list of files in the desktop
    files = os.listdir(desktop)
    # keep files only if the name is different to 4 digits
    files = [file for file in files if not file.isdigit()]
    # loop through the files
    # same for with tqdm
    for file in tqdm.tqdm(files):
        # get the path to the file
        file_path = os.path.join(desktop, file)
        # get the modification date of the file
        modification_date = os.path.getmtime(file_path)
        modification_date = datetime.fromtimestamp(modification_date).strftime('%Y-%m-%d %H:%M:%S')
        # get the year and month of the creation date        
        year = str(modification_date)[:4]
        month = str(modification_date)[5:7]
        # create a folder with the year and month in format desktop/year/month
        folder_path = os.path.join(desktop, year + '/' + month)
        # check if the folder exists
        if not os.path.exists(folder_path):
            # create the folder with all necesary parent folders
            os.makedirs(folder_path) 
        # move the file into the folder
        os.rename(file_path, os.path.join(folder_path, file))


# call the function
clean_desktop()
