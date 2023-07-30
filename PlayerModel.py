from SqlModel import SqlModel


class PlayerModel(SqlModel):
    player_name: str

    def __init__(self, id: int, name: str):
        super().__init__(id)
        self.player_name = name

    def serialize_to_json(self):
        data = super().serialize_to_json()
        data["player_name"] = self.player_name
        return data

    def __str__(self):
        str(self.serialize_to_json())


