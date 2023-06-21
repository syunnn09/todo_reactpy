from reactpy import component, html, hooks
import sqlite3

from components.checkbox import Checkbox
from styles import *

def connect():
    conn = sqlite3.connect('todo.db')
    cur = conn.cursor()
    return conn, cur

def close(conn: sqlite3.Connection, cur: sqlite3.Cursor):
    conn.commit()
    cur.close()
    conn.close()

def set_favorite(is_favorite: int, todo_id: int):
    conn, cur = connect()
    cur.execute('UPDATE todo SET isFavorite=? WHERE todoId=?', (is_favorite, todo_id))
    close(conn, cur)

def set_completed(is_completed: int, todo_id: int):
    conn, cur = connect()
    cur.execute('UPDATE todo SET isCompleted=? WHERE todoId=?', (is_completed, todo_id))
    close(conn, cur)

@component
def Task(tup: tuple):
    todo_id, title, is_completed, is_favorite, created_at = tup

    is_favorite, set_is_favorite = hooks.use_state(is_favorite)
    is_completed, set_is_completed = hooks.use_state(is_completed)

    def reverse_favorite(is_favorite):
        if is_favorite == 0:
            is_favorite = 1
        else:
            is_favorite = 0
        set_is_favorite(is_favorite)
        return is_favorite

    def reverse_completed(is_completed):
        if is_completed == 0:
            is_completed = 1
        else:
            is_completed = 0
        set_is_completed(is_completed)
        return is_completed

    def create_star_svg():
        if is_favorite:
            return html.svg(
                {
                    'xmlns': "http://www.w3.org/2000/svg",
                    'viewBox': '-100 -100 200 200',
                    'width': '30',
                    'height': '30',
                },
                html.polygon(
                    {
                        'points': '0,-100 29.39,-40.45 95.11,-30.9 47.55,15.45 58.78,80.90 0,50 -58.78,80.9 -47.55,15.45 -95.11,-30.9 -29.39,-40.45',
                        'fill': '#faf' if is_favorite else '#fff'
                    }
                )
            )
        else:
            return html.svg(
                {
                    'xmlns': "http://www.w3.org/2000/svg",
                    'viewBox': '0 0 48 48',
                    'width': '30',
                    'height': '30',
                },
                html.polygon(
                    {
                        'points': '23.98 5 29.85 16.9 42.98 18.8 33.48 28.07 35.72 41.14 23.98 34.97 12.24 41.14 14.48 28.07 4.98 18.8 18.11 16.9 23.98 5',
                        'fill': 'none',
                        'stroke': '#faf',
                        'stroke-linecap': 'round',
                        'stroke-linejoin': 'round',
                        'stroke-width': '2',
                    }
                )
            )

    return html.div(
        { 'style': center() },
        Checkbox(
            is_completed,
            lambda e: set_completed(reverse_completed(is_completed), todo_id)
        ),
        html.div(
            { 'class': 'task' },
            title
        ),
        html.div(
            {
                'on_click': lambda e: set_favorite(reverse_favorite(is_favorite), todo_id),
                'cursor': 'pointer',
                'style': 'height: 30px;'
            },
            create_star_svg()
        )
    )
