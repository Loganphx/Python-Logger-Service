from SqlModel import SqlModel


class AnimalModel(SqlModel):
    animal_type: str

    def __init__(self, id: int, name: str):
        super().__init__(id)
        self.animal_type = name

    def serialize_to_json(self):
        data = super().serialize_to_json()
        data["animal_type"] = str(self.animal_type)
        return data

    def __str__(self):
        str(self.serialize_to_json())


