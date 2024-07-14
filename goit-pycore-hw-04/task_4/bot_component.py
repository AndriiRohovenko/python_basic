class ConsoleBot:
    def __init__(self, user_input: str) -> None:
        self.user_input = user_input


    def parse_input(self):
        try:
            cmd, *args = self.user_input.strip().split()
            return cmd.lower(), args
        except Exception as ex:
            print(f"An error has occurred while user input parsing.{ex}")
    
    @staticmethod
    def add_contact(args, contacts):
        try:
            if len(args) != 2:
                return "Error: Invalid number of arguments for 'add' command."
            name, phone = args
            contacts[name] = phone
            return "Contact added."
        except Exception as ex:
            print(f"An error has occurred while add_contact.{ex}")


    @staticmethod
    def change_contact(args, contacts):
        try:
            if len(args) != 2:
                return "Error: Invalid number of arguments for 'change' command."
            name, phone = args
            if name in contacts:
                contacts[name] = phone
                return "Contact updated."
            else:
                return "Error: Contact not found."
        except Exception as ex:
            print(f"An error has occurred while change_contact.{ex}")
        
    @staticmethod
    def show_phone(args, contacts):
        try:
            if len(args) != 1:
                return "Error: Invalid number of arguments for 'phone' command."
            name = args[0]
            if name in contacts:
                return f"{name}: {contacts[name]}"
            else:
                return "Error: Contact not found."           
        except Exception as ex:
            print(f"An error has occurred while user show_phone.{ex}")

    @staticmethod
    def show_all(contacts):
        try:
            if contacts:
                return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
            else:
                return "No contacts found."
        except Exception as ex:
            print(f"An error has occurred while show_all contacts.{ex}")