import sqlite3


def create_connection():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    return conn, c


def create_database():
    conn, c = create_connection()
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
    table_exsits = c.fetchone()
    if not table_exsits:
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


def create_users_data_table():
    conn, c = create_connection()
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='UserData'")
    table_exists = c.fetchone()
    if not table_exists:
        c.execute(
            """
        CREATE TABLE IF NOT EXISTS UserData (
            data_id INTEGER PRIMARY KEY,
            user_id INTEGER,
            title TEXT,
            data TEXT,
            FOREIGN KEY (user_id) REFERENCES Users(user_id)
        )
                  """
        )
    conn.commit()
