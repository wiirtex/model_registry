import pydantic

import arqanmode


class Model(pydantic.BaseModel):
    model: arqanmode.ModelV1
    active: bool
