from src.models.person import Person
from  datetime import datetime
class Patient(Person):
    gender: int
    date_of_birth: datetime
    home_address: str
    balance: float
    number_of_records:int
