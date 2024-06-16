import fastapi
from starlette.requests import Request

import src.db
import src.models.models


class Router:

    def __init__(self, db: src.db.Database):
        self.db = db

        self.router = fastapi.APIRouter(
            prefix="/unregister",
            tags=["unregister"],
        )

        self.router.add_api_route(path='/',
                                  endpoint=self.endpoint,
                                  methods=['post'])
        pass

    async def endpoint(self, req: Request):
        req = src.db.interface.DeleteModelInput.model_validate(await req.json())

        inp = src.db.interface.DeleteModelInput.model_validate({
            'model_name': req.model_name
        })
        self.db.delete_model(inp)
