from datetime import datetime, date

class DateBuilder:
    @staticmethod
    def string_to_date(date_string: str):
        """
            Takes in a date string (must be in the YYYY-MM-DD format) and
            transforms it into a date.
        """
        year, month, day = date_string.split('-')
        new_date = date(int(year), int(month), int(day))
        return new_date
    
    @staticmethod
    def timestamp_to_string(datetime: datetime):
        """
            Takes a datetime object and transforms it into a string in the
            YYYY-MM-DD format.
        """
        date_str = f"{datetime.year}-{datetime.month}-{datetime.day}"
        return date_str
    