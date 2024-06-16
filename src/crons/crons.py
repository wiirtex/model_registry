import threading

import fastapi
import multiprocess as mp
import requests
import time

import src.db
from src.db.interface import PauseModelInput

started = False


def start_background_tasks(app: fastapi.FastAPI, db: src.db.Database):
    global started

    with threading.Lock():
        if started:
            return
        else:
            started = True

    print(requests.request('get', 'http://google.com'))

    proc = mp.Process(target=background_tasks, args=(app, db,), kwargs={}, daemon=True)
    proc.start()

    pass


def background_tasks(app: fastapi.FastAPI, db: src.db.Database):
    while True:
        time.sleep(15)

        check_active_models(app, db)


def check_active_models(app: fastapi.FastAPI, db: src.db.Database):
    models = db.list_active_models()
    for model in models:
        model = model[1]
        if model['port'] != '':
            url = f'http://localhost:{model['port']}/status/'
            response = None
            try:
                response = requests.request('GET', url)
            except Exception as e:
                print(e)

            if response is None or response.status_code != 200:
                db.pause_model(PauseModelInput(
                    model_name=model['model']['model_name'],
                ))
                print(f"model {model['model']['model_name']} is deactivated")

    print("check_active_models is passed")
