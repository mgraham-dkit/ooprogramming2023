# Import our class
from Book import Book


# Create a list to hold the book objects
library = []
# Loop 3 times
for i in range(3):
    # Take in book informatio
    title = input("Please enter the book's title: ")
    author = input("Please enter the book's author: ")
    book_id = input("Please enter the book's ID: ")
    # Create a book object using the user-supplied information
    # This will store the user's data for title, author and book_id
    # straight into a book object, instead of setting things to defaults and then resetting them
    b = Book(title, author, book_id)
    # Add the book to the library
    library.append(b)
    print("Book added to library")

print("-"*20)
for book in library:
    book.display()