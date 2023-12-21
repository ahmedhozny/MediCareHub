from abc import ABC, abstractmethod


class Model(ABC):
    __id: int | None

    id_name = None

    @staticmethod
    def relation_attribute_name() -> dict:
        return {'ID': 'id'}

    @classmethod
    def id_attr_name(cls):
        return cls.id_name

    def __init__(self, id: int | None):
        self.__id = id

    @property
    def id(self) -> int:
        return self.__id

    def __str__(self) -> str:
        return f'ID: {self.__id}'

    def __dict__(self) -> dict:
        return {'ID': self.id}

    def update(self, **kwargs) -> None:
        for key, value in kwargs.items():
            key = self.relation_attribute_name()[key]
            if hasattr(self, key):
                print(key, value)
                setattr(self, key, value)

    def display_info(self):
        print(self.__str__())
