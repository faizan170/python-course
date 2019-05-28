import sqlite3

conn  = sqlite3.connect("test.db")

cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, name VARCHAR(50))")
cur.execute("INSERT INTO test (name) VALUES ('Faizan')")
conn.commit()
res = cur.execute("SELECT * FROM test")

for row in res:
    print(row)

conn.close()