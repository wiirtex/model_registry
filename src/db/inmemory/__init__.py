import typing

import src.models.scheme


class InMemoryDatabase(src.db.Database):
    def __init__(self):
        self.data: typing.Dict[str, src.models.scheme.ModelV1] = dict()

    def create_model(self, data: src.db.interface.CreateModelInput) -> src.models.scheme.ModelV1:
        self.data[data.model.name] = data.model

        return data.model

    def delete_model(self, data: src.db.interface.DeleteModelInput) -> None:
        if data.model_name in self.data:
            del self.data[data.model_name]

        return

    def list_models(self) -> typing.List[src.models.scheme.ModelV1]:
        return list(self.data.values())
