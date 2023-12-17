# from src.models.doctor import Room
# from src.utils.database import conn


# def new_doctor(new_room: Room):
#     cursor = conn.cursor()
#     query = "INSERT INTO Room (FirstName, LastName, PhoneNumber, EmailAddress, JobTitle, OfficeNumber,Salary) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
#     cursor.execute(query, (new_room.id, new_room.first_name,))
#     conn.commit()
#     cursor.close()
#     return new_doctor
