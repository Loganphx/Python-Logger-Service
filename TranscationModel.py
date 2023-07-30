from SqlModel import SqlModel


class TranscationModel(SqlModel):
    give_gem: str
    take_gem: str
    maker: str
    taker: str

    def __init__(self, id: int, give_gem: str, take_gem: str, maker: str, taker: str):
        super().__init__(id)
        self.give_gem = give_gem
        self.take_gem = take_gem
        self.maker = maker
        self.taker = taker

    def serialize_to_json(self):
        data = super().serialize_to_json()
        data["give_gem"] = self.give_gem
        data["take_gem"] = self.take_gem
        data["maker"] = self.maker
        data["taker"] = self.taker
        return data

    def __str__(self):
        str(self.serialize_to_json())


class WETHModel(TranscationModel):
    def eat(self):
        pass

    def serialize_to_json(self):
        return super().serialize_to_json()

    def __init__(self, id: int, give_gem: str, take_gem: str, maker: str, taker: str):
        super().__init__(id, give_gem, take_gem, maker, taker)

    def __str__(self):
        str(self.serialize_to_json())
