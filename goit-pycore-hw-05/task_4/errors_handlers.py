def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Error: Contact not found."
        except ValueError:
            return "Error: Give me name and phone please."
        except IndexError:
            return "Error: Invalid number of arguments LOLOLLO."
        except Exception as e:
            return f"An unexpected error occurred: {e}"

    return inner
