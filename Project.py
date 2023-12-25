# from abc import ABC, abstractmethod

# class LibraryItem(ABC):
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

#     @abstractmethod
#     def display_details(self):
#         pass

# class Book(LibraryItem):
#     def __init__(self, title, author, genre):
#         super().__init__(title, author)
#         self.genre = genre

#     def display_details(self):
#         print(f"Book: {self.title} by {self.author}, Genre: {self.genre}")

# class User:
#     def __init__(self, user_id, name):
#         self.user_id = user_id
#         self.name = name

# class Transaction:
#     def __init__(self, book, user, transaction_type):
#         self.book = book
#         self.user = user
#         self.transaction_type = transaction_type

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.transactions = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            book.display_details()

    def add_user(self, user):
        self.users.append(user)

    def borrow_book(self, book, user):
        if book in self.books:
            transaction = Transaction(book, user, "Borrow")
            self.transactions.append(transaction)
            self.books.remove(book)
            print(f"{user.name} borrowed {book.title}.")
        else:
            print("Book not available for borrowing.")

    def return_book(self, book, user):
        if book not in self.books:
            transaction = Transaction(book, user, "Return")
            self.transactions.append(transaction)
            self.books.append(book)
            print(f"{user.name} returned {book.title}.")
        else:
            print("Book already in the library.")

