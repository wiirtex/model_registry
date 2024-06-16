import fastapi

import src.db


def start_background_tasks(app: fastapi.FastAPI, db: src.db.Database):
    # while True:
    #     check_active_models(app, db)
    #
    #     time.sleep(5)

    pass


def check_active_models(app: fastapi.FastAPI, db: src.db.Database):
    models = db.list_active_models()
