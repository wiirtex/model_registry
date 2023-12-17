import fastapi

import src.db
import src.models.scheme


class Router:

    def __init__(self, db: src.db.Database):
        self.db = db

        self.router = fastapi.APIRouter(
            prefix="/list",
            tags=["list"],
        )

        self.router.add_api_route(path='/',
                                  endpoint=self.endpoint,
                                  methods=['get'])
        pass

    async def endpoint(self):
        resp = self.db.list_models()

        return resp
