import typing

import arqanmode
import src


class InMemoryDatabase(src.db.Database):
    def __init__(self):
        self.data: typing.Dict[str, arqanmode.ModelV1] = dict()

    def create_model(self, data: src.db.interface.CreateModelInput) -> arqanmode.ModelV1:
        self.data[data.model.model_name] = data.model

        return data.model

    def delete_model(self, data: src.db.interface.DeleteModelInput) -> None:
        if data.model_name in self.data:
            del self.data[data.model_name]

        return

    def list_models(self) -> src.db.interface.ListModelsResponse:
        return src.db.interface.ListModelsResponse(
            models=list(self.data.values())
        )
