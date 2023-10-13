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
    # Create a default book object
    b = Book()
    # Store the user-supplied values within the book object
    b.title = title
    b.author = author
    b.book_id = book_id
    # Add the book to the library
    library.append(b)
    print("Book added to library")

# Print a line break
print("-"*20)
# Loop through the books in the library
for book in library:
    # Display the current book's information using its display method
    book.display()