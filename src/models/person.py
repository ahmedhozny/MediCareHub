from abc import ABC

from src.models.model import Model


class Person(Model, ABC):
    first_name: str
    last_name: str
    phone: str

    @staticmethod
    def relation_attribute_name() -> dict:
        return (Model.relation_attribute_name() | {
            'FirstName': 'first_name',
            'LastName': 'last_name',
            'Phone': 'phone'
        })

    def __init__(self, person_id: int | None, first_name: str, last_name: str, phone: str) -> None:
        super().__init__(person_id)
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone

    def __str__(self):
        return f'{super().__str__()}, Name: {self.first_name} {self.last_name}'

    def __dict__(self) -> dict:
        return {
            "FirstName": self.first_name,
            "LastName": self.last_name,
            "Phone": self.phone
        }
