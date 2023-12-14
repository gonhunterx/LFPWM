from LFPWM.users import User

if __name__ == "__main__":
    # Register a new user
    user = User.register("john_doe", "secure_password")

    if user:
        # Log in with the registered user
        logged_in_user = User.login("john_doe", "secure_password")

        if logged_in_user:
            # Insert some password data
            logged_in_user.insert_data("Email", "john_doe@example.com")
            logged_in_user.insert_data("Bank", "1234")

            # View stored password data
            print("Stored password data:")
            logged_in_user.get_data()

            # Remove password data
            logged_in_user.remove_data("Bank")

            # View updated password data
            print("Stored password data after removal:")
            logged_in_user.get_data()

            # Set a new username
            logged_in_user.set_username("john_smith")

            # Set a new password
            logged_in_user.set_password("new_secure_password")

            # Log out
            print("Logging out.")
            logged_in_user = None
        else:
            print("Login failed.")
    else:
        print("Registration failed.")
