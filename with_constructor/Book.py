# Define a Book class (in a file called Book.py)
class Book:
    # Define a constructor that will run whenever you build an instance of Book
    # This constructor requires 3 parameters to be supplied by the calling code:
        # The title of the Book being created
        # The author of the Book being created
        # The id of the book being created
    def __init__(self, title, author, book_id):
        # Store each value in the corresponding attribute of this instance
        self.title = title
        self.author = author
        self.book_id = book_id
    
    # Define a formatted way for a Book to display its information/state
    def display(self):
        print(f"Title: {self.title}\n\tAuthor: {self.author}\n\tBook id: {self.book_id}")
    
    # Define a way for a Book to turn its information/state into a string
    # This is useful to allow things like print() to display the Book's state
    # and not just its class type and location of the object in memory
    def __str__(self):
        '''
            Format of the line:
                Surround object description with <>
                Start description with Filename.Classname
                Label each piece of data with that attribute's name in the class
                Separate the attribute name and the data with an equals (=)
                Separate each attribute's information with a comma (,)
        '''
        return f"<Book.Book: title={self.title}, author={self.author}, book_id={self.book_id}>"