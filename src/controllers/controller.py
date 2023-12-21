from src.models.medical_record import MedicalRecord
from src.models.model import Model
from src.utils.database import conn
from typing import List, Type
import sys

from src.controllers.helper import *

# Adjust the path accordingly
sys.path.append(
    r"C:\Users\Serag Amged\Programing\FCDS\Level 4\Adv-DB\MediCareHub")


def new(model: Model) -> int | None:
    query = insert_schema(type(model), model.__dict__())
    with conn.cursor() as cursor:
        cursor.execute(query)
        conn.commit()
        return cursor.lastrowid


def list_model(cls: Type[Model]) -> List[Model]:
    query = f"SELECT * FROM {cls.__name__}"
    with conn.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()

    instances = []
    for row in rows:
        instance = cls(*row)
        instances.append(instance)
    return instances


def get_by_id(cls: Type[Model], id: int) -> Model | None:
    query = f"SELECT * FROM {cls.__name__} WHERE ID = %s"
    with conn.cursor() as cursor:
        cursor.execute(query, (id,))
        row = cursor.fetchone()
    if row is None:
        return None
    return cls(*row)


def update(model: Model) -> int | None:
    obj = get_by_id(model.__class__, model.id)
    if obj is None:
        raise Exception("id does not exist")

    with conn.cursor() as cursor:
        query = update_schema(model.__class__, model.id, model.__dict__())
        cursor.execute(query)
        conn.commit()
    return model.id


def delete(model: Model) -> int | None:
    obj = get_by_id(model.__class__, model.id)
    if obj is None:
        raise Exception("id does not exist")

    query = f"DELETE FROM {model.__class__.__name__} WHERE ID = %s"
    with conn.cursor() as cursor:
        cursor.execute(query, (id,))
        conn.commit()
    return model.id


def get_medical_record(patient_id: int, record_id: int) -> MedicalRecord | None:
    query = "SELECT * FROM MedicalRecord WHERE PatientID = %s AND ID = %s"
    with conn.cursor() as cursor:
        cursor.execute(query, (patient_id, record_id))
        row = cursor.fetchone()
    if row is None:
        return None
    row = list(row)
    row[0], row[1] = row[1], row[0]
    return MedicalRecord(*row)


def update_medical_record(record: MedicalRecord) -> int | None:
    query = update_record_schema(record.patient_id, record.id, record.__dict__())
    with conn.cursor() as cursor:
        cursor.execute(query)
        conn.commit()
    return record.id

