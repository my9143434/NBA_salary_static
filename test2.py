import sqlite3


def add_cloumn():
    addColumn = "ALTER TABLE Players ADD COLUMN efficiency FLOAT"
    cur.execute(addColumn)


conn = sqlite3.connect('test.db')
cur = conn.cursor()

cur.execute('SELECT name FROM Players')
results1 = cur.fetchall()
print(results1)
for name in results1:
    print(name[0])
