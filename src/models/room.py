from src.models.model import Model


class Room(Model):
    room_number: int
    type_id: int

    @staticmethod
    def relation_attribute_name() -> dict:
        return Model.relation_attribute_name() | {
            'RoomNumber': 'room_number',
            'TypeID': 'type_id'
        }

    def __init__(self, room_id: int | None, room_number: int, type_id: int) -> None:
        super().__init__(room_id)
        self.room_number = room_number
        self.type_id = type_id

    def __str__(self):
        return f"{super().__str__()}, Room Number: {self.room_number}, Room Type ID: {self.type_id}"

    def __dict__(self) -> dict:
        return {
            'ID': self.id,
            'RoomNumber': self.room_number,
            'TypeID': self.type_id,
        }
