from errors_handlers import input_error


class ConsoleBot:
    def __init__(self, user_input: str) -> None:
        self.user_input = user_input

    def parse_input(self):
        try:
            cmd, *args = self.user_input.strip().split()
            return cmd.lower(), args
        except Exception as ex:
            print(f"An error has occurred while parsing user input: {ex}")

    @staticmethod
    @input_error
    def add_contact(args, contacts):
        if len(args) != 2:
            raise IndexError
        name, phone = args
        contacts[name] = phone
        return "Contact added."

    @staticmethod
    @input_error
    def change_contact(args, contacts):
        if len(args) != 2:
            raise IndexError
        name, phone = args
        if name in contacts:
            contacts[name] = phone
            return "Contact updated."
        else:
            raise KeyError

    @staticmethod
    @input_error
    def show_phone(args, contacts):
        if len(args) != 1:
            raise IndexError
        name = args[0]
        if name in contacts:
            return f"{name}: {contacts[name]}"
        else:
            raise KeyError

    @staticmethod
    @input_error
    def show_all(contacts):
        if contacts:
            items = contacts.items()
            res = "\n".join([f"{name}: {phone}" for name, phone in items])
            return res
        else:
            return "No contacts found."
