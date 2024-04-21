class WoWo():
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def print_smg(self, count:int=1):
        try:
            a = "hello world!!!!!"
            b = "hello git!!!"
            c = "Carpe diem!!"
            for _ in range(count):
                print(f"wowoowo {a} and {b}\n{c}\nFrom: {self.name} > {self.age} years old.")
        except Exception as ex:
            print(f"An error has occured: {ex}")



a = WoWo("Andrii", 29)

a.print_smg(count=100)