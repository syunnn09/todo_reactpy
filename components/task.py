from reactpy import component, html, hooks

from components.input import Input
from components.checkbox import Checkbox
from components.trash_can import Trush_can
from styles import *
import exhtml
import utils.dbutils as dbutils
from utils.popuputils import PopupYesNo


def set_favorite(is_favorite: int, todo_id: int):
    conn, cur = dbutils.connect()
    cur.execute('UPDATE todo SET isFavorite=? WHERE todoId=?', (is_favorite, todo_id))
    dbutils.close(conn, cur)

def set_completed(is_completed: int, todo_id: int):
    conn, cur = dbutils.connect()
    cur.execute('UPDATE todo SET isCompleted=? WHERE todoId=?', (is_completed, todo_id))
    dbutils.close(conn, cur)

def set_db_title(title: int, todo_id: int):
    conn, cur = dbutils.connect()
    cur.execute('UPDATE todo SET title=? WHERE todoId=?', (title, todo_id))
    dbutils.close(conn, cur)

@component
def Task(tup: tuple, set_popup):
    todo_id, title, is_completed, is_favorite, created_at = tup

    def get_default_title_label():
        return html.p({ 'style': 'cursor: pointer;' }, title)

    title, set_title = hooks.use_state(title)
    is_favorite, set_is_favorite = hooks.use_state(is_favorite)
    is_completed, set_is_completed = hooks.use_state(is_completed)
    title_label, set_title_label = hooks.use_state(get_default_title_label())

    def reverse_value(value, func):
        if value == 0:
            value = 1
        else:
            value = 0
        func(value)
        return value

    def delete_task(e):
        conn, cur = dbutils.connect()
        cur.execute('DELETE FROM todo WHERE todoId=?', (todo_id, ))
        dbutils.close(conn, cur)
        set_popup(None)

    def close_popup(e):
        set_popup(None)

    def on_delete():
        set_popup(lambda e: PopupYesNo('削除してもよろしいですか？', delete_task, close_popup))

    def create_star_svg():
        if is_favorite:
            return html.svg(
                {
                    'xmlns': "http://www.w3.org/2000/svg",
                    'viewBox': '-100 -100 200 200',
                    'width': '30',
                    'height': '30',
                },
                exhtml.polygon(
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
                exhtml.polygon(
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

    def edit_title(value):
        set_db_title(value, todo_id)
        set_title(value)
        set_title_label(get_default_title_label())

    def edit(e):
        set_title_label(Input(edit_title, value=title))

    return html.div(
        { 'style': center() },
        Checkbox(
            is_completed,
            lambda e: set_completed(reverse_value(is_completed, set_is_completed), todo_id),
            margin='0 0.5rem'
        ),
        html.div(
            {
                'on_click': edit,
                'class': 'task',
                'style': 'margin: 0 0.5rem; width: 50%; overflow: hidden;'    
            },
            title_label
        ),
        html.div(
            {
                'on_click': lambda e: set_favorite(reverse_value(is_favorite, set_is_favorite), todo_id),
                'style': 'margin: 0 0.5rem; height: 30px; cursor: pointer;'
            },
            create_star_svg()
        ),
        Trush_can(on_delete, margin='0 0.5rem', width='25px', height='25px'),
    )
