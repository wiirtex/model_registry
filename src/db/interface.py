import typing

import pydantic

from src.db.scheme import Model


class ListModelsResponse(pydantic.BaseModel):
    models: typing.List[Model]


class CreateModelInput(pydantic.BaseModel):
    model: Model

    @classmethod
    @pydantic.model_validator(mode='before')
    def check_not_none(cls, data):
        if isinstance(data, dict):
            assert ('model' in data), "field scheme must not be omitted"
        return data


class DeleteModelInput(pydantic.BaseModel):
    model_name: str


class PauseModelInput(pydantic.BaseModel):
    model_name: str


class UnpauseModelInput(pydantic.BaseModel):
    model_name: str
