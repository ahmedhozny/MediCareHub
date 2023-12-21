from src.models.model import Model


class RoomType(Model):
    type_description: str

    @staticmethod
    def relation_attribute_name() -> dict:
        return Model.relation_attribute_name() | {
            'TypeDescription': 'type_description'
        }

    def __init__(self, type_id: int | None, type_description):
        super().__init__(type_id)
        self.type_description = type_description

    def __str__(self):
        return f"{super().__str__()}, Description: {self.type_description}"

    def __dict__(self) -> dict:
        return {
            'ID': self.id,
            'TypeDescription': self.type_description
        }
