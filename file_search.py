# Functions that manipulate files within your user account
from enum_choices import DateOption, Direction
from utils import DateBuilder

from pathlib import Path
import os
from datetime import datetime, date
import shutil

main_path = Path(f"C:\\Users\\{os.getlogin()}\\Desktop")

def find_file(file_to_search: str):
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
    date_string = str(formatted_timestamp)[0:10]
    print(f"Last accessed in: {date_string}")

def find_file_by_date(direction: Direction, date_str: str):
    new_date = DateBuilder.string_to_date(date_str)
    found_files = main_path.rglob('script.js')
    match (direction):
        case Direction.BEFORE:
            for file in found_files:
                timestamp = datetime.fromtimestamp(file.stat().st_atime)
                timestamp_str = DateBuilder.timestamp_to_string(timestamp)
                file_date = DateBuilder.string_to_date(timestamp_str)
                if (file_date < new_date):
                    print(timestamp)           
        

# found_files = find_file('script.js')
find_file_by_date(Direction.BEFORE, '2024-12-21')

# for file in found_files:
#     show_file_stats(file)
    # copy_file(file, 'crazyfolder')

        