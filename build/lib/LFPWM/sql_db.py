import sqlite3


def create_connection():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    return conn, c


def create_tables():
    # creating two tables within the users.db
    conn, c = create_connection()
    # checking if the table already exists with sqlite_master
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Users'")
    # by capturing the fetch from the above execute we are able to check if the table exists
    table_exists = c.fetchone()
    if not table_exists:
        # creating the first table (Users) for user auth
        c.execute(
            """
        CREATE TABLE IF NOT EXISTS Users (
            user_id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
                  """
        )
    conn.commit()

    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='UserData'")
    table2_exists = c.fetchone()
    if not table2_exists:
        c.execute(
            """
        CREATE TABLE IF NOT EXISTS UserData (
            data_id INTEGER PRIMARY KEY,
            user_id INTEGER,
            title TEXT NOT NULL,
            data TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES Users(user_id)
        )
                  """
        )
    conn.commit()


create_tables()
