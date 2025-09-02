from relationship_app.models import Author, Book, Library, Librarian

# Create sample data
author = Author.objects.create(name="George Orwell")
book1 = Book.objects.create(title="1984", author=author)
book2 = Book.objects.create(title="Animal Farm", author=author)

library = Library.objects.create(name="Central Library")
library.books.set([book1, book2])

librarian = Librarian.objects.create(name="Ms. Reed", library=library)

# 1. Query all books by a specific author
author_name = "George Orwell"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print(f"Books by {author_name}:")
for book in books_by_author:
    print(f"- {book.title}")

# 2. List all books in a library
library_name = "Central Library"
library = Library.objects.get(name=library_name)
books = library.books.all()
print(f"\nBooks in {library_name}:")
for book in books:
    print(f"- {book.title}")

# 3. Retrieve the librarian for a library
lib = Librarian.objects.get(library=library)
print(f"\nLibrarian for {library.name}: {lib.name}")
