**Command:**

```python
from .models import Book

new_book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_date=1949
)

print(f"Book created: {new_book}")

# Expected Output (create.md):

# Book created: 1984 (id=<book_id>)



### Retrieve (retrieve.md):

from .models import Book

retrieved_book = Book.objects.get(pk=new_book.id)

print(f"Retrieved book details:\n{retrieved_book}")

# Expected Output (retrieve.md):

# Retrieved book details:
# 1984 (id=<book_id>)
#     author: George Orwell
#     publication_date: 1949


###Update (update.md):

retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()

print(f"Book title updated: {retrieved_book}")

# Expected Output (update.md):

# Book title updated: Nineteen Eighty-Four (id=<book_id>)



###Delete (delete.md):
retrieved_book.delete()

print("Book deleted.")

# Try to retrieve all books to confirm deletion
all_books = Book.objects.all()

if all_books:
    print("There are still books in the database. Something went wrong!")
else:
    print("Book deletion confirmed. No books found.")

#     Expected Output (delete.md):

# Book deleted.
# Book deletion confirmed. No books found.