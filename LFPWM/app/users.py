from app.sql_db import create_connection
from cryptography.fernet import Fernet

conn, c = create_connection()

key = Fernet.generate_key()
cipher_suite = Fernet(key)


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def set_username(self, new_username):
        new_username = self.username
        c.execute(
            "UPDATE Users SET username = ? WHERE user_id = ?",
            (new_username, self.username),
        )
        conn.commit()

    def set_password(self, new_password):
        new_password = self.password
        c.execute(
            "UPDATE Users SET password = ? WHERE user_id = ?",
            (new_password, self.username),
        )
        conn.commit()

    # use the password encryption methods on the data to encrypt it while stored.
    def insert_data(self, title, data):
        encrypted_data = encrypt_password(data)
        c.execute(
            "INSERT INTO UserData (user_id, title, data) VALUES (?, ?, ?)",
            # pass in the now encrypted data to the data row with the title
            (self.username, title, encrypted_data),
        )
        conn.commit()

    def get_data(self):
        c.execute(
            "SELECT title, data FROM UserData WHERE user_id = ?", (self.username,)
        )
        rows = c.fetchall()
        # decrypt the password to view it
        for row in rows:
            decrypted_data = decrypt_password(row[1])
            print(row[0], decrypted_data)

    def remove_data(self, data_to_delete):
        # try:
        c.execute(
            "DELETE FROM UserData WHERE user_id = ? AND title = ?",
            (self.username, data_to_delete),
        )
        # except Exception as e:
        #     print(f"Error at {e}")
        conn.commit()

    @staticmethod
    def login(username, password):
        c.execute(
            "SELECT user_id FROM Users WHERE username = ? AND password = ?",
            (username, password),
        )
        user_id = c.fetchone()
        if user_id:
            return user_id[0]
        else:
            return None
        # print("User id not found")


# create functions that will encrypt and decrypt a password
def encrypt_password(password):
    encrypted_password = cipher_suite.encrypt(password.encode())
    return encrypted_password


def decrypt_password(encrypted_password):
    decrypted_password = cipher_suite.decrypt(encrypted_password).decode()
    return decrypted_password
