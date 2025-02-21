"""Library Management System Based on OOP concepts"""


class Book:
    """
    Represents a book in the library.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        _is_checked_out (bool): The checkout status of the book (True if checked out, False otherwise).
    """

    def __init__(self, title, author):
        """
        Initializes a new Book object.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author
        self._is_checked_out = False  # Initialize as not checked out

    def change_book_status(self, status):
        """
        Changes the checkout status of the book.

        Args:
            status (bool): The new checkout status (True or False).
        """
        self._is_checked_out = status

    def get_status(self):
        """
        Gets the current checkout status of the book.

        Returns:
            bool: The current checkout status.
        """
        return self._is_checked_out


class Library:
    """
    Manages the collection of books in the library.

    Attributes:
        __books (list): A list of Book objects in the library.
    """

    def __init__(self):
        """Initializes a new Library object."""
        self.__books = []

    def add_book(self, new_book):
        """
        Adds a new book to the library.

        Args:
            new_book (Book): The Book object to add.
        """
        self.__books.append(new_book)
        print(f"Added: {new_book.title} by {new_book.author}\n")

    def check_if_book_exists(self, book_title):
        """
        Checks if a book with the given title exists in the library.

        Args:
            book_title (str): The title of the book to check.

        Returns:
            bool: True if the book exists, False otherwise.
        """
        try:
            for book in self.__books:
                if book_title == book.title:
                    return True
            return False
        except Exception:
            print("Error: failed in checking if the book exists")
            return False  # Important: Return False in case of error.

    def get_book(self, book_title):
        """
        Gets a book object by its title.

        Args:
            book_title (str): The title of the book to get.

        Returns:
            Book or None: The Book object if found, None otherwise.
        """
        try:
            if self.check_if_book_exists(book_title):
                for book in self.__books:
                    if book_title == book.title:
                        return book
            else:
                return None
        except Exception:
            print("Error: failed in getting the book")
            return None  # Important: Return None in case of error

    def check_book_status(self, book_title):
        """
        Checks the checkout status of a book.

        Args:
            book_title (str): The title of the book to check.

        Returns:
            bool or None: The checkout status (True or False) if the book exists, None otherwise.
        """
        try:
            if self.check_if_book_exists(book_title):
                book = self.get_book(book_title)
                if book:  # check if book is not none
                    return book.get_status()
                else:
                    return None
            else:
                return None
        except Exception as e:
            print(f"Error in status: {e}")
            return None

    def check_out_book(self, book_title):
        """
        Checks out a book from the library.

        Args:
            book_title (str): The title of the book to check out.
        """
        try:
            if self.check_if_book_exists(book_title):
                if not self.check_book_status(book_title):
                    self.get_book(book_title).change_book_status(True)
                    print(f"You have successfully checked out '{book_title}'.\n")
                else:
                    print(f"Sorry, '{book_title}' is already checked out.\n")
            else:
                print(f"Sorry, '{book_title}' is not in the library.\n")
        except (ValueError, AttributeError) as e:  # Combined exception handling
            print(f"Error: {e}")

    def return_book(self, book_title):
        """
        Returns a book to the library.

        Args:
            book_title (str): The title of the book to return.
        """
        try:
            if self.check_book_status(book_title):
                self.get_book(book_title).change_book_status(False)
                print(f"{book_title} has been returned.\n")
            elif self.check_if_book_exists(book_title):
                print(f"{book_title} is already in the library.")
            else:
                print(f"Sorry, {book_title} doesn't exist.")

        except (ValueError, AttributeError) as e:  # Combined exception handling
            print(f"Error: {e}")

    def list_available_books(self):
        """Lists all available books in the library."""
        print("Available books...")
        for book in self.__books:
            if not book.get_status():
                print(f"{book.title} by {book.author}")



