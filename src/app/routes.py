import fastapi

import src.app.list_models
import src.app.register
import src.app.unregister
import src.db


def register(app: fastapi.FastAPI, db: src.db.Database):
    @app.get("/")
    async def index():
        return "this is model registry"

    app.include_router(src.app.register.Router(db).router)
    app.include_router(src.app.unregister.Router(db).router)
    app.include_router(src.app.list_models.Router(db).router)
