from base import Field


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
        return value.isdigit() and len(value) == 10
