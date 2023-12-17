from src.utils.database import conn
from models.room_type import Room_Type


def new_room_type(new_room_type: Room_Type):
    cursor = conn.cursor()
    query = "INSERT INTO RoomType (TypeDescription) VALUES (%s)"
    cursor.execute(query, (new_room_type.type_description,))
    conn.commit()
    cursor.close()
    return new_room_type


r1 = Room_Type(type_description="room2")
new_room_type(r1)
