class RoomType:
    type_id: int
    type_description: str

    def __init__(self, type_description):
        self.type_description = type_description

    def display_info(self):
        print(f"Description: {self.type_description}")
