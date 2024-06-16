from typing import Literal

import fastapi
import uvicorn

import src.app.routes
import src.crons.crons
import src.db.postgres.db

# class MyMiddleware:
#
#     async def __call__(self, request: Request, call_next):
#         # do something with the request object
#         print(await request.json())
#         print(json.loads(await request.json()))
#
#         # process the request and get the response
#         response = await call_next(request)
#
#         return response

app = fastapi.FastAPI()

# app.add_middleware(BaseHTTPMiddleware, dispatch=MyMiddleware())
db = src.db.postgres.db.PostgresDatabase(config=src.db.Database.Config(
    dbname="postgres",
    user="postgres",
    host="localhost",
    password=None
))
src.app.routes.register(app, db)

src.crons.crons.start_background_tasks(app, db)


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
