import abc

import arqanmode
import src.db.interface as interface


class Database(abc.ABC):

    @abc.abstractmethod
    def create_model(self, data: interface.CreateModelInput) -> arqanmode.ModelV1:
        pass

    @abc.abstractmethod
    def delete_model(self, data: interface.DeleteModelInput) -> None:
        pass

    @abc.abstractmethod
    def list_models(self) -> interface.ListModelsResponse:
        pass
