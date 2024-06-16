import json

import fastapi
from starlette.requests import Request

import src.db
import src.models.models


class Router:

    def __init__(self, db: src.db.Database):
        self.db = db

        self.router = fastapi.APIRouter(
            prefix="/register",
            tags=["register"],
        )

        self.router.add_api_route(path='/',
                                  endpoint=self.endpoint,
                                  methods=['post'])
        pass

    async def endpoint(self, req: Request):
        # : src.models.models.RegisterInput
        # print(type(req), req)

        req = src.models.models.RegisterInput.model_validate(json.loads(await req.json()))

        inp = src.db.interface.CreateModelInput.model_validate({
            'model': {
                'model': {
                    'model_name': req.model_name,
                    'scheme': req.scheme
                },
                'active': True,
            }
        })
        resp = self.db.create_model(inp)

        return resp
