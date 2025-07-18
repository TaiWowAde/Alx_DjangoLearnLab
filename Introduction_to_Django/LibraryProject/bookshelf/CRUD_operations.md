## CREATE
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

## RETRIEVE
Book.objects.all()

## UPDATE
book.title = "Nineteen Eighty-Four"
book.save()

## DELETE
book.delete()
Book.objects.all()
