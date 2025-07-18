from relationship_app.models import Author, Book, Library, Librarian

# Create sample data
author = Author.objects.create(name="George Orwell")
book1 = Book.objects.create(title="1984", author=author)
book2 = Book.objects.create(title="Animal Farm", author=author)

library = Library.objects.create(name="Central Library")
library.books.set([book1, book2])

librarian = Librarian.objects.create(name="Ms. Reed", library=library)

# 1. Query all books by a specific author
books_by_orwell = Book.objects.filter(author__name="George Orwell")
print("Books by George Orwell:")
for book in books_by_orwell:
    print(f"- {book.title}")

# 2. List all books in a library
print("\nBooks in Central Library:")
for book in library.books.all():
    print(f"- {book.title}")

# 3. Retrieve the librarian for a library
lib = Librarian.objects.get(library=library)
print(f"\nLibrarian for {library.name}: {lib.name}")
