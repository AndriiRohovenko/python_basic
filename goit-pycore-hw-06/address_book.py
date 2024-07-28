from collections import UserDict

from fields import Name
from fields import Phone


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        try:
            phone = Phone(phone_number)
            self.phones.append(phone)
        except Exception as e:
            print(f"Failed to add phone: {e}")

    def remove_phone(self, phone_number):
        try:
            self.phones = [
                phone for phone in self.phones if phone.value != phone_number
            ]
        except Exception as e:
            print(f"Failed to remove phone: {e}")

    def edit_phone(self, old_number, new_number):
        try:
            for phone in self.phones:
                if phone.value == old_number:
                    phone.value = new_number
                    return
            raise ValueError(f"Phone number {old_number} not found in record.")
        except Exception as e:
            print(f"Failed to edit phone: {e}")

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
        return f"Contact name: {self.name.value}, phones: {phones_str}"


class AddressBook(UserDict):
    def add_record(self, record):
        try:
            self.data[record.name.value] = record
        except Exception as e:
            print(f"Failed to add record: {e}")

    def find(self, name):
        try:
            return self.data.get(name)
        except KeyError as e:
            print(f"Record with name {name} not found: {e}")
            return None

    def delete(self, name):
        try:
            if name in self.data:
                del self.data[name]
            else:
                raise ValueError(f"Record with name {name} not found.")
        except ValueError as e:
            print(f"Failed to delete record: {e}")
        except Exception as e:
            print(f"Unknown error: {e}")
