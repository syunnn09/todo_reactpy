from reactpy import component, html, hooks
from reactpy.backend.fastapi import configure
from uvicorn import run
from fastapi import FastAPI

import utils.dbutils as dbutils
from components.input import Input
from components.task import Task

@component
def Todo():
    tasks, set_tasks = hooks.use_state([])

    def get_tasks():
        _, cur = dbutils.connect()
        result = cur.execute('SELECT todoId, title, isCompleted, isFavorite, createdAt FROM todo')
        set_tasks(list(map(create_tasks, result)))

    def create_tasks(tup: tuple):
        return Task(tup)

    def add_todo(value):
        conn, cur = dbutils.connect()
        cur.execute('INSERT INTO todo(title, createdAt) VALUES(?, ?);', (value, dbutils.get_now_time()))
        conn.commit()
        dbutils.close(conn, cur)
        get_tasks()

    get_tasks()
    # tasks = sorted(tasks, key=lambda x: x._args[0][4])
    return html.div(
        Input(add_todo),
        html.div(
            { 'style': 'width: 100%; margin-top: 2rem;' },
            tasks
        )
    )

app = FastAPI()
configure(app, Todo)
# run(app, host='127.0.0.1', port=8001)