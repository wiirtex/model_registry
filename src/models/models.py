import pydantic

import src.models.scheme


class RegisterInput(pydantic.BaseModel):
    model_name: str
    scheme: src.models.scheme.SchemeV1

    @pydantic.model_validator(mode='before')
    @classmethod
    def check_not_none(cls, data):
        if isinstance(data, dict):
            assert ('scheme' in data), "field scheme must not be omitted"
        return data


class UnregisterInput(pydantic.BaseModel):
    name: str
