import pydantic

import arqanmode


class RegisterInput(pydantic.BaseModel):
    model_name: str
    scheme: arqanmode.SchemeV1

    @classmethod
    @pydantic.model_validator(mode='before')
    def check_not_none(cls, data):
        if isinstance(data, dict):
            assert ('scheme' in data), "field scheme must not be omitted"
        return data


class UnregisterInput(pydantic.BaseModel):
    name: str
