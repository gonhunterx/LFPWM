from sql_db import create_connection

conn, c = create_connection()


# when this executes it will show the encrypted password because it is stored
# that way.
c.execute("SELECT * FROM UserData")
rows = c.fetchall()
for row in rows:
    print(row)
