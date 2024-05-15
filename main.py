from typing import Literal

import fastapi
import uvicorn

import src.app.routes
import src.db.inmemory.db

app = fastapi.FastAPI()
db: src.db.Database = src.db.inmemory.db.InMemoryDatabase()
src.app.routes.register(app, db)


def main():
    start_server(num_workers=1, reload=False, host='0.0.0.0')


def start_server(host='127.0.0.1', port=8000, num_workers=4,
                 loop: Literal["none", "auto", "asyncio", "uvloop"] = 'auto', reload=False):
    uvicorn.run('main:app', host=host,
                port=port,
                workers=num_workers,
                loop=loop,
                reload=reload)


if __name__ == '__main__':
    main()
