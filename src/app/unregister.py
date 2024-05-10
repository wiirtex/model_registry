import fastapi

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

    async def endpoint(self, req: src.models.models.UnregisterInput):
        print(type(req), req)

        inp = src.db.interface.DeleteModelInput.model_validate({
            'model_name': req.name
        })
        resp = self.db.delete_model(inp)

        return resp
