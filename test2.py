import sqlite3

conn = sqlite3.connect('test.db')
cur = conn.cursor()

addColumn = "ALTER TABLE Players ADD COLUMN points INTEGER"
cur.execute(addColumn)



