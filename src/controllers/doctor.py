from models.doctor import Doctor
from src.utils.database import conn


def new_doctor(new_doctor: Doctor):
    cursor = conn.cursor()
    query = "INSERT INTO Doctor (DoctorID, FirstName, LastName, PhoneNumber, EmailAddress, JobTitle, OfficeNumber,Salary) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(query, (new_doctor.id, new_doctor.first_name,))
    conn.commit()
    cursor.close()
    return new_doctor
