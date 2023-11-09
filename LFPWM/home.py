# from app.users import User


def home_page_menu():
    print(
        """
1. Add passwords to storage
2. View storage
3. Delete items from storage
4. Logout
          """
    )
    choice = input("Input: ")
    return choice


def home_page(user):
    print("====================")
    print("Home page 🏡")
    while True:
        choice = home_page_menu()
        if choice == "1":
            title = input("Please enter a title for the password: ")
            data = input("Store a password: ")
            user.insert_data(title, data)
            print("Saved. ")
        elif choice == "2":
            user.get_data()
        elif choice == "3":
            data_to_delete = input("Enter a password to delete: ")
            user.remove_data(data_to_delete)
            print("Data deleted.")
        elif choice == "4":
            print("Logging out...")
            break
        else:
            print("Invalid input.")
