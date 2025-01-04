"""
Authenticator module to validate username and password.
"""


def authenticator(username, password, file_path="users.txt"):
    """
    Authenticates a user by checking the username and password against a credentials file.

    Args:
        username (str): The username to authenticate.
        password (str): The password for the user.
        file_path (str): Path to the credentials file. Defaults to 'users.txt'.

    Raises:
        ValueError: If the username does not exist or the password does not match.
    """
    try:
        # Read credentials from the file
        with open(file_path, "r", encoding="utf-8") as users_file:
            credentials = {
                line.strip().split(":")[0]: line.strip().split(":")[1]
                for line in users_file
            }

        # Validate the username and password
        if username not in credentials:
            raise ValueError("Username does not exist.")
        if password != credentials[username]:
            raise ValueError("Password does not match.")

        print("Authentication successful!")

    except FileNotFoundError:
        print("Error: The file does not exist!")
    except ValueError as error:
        print(f"Error: Authentication failed - {error}")
    except OSError as os_error:
        print(f"Error: OS-related issue - {os_error}")
    except Exception as unexpected_error:
        print(f"An unexpected error occurred: {unexpected_error}")


# Example Usage
if __name__ == "__main__":
    authenticator("admin", "password123")  # Successful
    authenticator("karim", "wrongpass")  # Wrong password
    authenticator("someuser", "wrongpass")  # Username does not exist
