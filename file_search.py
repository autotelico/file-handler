# Functions that manipulate files within your user account
from enum_choices import DateOption, Direction
from utils import DateBuilder

from pathlib import Path
import os
from datetime import datetime, date
import shutil

start_dir = Path(f"C:\\Users\\{os.getlogin()}\\Desktop")

class FileHandler:

    @staticmethod
    def find_file(pattern: str):
        """ 
            Finds all files with the given pattern. 
        """
        files = start_dir.rglob(pattern)
        return files

    @staticmethod
    def copy_file(src: str, dest: str):
    # Copies file from a source path to a destination path
        shutil.copy(str(src), os.path.join(start_dir, dest))

    @staticmethod
    def show_file_stats(file):
    # Shows important stats about the file
        print(file)
        file_stats = file.stat()
        timestamp = file_stats.st_atime
        formatted_timestamp = datetime.fromtimestamp(timestamp)
        date_string = str(formatted_timestamp)[0:10]
        print(f"Last accessed in: {date_string}")

    @staticmethod
    def find_file_by_date(pattern: str, direction: Direction, date_str: str):
        """
            Finds a pattern before or after a date.
        """

        new_date = DateBuilder.string_to_date(date_str)
        found_files = start_dir.rglob(pattern)
        
        for file in found_files: 
            timestamp = datetime.fromtimestamp(file.stat().st_birthtime)
            timestamp_str = DateBuilder.timestamp_to_string(timestamp)
            file_date = DateBuilder.string_to_date(timestamp_str)
            found_msg = f"{file.name} - last accessed in {timestamp}"

            match (direction):
                case Direction.BEFORE:
                        if (file_date < new_date):
                            print(found_msg)
                case Direction.AFTER:
                        if (file_date > new_date):
                            print(found_msg)
                            
FileHandler.find_file_by_date('sample.txt', Direction.AFTER, '2024-12-01')

        