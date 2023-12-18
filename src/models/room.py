class Room:
    room_id:int
    room_number: int
    room_capacity: int
    room_type_id: int

    def __init__(self, room_number: int, room_capacity: int, room_type_id: int) -> None:
        self.room_number = room_number
        self.room_capacity = room_capacity
        self.room_type_id = room_type_id

    def display_info(self):
        print(f"Room Number: {self.room_number}, Capacity: {self.room_capacity}, Type ID: {self.room_type_id}")
