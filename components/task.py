from reactpy import component, html, hooks

from components.input import Input
from components.checkbox import Checkbox
from components.trash_can import Trush_can
from styles import *

import utils.dbutils as dbutils
from utils.popuputils import PopupYesNo
from utils.styleutils import create_star_svg
from utils.commonutils import reverse_value


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

    def delete_task(e):
        conn, cur = dbutils.connect()
        cur.execute('DELETE FROM todo WHERE todoId=?', (todo_id, ))
        dbutils.close(conn, cur)
        set_popup(None)

    def close_popup(e):
        set_popup(None)

    def on_delete():
        set_popup(lambda e: PopupYesNo('削除してもよろしいですか？', delete_task, close_popup))

    def edit_title(value):
        set_db_title(value, todo_id)
        set_title(value)
        set_title_label(get_default_title_label())

    def edit(e):
        set_title_label(Input(edit_title, value=title))

    return html.div(
        { 'style': center() },
        html.div(
            { 'style': center() + 'width: 100%;' },
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
                create_star_svg(is_favorite)
            ),
            Trush_can(on_delete, margin='0 0.5rem', width='25px', height='25px'),
        )
    )
