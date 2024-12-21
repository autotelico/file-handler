# Functions that manipulate files within your user account

from pathlib import Path
import os
from datetime import datetime
import shutil

main_path = Path(f"C:\\Users\\{os.getlogin()}\\Desktop")

def find_file(file_to_search):
    f""" 
    Finds all files with the given name {file_to_search} 
    """
    file_to_find = main_path.rglob(file_to_search)
    return file_to_find

def copy_file(src: str, dest: str):
# Copies file from a source path to a destination path
    shutil.copy(str(src), os.path.join(main_path, dest))

def show_file_stats(file):
# Shows important stats about the file
    print(file)
    file_stats = file.stat()
    timestamp = file_stats.st_atime
    formatted_timestamp = datetime.fromtimestamp(timestamp)
    print(f"Last accessed in: {formatted_timestamp}")

found_files = find_file('App.jsx')

for file in found_files:
    show_file_stats(file)
    copy_file(file, 'crazyfolder')

        