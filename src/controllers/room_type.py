from src.utils.database import conn
from models.room_type import RoomType


def new_room_type(new_room_type: RoomType):
    cursor = conn.cursor()
    query = "INSERT INTO RoomType (TypeDescription) VALUES (%s)"
    cursor.execute(query, (new_room_type.type_description,))
    conn.commit()
    cursor.close()
    return new_room_type


r1 = RoomType(type_description="room2")
new_room_type(r1)
