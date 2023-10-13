# Define a Book class (in a file called Book.py)
class Book:
    # Establish 3 attributes (with default values) that every instance/object
    # of this class will possess
    title = "Default title"
    author = "Default author"
    book_id = None
    
    # Define a formatted way for a Book to display its information/state
    def display(self):
        print(f"Title: {self.title}\n\tAuthor: {self.author}\n\tBook id: {self.book_id}")