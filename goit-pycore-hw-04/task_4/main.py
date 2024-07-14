from bot_component import ConsoleBot

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip()
        if not user_input:
            print("Invalid command.")
            continue

        bot = ConsoleBot(user_input=user_input)
        command, args = bot.parse_input()

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(bot.add_contact(args, contacts))
        elif command == "change":
            print(bot.change_contact(args, contacts))
        elif command == "phone":
            print(bot.show_phone(args, contacts))
        elif command == "all":
            print(bot.show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()


