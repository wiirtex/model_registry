import fastapi

import src.db
import src.models.models
import src.models.scheme


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

    async def endpoint(self, req: src.models.models.RegisterInput):
        print(type(req), req)

        inp = src.db.interface.CreateModelInput.model_validate({
            'model': {
                'name': req.model_name,
                'scheme': req.scheme
            }
        })
        resp = self.db.create_model(inp)

        return resp
