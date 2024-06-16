import typing

import arqanmode
import src
from src.db.scheme import Model


class InMemoryDatabase(src.db.Database):
    def __init__(self, config: src.db.Database.Config):
        self.data: typing.Dict[str, Model] = dict()

    def create_model(self, data: src.db.interface.CreateModelInput) -> arqanmode.ModelV1:
        self.data[data.model.model.model_name] = data.model

        return data.model

    def delete_model(self, data: src.db.interface.DeleteModelInput) -> None:
        if data.model_name in self.data:
            del self.data[data.model_name]

        return

    def list_active_models(self) -> src.db.interface.ListModelsResponse:
        return src.db.interface.ListModelsResponse(
            models=list(filter(lambda x: x.active == True, self.data.values()))
        )

    def pause_model(self, data: src.db.interface.PauseModelInput) -> None:
        if data.model_name in self.data:
            self.data[data.model_name].active = False

        return

    def unpause_model(self, data: src.db.interface.UnpauseModelInput) -> None:
        if data.model_name in self.data:
            self.data[data.model_name].active = True

        return
