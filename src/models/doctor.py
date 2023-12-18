from src.models.person import Person


class Doctor(Person):
    job_title: str
    salary: int
    email: str
    office_number: int
