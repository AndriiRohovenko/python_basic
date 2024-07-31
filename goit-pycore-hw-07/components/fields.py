from datetime import datetime

from core.base import Field


class Name(Field):
    def __init__(self, value):
        super().__init__(value)

    def __str__(self):
        return str(self.value)


class Phone(Field):
    def __init__(self, value=None):
        if value is not None and not self.validate_phone(value):
            raise ValueError("Phone number must contain exactly 10 digits.")
        super().__init__(value)

    def __str__(self):
        return str(self.value) if self.value is not None else "None"

    @staticmethod
    def validate_phone(value):
        # print(len(value))
        return value.isdigit() and len(value) == 10


class Birthday(Field):
    def __init__(self, value):
        self.bd_date = self.__validated_date(value)

    @staticmethod
    def __validated_date(date_str):
        try:
            date = datetime.strptime(date_str, "%d.%m.%Y")
            if date > datetime.now():
                raise ValueError("Date cannot be in the future.")
            return date
        except ValueError as e:
            raise ValueError(f"Invalid format: {e}. Use DD.MM.YYYY") from e

    def __str__(self):
        return self.bd_date.strftime("%d.%m.%Y")
