import pydantic

import src.models.scheme


class CreateModelInput(pydantic.BaseModel):
    model: src.models.scheme.ModelV1

    @pydantic.model_validator(mode='before')
    @classmethod
    def check_not_none(cls, data):
        if isinstance(data, dict):
            assert ('model' in data), "field scheme must not be omitted"
        return data


class DeleteModelInput(pydantic.BaseModel):
    model_name: str
