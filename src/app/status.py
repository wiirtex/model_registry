import fastapi

import src.db


class Router:

    def __init__(self, db: src.db.Database):
        self.db = db

        self.router = fastapi.APIRouter(
            prefix="/status",
            tags=["status"],
        )

        self.router.add_api_route(path='/',
                                  endpoint=self.endpoint,
                                  methods=['get'])
        pass

    async def endpoint(self):
        return {
            "status": "ok"
        }
