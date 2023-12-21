from src.models.person import Person


class Nurse(Person):
    email: str
    room_id: int
    salary: float

    @staticmethod
    def relation_attribute_name() -> dict:
        return (Person.relation_attribute_name() | {
            'Email': 'email',
            "RoomID": "room_id",
            "Salary": "salary"
        })

    def __init__(self, id: int | None, first_name: str, last_name: str, phone: str,
                 email: str, room_id: int, salary: float) -> None:
        super().__init__(id, first_name, last_name, phone)
        self.email = email
        self.room_id = room_id
        self.salary = salary

    def __str__(self):
        return f"{super().__str__()}, Email: {self.email}, Room ID: {self.room_id}, Salary: {self.salary}"

    def __dict__(self) -> dict:
        return {
            "ID": self.id,
            "FirstName": self.first_name,
            "LastName": self.last_name,
            "Phone": self.phone,
            "Email": self.email,
            "RoomID": self.room_id,
            "Salary": self.salary
        }
