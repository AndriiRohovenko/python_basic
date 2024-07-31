from components.fields import Birthday
from components.fields import Name
from components.fields import Phone
from core.decorators import input_error


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    @input_error
    def add_birthday(self, date: str):
        try:
            if date != None:
                self.birthday = Birthday(date)
        except Exception as e:
            print(f"Failed to add birthday: {e}")

    @input_error
    def add_phone(self, phone_number):
        try:
            phone = Phone(phone_number)
            self.phones.append(phone)
            return True
        except Exception as e:
            print(f"Failed to add phone: {e}")
            return False

    @input_error
    def remove_phone(self, phone_number):
        try:
            self.phones = [
                phone for phone in self.phones if phone.value != phone_number
            ]
        except Exception as e:
            print(f"Failed to remove phone: {e}")

    @input_error
    def edit_phone(self, old_number, new_number):
        try:
            for phone in self.phones:
                if phone.value == old_number:
                    phone.value = new_number
                    return
            raise ValueError(f"Phone number {old_number} not found in record.")
        except Exception as e:
            print(f"Failed to edit phone: {e}")

    @input_error
    def find_phone(self, phone_number):
        try:
            for phone in self.phones:
                if phone.value == phone_number:
                    return phone
            raise ValueError(f"{phone_number} not found.")
        except Exception as e:
            print(f"Failed to find phone: {e}")

    def __str__(self):
        if self.phones:
            phones_str = "; ".join(phone.value for phone in self.phones)
        else:
            phones_str = "None"
        return f"Contact name: {self.name.value}, Birthday: {self.birthday}, phones: {phones_str}"
