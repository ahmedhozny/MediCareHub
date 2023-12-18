from person import Person


class Doctor(Person):
    job_title: str
    salary: int
    email: str
    office_number: int

    def __init__(self, person_id: int, first_name: str, last_name: str, phone: str,
                 job_title: str, salary: int, email: str, office_number: int) -> None:
        
        super().__init__(person_id, first_name, last_name, phone)
        self.job_title = job_title
        self.salary = salary
        self.email = email
        self.office_number = office_number


