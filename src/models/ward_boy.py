from src.models.person import Person


class WardBoy(Person):
    room_id: int
    salary: float

    @staticmethod
    def relation_attribute_name() -> dict:
        return Person.relation_attribute_name() | {
            "RoomID": "room_id",
            "Salary": "salary"
        }

    def __init__(self, person_id: int | None, first_name: str, last_name: str, phone: str,
                 room_id: int, salary: float):
        super().__init__(person_id, first_name, last_name, phone)
        self.room_id = room_id
        self.salary = salary

    def __str__(self):
        return f"{super().__str__()}, Room ID: {self.room_id}, Salary: {self.salary}"

    def __dict__(self) -> dict:
        return {
            "ID": self.id,
            "FirstName": self.first_name,
            "LastName": self.last_name,
            "Phone": self.phone,
            "RoomID": self.room_id,
            "Salary": self.salary
        }
