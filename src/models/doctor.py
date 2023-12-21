from src.models.person import Person


class Doctor(Person):
    job_title: str
    salary: float
    email: str
    office_id: int

    @staticmethod
    def relation_attribute_name() -> dict:
        return (Person.relation_attribute_name() |
                {
                    'Email': 'email',
                    "JobTitle": "job_title",
                    "OfficeID": "office_id",
                    "Salary": "salary"
                })

    def __init__(self, person_id: int | None, first_name: str, last_name: str, phone: str,
                 email: str, job_title: str, office_id: int, salary: float) -> None:
        super().__init__(person_id, first_name, last_name, phone)
        self.job_title = job_title
        self.salary = salary
        self.email = email
        self.office_id = office_id

    def __str__(self):
        return (f"{super().__str__()}, Job Title: {self.job_title}, Salary: {self.salary},"
                f" Email: {self.email}, Office ID: {self.office_id}")

    def __dict__(self) -> dict:
        return {
            "ID": self.id,
            "FirstName": self.first_name,
            "LastName": self.last_name,
            "Phone": self.phone,
            "Email": self.email,
            "JobTitle": self.job_title,
            "OfficeID": self.office_id,
            "Salary": self.salary
        }
