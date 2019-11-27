import sqlite3

conn = sqlite3.connect('test.db')
cur = conn.cursor()

cur.execute('SELECT name FROM Players')
results1 = cur.fetchall()
print(results1)
for name in results1:
    print(name[0])



# addColumn = "ALTER TABLE Players ADD COLUMN points INTEGER"
# cur.execute(addColumn)



