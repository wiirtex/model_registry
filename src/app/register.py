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

    async def endpoint(self, request: Request):
        req = src.models.models.RegisterInput.model_validate(json.loads(await request.json()))

        origin_url = dict(request.headers).get(b"host", b"").decode()
        print(origin_url)

        inp = src.db.interface.CreateModelInput.model_validate({
            'model': {
                'model': {
                    'model_name': req.model_name,
                    'scheme': req.scheme
                },
                'active': True,
                'url': origin_url
            }
        })
        resp = self.db.create_model(inp)

        return resp
