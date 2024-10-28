"""
Implement procedural programming
"""

def create_book(title, author):
    return {
        "title": title,
        "author": author,
        "available": True}

book1 = create_book("The Catcher in the Rye", "J. D. Salinger")
book2 = create_book("To Kill a Mockingbird", "Harper Lee")
book3 = create_book("The Great Gatsby", "F. Scott Fitzgerald")

print("============================================")

def create_user(name, borrowed_books=[]):
    return {
        "name": name,
        "borrowed_books": borrowed_books
    }

Jhon = create_user("Jhon Doe")
print(Jhon["name"])
print(Jhon["borrowed_books"])

print("============================================")

# User action

def borrow_book(user, book):
    user["borrowed_books"].append(book)
    book["available"] = False

    print(f"{user['name']} borrowed {book['title']}")

def return_book(user, book):
    user["borrowed_books"].remove(book)
    book["available"] = True

    print(f"{user['name']} returned {book['title']}")

borrow_book(Jhon, book1)
borrow_book(Jhon, book2)

print(book1)

return_book(Jhon, book1)

print(Jhon)

print(book1)