from bookshelf.models import Book

# Retrieve the book using get()
book = Book.objects.get(title="1984")

# Display all attributes
book.title
# Output: '1984'

book.author
# Output: 'George Orwell'

book.publication_year
# Output: 1949

book
# Output: <Book: 1984 by George Orwell (1949)>
