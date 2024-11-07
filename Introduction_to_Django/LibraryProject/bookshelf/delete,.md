**Command:**

```python
retrieved_book.delete()

print("Book deleted.")

# Try to retrieve all books to confirm deletion
all_books = Book.objects.all()

if all_books:
    print("There are still books in the database. Something went wrong!")
else:
    print("Book deletion confirmed. No books found.")