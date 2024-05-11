import fastapi

import src.db
import src.models.models
from src.db.interface import PauseModelInput


class Router:

    def __init__(self, db: src.db.Database):
        self.db = db

        self.router = fastapi.APIRouter(
            prefix="/pause_tasks_creation",
            tags=["tasks creation"],
        )

        self.router.add_api_route(path='/',
                                  endpoint=self.endpoint,
                                  methods=['post'])
        pass

    async def endpoint(self, req: src.models.models.PauseModelInput):
        self.db.pause_model(PauseModelInput(
            model_name=req.name,
        ))
