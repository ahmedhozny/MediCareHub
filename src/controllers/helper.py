from typing import Type

from src.models.model import Model


def insert_schema(cls: Type[Model], attributes: dict) -> str:
    res = ""
    res2 = ""
    for key, value in attributes.items():
        if value is not None:
            res += key + ", "
            res2 += "'" + str(value) + "', "

    return f"INSERT INTO {cls.__name__} ({res[:-2]}) VALUES ({res2[:-2]})"


def update_schema(cls: Type[Model], id: int, attributes: dict) -> str:
    res = ""
    for key, value in attributes.items():
        if value is not None:
            res += key + " = '" + str(value) + "', "
    return f"UPDATE {cls.__name__} SET {res[:-2]} WHERE ID = {id};"


def update_record_schema(patient_id: int, record_id: int, attributes: dict) -> str:
    res = ""
    for key, value in attributes.items():
        if value is not None:
            res += key + " = '" + str(value) + "', "
    return f"UPDATE MedicalRecord SET {res[:-2]} WHERE PatientID = {patient_id} AND ID = {record_id}"
