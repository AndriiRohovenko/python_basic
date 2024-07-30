from collections import UserDict
from datetime import datetime
from datetime import timedelta

from fields import Birthday
from fields import Name
from fields import Phone


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_birthday(self, date: str):
        try:
            if date != None:
                self.birthday = Birthday(date)
        except Exception as e:
            print(f"Failed to add birthday: {e}")

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
        return f"Contact name: {self.name.value}, Birthday: {self.birthday}, phones: {phones_str}"


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

    def get_all_contacts(self):
        try:
            contacts_list = []
            for record in self.data.values():
                contact = {
                    "name": record.name.value,
                    "birthday": record.birthday.bd_date.strftime("%d.%m.%Y"),
                }
                contacts_list.append(contact)
            return contacts_list

        except Exception as e:
            print(f"Unknown error: {e}")


def get_upcoming_birthdays(self):
    try:
        today = datetime.today().date()
        upcoming_birthdays = []
        one_week_from_today = today + timedelta(days=7)
        users = self.get_all_contacts()
        for user in users:
            name = user["name"]
            birthday = user["birthday"]
            birthday_date = datetime.strptime(birthday, "%d.%m.%Y").date()

            # Set birthday to current year
            birthday_this_year = birthday_date.replace(year=today.year)

            # Move to next year if birthday passed
            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)

            # Check if birthday is within the next 7 days
            if today <= birthday_this_year <= one_week_from_today:
                # Adjust for weekend
                if birthday_this_year.weekday() == 5:
                    congratulation_date = birthday_this_year + timedelta(days=2)
                elif birthday_this_year.weekday() == 6:
                    congratulation_date = birthday_this_year + timedelta(days=1)
                else:
                    congratulation_date = birthday_this_year

                upcoming_birthdays.append(
                    {
                        "name": name,
                        "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
                    }
                )

        return upcoming_birthdays
    except Exception as ex:
        print(f"An unknown error occurred: {ex}")
