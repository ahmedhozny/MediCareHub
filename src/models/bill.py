import datetime

from src.models.model import Model


class Bill(Model):
    patient_id: int
    bill_amount: float
    bill_date: datetime.datetime

    @staticmethod
    def relation_attribute_name() -> dict:
        return (Model.relation_attribute_name() |
                {
                    'PatientID': 'first_name',
                    'BillAmount': 'last_name',
                    'BillingDate': 'phone'
                })

    def __init__(self, bill_id: int | None, patient_id: int, bill_amount: float, bill_date: datetime.datetime) -> None:
        super().__init__(bill_id)
        self.patient_id = patient_id
        self.bill_amount = bill_amount
        self.bill_date = bill_date

    def __str__(self):
        return (f"{super().__str__()}, Bill Number: {self.id}, Patient: {self.patient_id},"
                f" Amount: {self.bill_amount}, Date: {self.bill_date}")

    def __dict__(self) -> dict:
        return {
            'ID': self.id,
            'PatientID': self.patient_id,
            'BillAmount': self.bill_amount,
            'BillingDate': self.bill_date
        }
