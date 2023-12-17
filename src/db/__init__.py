import abc
import typing

import src.db.interface
import src.models.scheme


class Database(abc.ABC):

    @abc.abstractmethod
    def create_model(self, data: interface.CreateModelInput) -> src.models.scheme.ModelV1:
        pass

    @abc.abstractmethod
    def delete_model(self, data: interface.DeleteModelInput) -> None:
        pass

    @abc.abstractmethod
    def list_models(self) -> typing.List[src.models.scheme.ModelV1]:
        pass
