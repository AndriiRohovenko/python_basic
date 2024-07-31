from collections import UserDict
from datetime import datetime
from datetime import timedelta

from core.decorators import input_error


class AddressBook(UserDict):
    def add_record(self, record):
        try:
            self.data[record.name.value] = record
        except Exception as e:
            print(f"Failed to add record: {e}")

    @input_error
    def find(self, name):
        try:
            return self.data.get(name)
        except KeyError as e:
            print(f"Record with name {name} not found: {e}")
            return None

    @input_error
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
                    "phones": [phone.value for phone in record.phones],
                    "birthday": record.birthday.bd_date.strftime("%d.%m.%Y")
                    if record.birthday
                    else "None",
                }
                contacts_list.append(contact)
            return contacts_list
        except Exception as e:
            print(f"Unknown error: {e}")

    @input_error
    def get_contact_birthday(self, user_name: str):
        try:
            if user_name:
                for record in self.data.values():
                    if record.name.value == user_name:
                        return record.birthday.bd_date.strftime("%d.%m.%Y")
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
                if birthday == "None":
                    continue
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
                            "congratulation_date": congratulation_date.strftime(
                                "%d.%m.%Y"
                            ),
                        }
                    )

            return upcoming_birthdays
        except Exception as ex:
            print(f"An unknown error occurred: {ex}")
