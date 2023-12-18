from src.models.person import Person
from datetime import datetime


class Patient(Person):
    gender: int
    date_of_birth: datetime
    home_address: str
    balance: float
    number_of_records: int

    def __init__(self, first_name: str, last_name: str, phone: str,
                 gender: int, date_of_birth: datetime, home_address: str,
                 balance: float, number_of_records: int) -> None:
        super().__init__(first_name, last_name, phone)
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.home_address = home_address
        self.balance = balance
        self.number_of_records = number_of_records

    def display_info(self):
        super().display_info()
        print(f"Gender: {self.gender}, Date of Birth: {self.date_of_birth.strftime('%Y-%m-%d')},"
              f" Home Address: {self.home_address}, Balance: {self.balance},"
              f" Number of Records: {self.number_of_records}")
