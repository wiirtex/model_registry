import typing

import pydantic

import arqanmode


class ListModelsResponse(pydantic.BaseModel):
    models: typing.List[arqanmode.ModelV1]


class CreateModelInput(pydantic.BaseModel):
    model: arqanmode.ModelV1

    @classmethod
    @pydantic.model_validator(mode='before')
    def check_not_none(cls, data):
        if isinstance(data, dict):
            assert ('model' in data), "field scheme must not be omitted"
        return data


class DeleteModelInput(pydantic.BaseModel):
    model_name: str
