from LFPWM.sql_db import create_connection
from cryptography.fernet import Fernet

conn, c = create_connection()

key = Fernet.generate_key()
cipher_suite = Fernet(key)


# PasswordManager is a class used within the User class for its static methods.
# you can also create an instance of it and use its methods for creating your own variables.
class PasswordManager:
    @staticmethod
    def encrypt_password(password):
        encrypted_password = cipher_suite.encrypt(password.encode())
        return encrypted_password

    @staticmethod
    def decrypt_password(encrypted_password):
        decrypted_password = cipher_suite.decrypt(encrypted_password).decode()
        return decrypted_password


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        # creating an instance to use in the class of the PWM class
        self.password_manager = PasswordManager()

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

    def insert_data(self, title, data):
        encrypted_data = self.password_manager.encrypt_password(data)
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
            decrypted_data = self.password_manager.decrypt_password(row[1])
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
