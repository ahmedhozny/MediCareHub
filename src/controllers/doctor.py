from typing import List
from models import doctor
from models.doctor import Doctor
from src.utils.database import conn


def new(new_doctor: Doctor):
    cursor = conn.cursor()
    query = "INSERT INTO Doctor (DoctorID, FirstName, LastName, PhoneNumber, EmailAddress, JobTitle, OfficeNumber,Salary) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(query, (new_doctor.id, new_doctor.first_name,))
    conn.commit()
    cursor.close()
    return new_doctor


def list() -> List[Doctor]:
    cursor = conn.cursor()
    query = "SELECT * FROM Doctor"
    cursor.execute(query)
    doctors = cursor.fetchall()
    cursor.close()
    res: List[Doctor] = []
    for doctor in doctors:
        d = Doctor(person_id=doctor[0],
                   first_name=doctor[1], last_name=doctor[2], phone=doctor[3], email=doctor[
                       4], job_title=doctor[5], office_number=doctor[6], salary=doctor[7]
                   )
        res.append(d)
    return res


def read_item(item_id: int):
    cursor = conn.cursor()
    query = "SELECT id, name, description FROM items WHERE id=%s"
    cursor.execute(query, (item_id,))
    item = cursor.fetchone()
    cursor.close()
    return {"id": item[0], "name": item[1], "description": item[2]}
