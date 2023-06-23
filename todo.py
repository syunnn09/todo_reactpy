from reactpy import component, html, hooks
from reactpy.backend.fastapi import configure, Options
from uvicorn import run
from fastapi import FastAPI

import utils.dbutils as dbutils

from header import Head
from components.input import Input
from components.task import Task

@component
def Todo():
    tasks, set_tasks = hooks.use_state([])
    popup, set_popup = hooks.use_state(None)

    def get_tasks():
        _, cur = dbutils.connect()
        result = cur.execute('SELECT todoId, title, isCompleted, isFavorite, createdAt FROM todo')
        set_tasks(list(map(create_tasks, result)))

    def create_tasks(tup: tuple):
        return Task(tup, set_popup)

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
        ),
        (popup if popup is not None else '')
    )

app = FastAPI()
configure(
    app,
    Todo,
    Options(head=Head())
)
# run(app, host='127.0.0.1', port=8001)