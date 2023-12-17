from person import Person


class Nurse(Person):
    salary: int
    email: str
    room_number: int

    def __init__(self, first_name: str, last_name: str, phone: str,
                 salary: int, email: str, room_number: int) -> None:
        super().__init__(first_name, last_name, phone)
        self.salary = salary
        self.email = email
        self.room_number = room_number

    def display_info(self):
        super().display_info()
        print(
            f"Salary: {self.salary}, Email: {self.email}, Room Number: {self.room_number}")
