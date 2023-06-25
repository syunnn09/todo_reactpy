from reactpy import component, html, hooks
from reactpy.backend.fastapi import configure, Options
from uvicorn import run
from fastapi import FastAPI

import utils.dbutils as dbutils

from header import Head
from styles import center
from const import Sort_Type
from components.input import Input
from components.task import Task
from components.option import Option


def add_todo(value):
    conn, cur = dbutils.connect()
    cur.execute('INSERT INTO todo(title, createdAt) VALUES(?, ?);', (value, dbutils.get_now_time()))
    conn.commit()
    dbutils.close(conn, cur)


@component
def Todo():
    tasks, set_tasks = hooks.use_state([])
    popup, set_popup = hooks.use_state(None)
    sort, set_sort = hooks.use_state(Sort_Type.作成日.value)

    def get_tasks():
        conn, cur = dbutils.connect()
        result = cur.execute(f'SELECT todoId, title, isCompleted, isFavorite, createdAt FROM todo ORDER BY {sort}')
        set_tasks(list(map(create_tasks, result)))
        dbutils.close(conn, cur)

    def create_tasks(tup: tuple):
        return Task(tup, set_popup)

    def on_click_select(e):
        if e['button'] == -1:
            value = e['currentTarget']['value']
            set_sort(Sort_Type[value].value)

    def create_select():
        options = [Option(e.name, lambda e: print(e)) for e in Sort_Type]
        return html.select({ 'on_click': lambda e: on_click_select(e) }, options)

    get_tasks()
    return html.div(
        Input(add_todo),
        html.div(
            { 'style': center() + 'flex-direction: column; margin-top: 2rem; width: 100%;' },
            html.div(
                { 'style': 'width: 100%; margin-right: 40%;' },
                html.div(
                    { 'style': 'display: flex; justify-content: flex-end;' },
                    html.div(create_select())
                )
            ),
            html.div(
                { 'style': 'display: flex; width: 100%; margin-top: 1rem;' },
                html.div({ 'style': 'flex: 1;' }, tasks)
            )
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