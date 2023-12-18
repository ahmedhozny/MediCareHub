from src.models.person import Person


class WardBoy(Person):
    salary: int
    room_number: int

    def __init__(self, person_id: int, first_name: str, last_name: str, phone: str,
                 salary: int, room_number: int):
        super().__init__(person_id, first_name, last_name, phone)
        self.salary = salary
        self.room_number = room_number

    def display_info(self):
        super().display_info()
        print(f"Salary: {self.salary}, Room Number: {self.room_number}")
