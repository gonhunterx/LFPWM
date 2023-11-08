from app.sql_db import create_connection, create_database, create_users_data_table
from app.users import User
from app.home import home_page

conn, c = create_connection()


def login():
    print("Please log in 😊")
    username = input("Username: ")
    password = input("Password: ")
    # use the static method from User class to verify
    user_id = User.login(username, password)

    if user_id:
        print("Login successful! User ID:", user_id)
        user = User(username, password)
    else:
        print("Invalid username or password. Please try again. ")
        main()
    home_page(user)


def register():
    print("Please create an account 😊")
    username = input("Username: ")
    c.execute("SELECT user_id FROM Users WHERE username = ?", (username,))
    existing_user = c.fetchone()
    if existing_user:
        print("This username is already in use. Please use another.")
    else:
        password = input("Password: ")
        c.execute(
            "INSERT INTO Users(username, password) VALUES (?, ?)", (username, password)
        )
        conn.commit()
        print("Account created successfully!")


def main_menu():
    print(
        """
1. Login
2. Register
3. Exit
          """
    )
    choice = input("Input: ")
    return choice


def main():
    try:
        print("=======================")
        print("Welcome to LamaForge PW Manager")
        create_database()
        while True:
            login_menu_choice = main_menu()
            if login_menu_choice == "1":
                login()
            elif login_menu_choice == "2":
                register()
            elif login_menu_choice == "3":
                conn.close()  # Close the connection before exiting
                break
            else:
                print("Invalid input. Please input 1, 2, or 3.")
    finally:
        conn.close()


if __name__ == "__main__":
    create_users_data_table()
    main()
