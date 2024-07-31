from components.address_book import AddressBook
from components.record import Record


def parse_input(user_input):
    parts = user_input.split()
    command = parts[0].lower()
    args = parts[1:]
    return command, args


def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
        command = command.lower()
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            if len(args) >= 2:
                name = args[0]
                phone = args[1]
                record = book.find(name)
                if not record:
                    record = Record(name)
                    book.add_record(record)
                add_phone = record.add_phone(phone)
                print(add_phone)
                if add_phone is True:
                    print(f"Added phone {phone} for {name}.")
            else:
                print("Usage: add <name> <phone>")
        elif command == "change":
            if len(args) >= 3:
                name = args[0]
                old_phone = args[1]
                new_phone = args[2]
                record = book.find(name)
                if record:
                    record.edit_phone(old_phone, new_phone)
                    print(f"Changed phone from {old_phone} to {new_phone} for {name}.")
                else:
                    print(f"Record with name {name} not found.")
            else:
                print("Usage: change <name> <old_phone> <new_phone>")
        elif command == "phone":
            if len(args) >= 1:
                name = args[0]
                record = book.find(name)
                if record:
                    print(
                        f"{name}'s phones: {', '.join(phone.value for phone in record.phones)}"
                    )
                else:
                    print(f"Record with name {name} not found.")
            else:
                print("Usage: phone <name>")
        elif command == "all":
            contacts = book.get_all_contacts()
            if contacts:
                for contact in contacts:
                    name = contact["name"]
                    phones = ", ".join(contact["phones"])
                    birthday = contact["birthday"]
                    print(f"Name: {name}, Phones: {phones}, Birthday: {birthday}")
            else:
                print("No contacts found.")
        elif command == "add-birthday":
            if len(args) >= 2:
                name = args[0]
                birthday = args[1]
                record = book.find(name)
                if record:
                    record.add_birthday(birthday)
                    print(f"Added birthday {birthday} for {name}.")
                else:
                    print(f"Record with name {name} not found.")
            else:
                print("Usage: add-birthday <name> <birthday>")
        elif command == "show-birthday":
            if len(args) >= 1:
                name = args[0]
                birthday = book.get_contact_birthday(name)
                if birthday:
                    print(f"{name}'s birthday is on {birthday}.")
                else:
                    print(f"No birthday found for {name}.")
            else:
                print("Usage: show-birthday <name>")
        elif command == "birthdays":
            upcoming_birthdays = book.get_upcoming_birthdays()
            if upcoming_birthdays:
                for entry in upcoming_birthdays:
                    print(
                        f"{entry['name']}'s birthday is on {entry['congratulation_date']}."
                    )
            else:
                print("No upcoming birthdays.")
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
