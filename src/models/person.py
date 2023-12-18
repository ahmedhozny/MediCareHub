class Person:
    id: int
    first_name: str
    last_name: str
    phone: str

    def __init__(self, first_name: str, last_name: str, phone: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone

    def display_info(self):
        print(
            f"Name: {self.first_name} {self.last_name}, Phone: {self.phone}")
