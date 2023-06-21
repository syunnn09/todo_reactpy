import sqlite3

# sql = '''
# CREATE TABLE todo(
#     todoId INTEGER PRIMARY KEY AUTOINCREMENT,
#     title TEXT NOT NULL,
#     isCompleted INTEGER NOT NULL DEFAULT 0,
#     isFavorite INTEGER NOT NULL DEFAULT 0,
#     createdAt TEXT
# );
# '''

sql = 'INSERT INTO todo(title, createdAt) VALUES(\'create todo app with reactpy\', \'2023-06-21 21:50:43\');'

conn = sqlite3.connect('todo.db')
cur = conn.cursor()

cur.execute(sql)
conn.commit()

cur.close()
conn.close()