import sqlite3
from typing import Tuple
import datetime


def connect() -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    conn = sqlite3.connect('todo.db')
    cur = conn.cursor()
    return conn, cur

def close(conn: sqlite3.Connection, cur: sqlite3.Cursor) -> None:
    conn.commit()
    cur.close()
    conn.close()

def get_now_time() -> str:
    now = datetime.datetime.now()
    return now.strftime('%Y/%m/%d %H:%M%S')
