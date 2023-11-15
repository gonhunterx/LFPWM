# LFPWM

If you are using it for the first time, you must create a user data table.

Developed in: VSCode

LamaForge PW Manager pip Package Documentation

Summary:
Lamaforge PW Manager is a secure Pypi package for password storage and user authentication.
This program allows users to create a custom user instance with the predefined User class.
Another feature is that you can easily create and store encrypted data of your own or take input from a user
of the developer's application.

Passwords are encrypted before they are stored locally. The database used for this application is SQLite3.
SQLite3 uses a database created on your local machine and is equally as safe as any other database.

Link to repository: https://github.com/gonhunterx/LFPWM

(For specific use examples of methods and parameters
go to the Example Usage in Python section)

Step 1 (in terminal):

```
pip install LFPWM
```

Step 2: from LFPWM import \*
(This step will allow you to access all functionality of the LFPWM Package.)

After installation,

LFPWM pip package usage:

# Password Manager (PasswordManager)

The PasswordManager class in the LFPWM package is designed to handle the encryption and decryption of passwords. It utilizes the Fernet symmetric encryption scheme from the cryptography library.

### Methods:

encrypt_password(password: str) -> bytes
Encrypts the given plaintext password.

### Parameters:

password (str): The plaintext password to be encrypted.
Returns: The encrypted password.

decrypt_password(encrypted_password) -> str
Decrypts the given encrypted password.

### Parameters:

encrypted_password: The encrypted password.
str: The decrypted plaintext password.

# User Class (User)

The User class represents a user entity and includes methods for managing user information and storing encrypted passwords.

### Methods:

set_username(new_username: str) -> None
Updates the username for the user.

### Parameters:

new_username (str): The new username to set.

set_password(new_password: str) -> None
Updates the password for the user.

### Parameters:

new_password (str): The new password to set.

insert_data(title: str, data: str) -> None
Inserts encrypted password data into the UserData table.

### Parameters:

title (type: string): The title associated with the stored password.
data (type: string): The plaintext password to be encrypted and stored.

get_data() -> None
Retrieves and decrypts stored password data from the UserData table, then prints it.

remove_data(data_to_delete: str) -> None

Deletes password data associated with a given title.

Parameters:
data_to_delete (str): The title of the data to be deleted.

Example Usage
In Python:
from LFPWM.sql_db import create_connection
from LFPWM import User

# Create a user instance

```
user = User("example_user", "example_password")
```

# Set a new username

```
user.set_username("new_username")
```

# Set a new password

```
user.set_password("new_password")
```

# Insert data into UserData table

```
user.insert_data("Email", "user@example.com")
```

# Retrieve and print stored data

```
user.get_data()
```

# Remove data by title

```
user.remove_data("Email")
```

# Encrypt your own data for use

```
Item_to_encrypt = “Hello World”
encrypted_item = PasswordManager.encrypt_password(Item_to_encrypt)
print(encrypted_item)
```

This will print as an encrypted token.
You can also use the PasswordManager’s decrypt_password static method. This will allow you to view the original value behind an encrypted one.

# You can use it like this:

```
decrypted_item = PasswordManager.decrypt_password(encrypted_item)
print(decrypted_item)
```

# this will print “Hello World” (The decrypted value of encrypted_item)

This example demonstrates some possible use cases of the User, and PasswordManager classes and their associated methods.
You can integrate these functionalities into your own projects for secure password management and other data storage uses for small to medium-sized projects.
