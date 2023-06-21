from reactpy import component, html
from reactpy.backend.fastapi import configure
from uvicorn import run
from fastapi import FastAPI
import sqlite3

from components.input import Input
from components.task import Task

@component
def Todo():
    def create_tasks(tup: tuple):
        return Task(tup)
    conn = sqlite3.connect('todo.db')
    cur = conn.cursor()
    result = cur.execute('SELECT todoId, title, isCompleted, isFavorite, createdAt FROM todo')
    tasks = map(create_tasks, result)

    return html.div(
        Input(),
        html.div(tasks)
    )

app = FastAPI()
configure(app, Todo)
run(app, host='127.0.0.1', port=8001)