from datetime import datetime, date

class DateBuilder:
    @staticmethod
    def string_to_date(date_string: str):
        year, month, day = date_string.split('-')
        new_date = date(int(year), int(month), int(day))
        return new_date
    def timestamp_to_string(datetime: datetime):
        date_str = f"{datetime.year}-{datetime.month}-{datetime.day}"
        return date_str