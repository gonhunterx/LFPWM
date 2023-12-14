import bcrypt
from LFPWM.sql_db import create_connection
from cryptography.fernet import Fernet

conn, c = create_connection()

key = Fernet.generate_key()
cipher_suite = Fernet(key)


class PasswordManager:
    @staticmethod
    def encrypt_password(password):
        if isinstance(password, str):
            password = password.encode()
        encrypted_password = cipher_suite.encrypt(password)
        return encrypted_password

    @staticmethod
    def decrypt_password(encrypted_password):
        decrypted_password = cipher_suite.decrypt(encrypted_password).decode()
        return decrypted_password


class User:
    def __init__(self, username, password):
        self.username = username
        self.password_manager = PasswordManager()
        self.password = self.password_manager.encrypt_password(password)

    def set_username(self, new_username):
        self.username = new_username
        c.execute(
            "UPDATE Users SET username = ? WHERE user_id = ?",
            (self.username, self.username),
        )
        conn.commit()

    def set_password(self, new_password):
        self.password = self.password_manager.encrypt_password(new_password)
        c.execute(
            "UPDATE Users SET password = ? WHERE user_id = ?",
            (self.password, self.username),
        )
        conn.commit()

    def insert_data(self, title, data):
        encrypted_data = self.password_manager.encrypt_password(data)
        c.execute(
            "INSERT INTO UserData (user_id, title, data) VALUES (?, ?, ?)",
            (self.username, title, encrypted_data),
        )
        conn.commit()

    def get_data(self):
        c.execute(
            "SELECT title, data FROM UserData WHERE user_id = ?", (self.username,)
        )
        rows = c.fetchall()
        for row in rows:
            decrypted_data = self.password_manager.decrypt_password(row[1])
            print(row[0], decrypted_data)

    def remove_data(self, data_to_delete):
        c.execute(
            "DELETE FROM UserData WHERE user_id = ? AND title = ?",
            (self.username, data_to_delete),
        )
        conn.commit()

    @staticmethod
    def hash_password(password):
        # Generate a salt and hash the password using bcrypt
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode(), salt)
        return hashed_password

    @staticmethod
    def verify_password(input_password, hashed_password):
        # Check if the input password matches the hashed password
        return bcrypt.checkpw(input_password.encode(), hashed_password)

    @staticmethod
    def register(username, password):
        c.execute("SELECT user_id FROM Users WHERE username = ?", (username,))
        existing_user = c.fetchone()
        if existing_user:
            print("Username already exists. Please choose a different username.")
            return None
        else:
            # Hash the password before storing it in the database
            hashed_password = User.hash_password(password)
            c.execute(
                "INSERT INTO Users (username, password) VALUES (?, ?)",
                (username, hashed_password),
            )
            conn.commit()
            print("Registration successful.")
            return User(username, hashed_password)

    @staticmethod
    def login(username, password):
        c.execute("SELECT user_id, password FROM Users WHERE username = ?", (username,))
        user_data = c.fetchone()
        if user_data and User.verify_password(password, user_data[1]):
            return User(username, user_data[1])
        else:
            print("Invalid username or password. Please try again.")
            return None
