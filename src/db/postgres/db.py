import typing
from contextlib import contextmanager

import psycopg2.pool

import arqanmode
import src


class PostgresDatabase(src.db.Database):

    def exec(self, func):
        conn = psycopg2.connect(dbname=self.config.dbname,
                                user=self.config.user,
                                password=self.config.password,
                                host=self.config.host,
                                )

        with conn.conn.cursor() as curr:
            func(curr)

        conn.close()

    @contextmanager
    def db_cursor(self):
        conn = self.dbpool.getconn()
        try:
            with conn.cursor() as cur:
                yield cur
                conn.commit()
        except:
            conn.rollback()
            raise

        finally:
            self.dbpool.putconn(conn)

    def __init__(self, config: src.db.Database.Config):

        self.dbpool = psycopg2.pool.ThreadedConnectionPool(
            dbname=config.dbname,
            user=config.user,
            password=config.password,
            host=config.host,
            maxconn=10,
            minconn=2,
        )

        with self.db_cursor() as curr:
            curr.execute("create table if not exists models (name text primary key, interface jsonb)")

            curr.execute("select * from models")

    def create_model(self, data: src.db.interface.CreateModelInput) -> arqanmode.ModelV1:
        with self.db_cursor() as curr:
            curr.execute(
                "insert into models (name, interface) values (%s, %s) on conflict (name) do update set interface = excluded.interface",
                (data.model.model.model_name, data.model.json()))

        return data.model

    def delete_model(self, data: src.db.interface.DeleteModelInput) -> None:

        with self.db_cursor() as curr:
            curr.execute("delete from models where name = %s",
                         (data.model_name,))

        return

    def list_active_models(self) -> src.db.interface.ListModelsResponse:

        with self.db_cursor() as curr:
            curr.execute("select * from models where (interface->>'active')::bool = true")
            resp = curr.fetchall()

        return resp

    def pause_model(self, data: src.db.interface.PauseModelInput) -> None:

        with self.db_cursor() as curr:
            curr.execute(
                """update models set interface = jsonb_set(interface, '{"active"}', 'false', false) where name = %s""",
                (data.model_name,))

        return

    def unpause_model(self, data: src.db.interface.UnpauseModelInput) -> None:

        with self.db_cursor() as curr:
            curr.execute(
                """update models set interface = jsonb_set(interface, '{"active"}', 'true', false) where name = %s""",
                (data.model_name,))
        return
