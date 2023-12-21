from src.models.person import Person
from datetime import datetime


class Patient(Person):
    gender: bool
    date_of_birth: datetime
    home_address: str
    chronic_diseases: str
    balance: float
    number_of_records: int

    @staticmethod
    def relation_attribute_name() -> dict:
        return Person.relation_attribute_name() | {
            'Gender': 'gender',
            "DOB": "date_of_birth",
            "HomeAddress": "home_address",
            "ChronicDiseases": "chronic_diseases",
            "Balance": "balance",
            "NumberOfRecords": "number_of_records"
        }

    def __init__(self, person_id: int | None, first_name: str, last_name: str, phone: str,
                 gender: bool, date_of_birth: datetime, home_address: str, chronic_diseases: str,
                 balance: float, number_of_records: int) -> None:
        super().__init__(person_id, first_name, last_name, phone)
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.home_address = home_address
        self.chronic_diseases = chronic_diseases
        self.balance = balance
        self.number_of_records = number_of_records

    def __str__(self):
        return (f"{super().__str__()}, Gender: {self.gender}, Date of Birth: {self.date_of_birth.strftime('%Y-%m-%d')},"
                f" Home Address: {self.home_address}, ChronicDiseases: {self.chronic_diseases}, Balance: {self.balance},"
                f" Number of Records: {self.number_of_records}")

    def __dict__(self) -> dict:
        return {
            "ID": self.id,
            "FirstName": self.first_name,
            "LastName": self.last_name,
            "Phone": self.phone,
            'Gender': self.gender,
            "DOB": self.date_of_birth,
            "HomeAddress": self.home_address,
            "ChronicDiseases": self.chronic_diseases,
            "Balance": self.balance,
            "NumberOfRecords": self.number_of_records
        }
