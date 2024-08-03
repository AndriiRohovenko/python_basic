import os
import pickle


class Serialization:
    def __init__(self, item, filename) -> None:
        self.item = item
        self.filename = filename

    def save_data(self):
        try:
            os.makedirs(os.path.dirname(self.filename), exist_ok=True)
            with open(self.filename, "wb") as file:
                pickle.dump(self.item, file)
            print(f"Data successfully saved to {self.filename}")
        except Exception as ex:
            print(f"An error occurred while saving data: {ex}")

    def load_data(self):
        try:
            with open(self.filename, "rb") as file:
                self.item = pickle.load(file)
            print(f"Data successfully loaded from {self.filename}")
            return self.item
        except FileNotFoundError:
            # print(f"File {self.filename} not found.")
            return type(self.item)()  # Returns a new instance of the item's type
        except Exception as ex:
            print(f"An error occurred while loading data: {ex}")
