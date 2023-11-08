from app.sql_db import create_connection

conn, c = create_connection()

c.execute("SELECT * FROM UserData")
rows = c.fetchall()
for row in rows:
    print(row)
