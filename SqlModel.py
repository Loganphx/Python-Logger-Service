from abc import ABC, abstractmethod


class SqlModel(ABC):
    id: int

    @abstractmethod
    def __init__(self, id: int):
        self.id = id

    @abstractmethod
    def serialize_to_json(self):
        return {"id": str(self.id)}

    @abstractmethod
    def __str__(self):
        str(self.serialize_to_json())

