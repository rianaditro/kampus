class Book:
    def __init__(self, title, author, category):
        self.title = title
        self.author = author
        self.category = category

        print(f"Book {self.title} with {self.category} category created")

    def __repr__(self):
        return f"Book({self.title}, {self.author}, {self.category})"


class ShelfBook:
    def __init__(self, category_name):
        self.category_name = category_name
        self.books_on_shelf = []
        self.total_books = len(self.books_on_shelf)
        
        print(f"{self.category_name} shelf created with {self.total_books} books: ")

    def __repr__(self):
        return f"ShelfBook({self.category_name})"

class Librarian:
    def __init__(self, name):
        self.name = name
        self.shelfs = []

        print(f"Librarian {self.name} created")
        print(f"{self.name} has {len(self.shelfs)} shelves")

    def add_book_to_shelf(self, book):

        # get the list of shelf category
        shelf_categories = [shelf.category_name for shelf in self.shelfs]

        # check if book category is in shelf category
        if book.category in shelf_categories:
            # get index
            index = shelf_categories.index(book.category)
            # add book to shelf
            self.shelfs[index].books_on_shelf.append(book)
            print(f"{book.title} added to {book.category} shelf")
        else:
            # create new shelf
            new_shelf = ShelfBook(book.category)
            # add book to shelf
            new_shelf.books_on_shelf.append(book)
            # add shelf to librarian
            self.shelfs.append(new_shelf)
            print(f"{book.title} added to {book.category} shelf")

            


"""------------------"""
book1 = Book("The Catcher in the Rye", "J. D. Salinger", "Fiction")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "Fiction")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction")
book4 = Book("Netherland", "Harper Lee", "Non-fiction")
book5 = Book("Dream", "Robert T. Kiyosaki", "Science")


librarian = Librarian("John Doe")

librarian.add_book_to_shelf(book1)
librarian.add_book_to_shelf(book2)
librarian.add_book_to_shelf(book5)

print("============================================")

for shelf in librarian.shelfs:
    print(f"{shelf.category_name} shelf has {len(shelf.books_on_shelf)} books: {shelf.books_on_shelf}")

