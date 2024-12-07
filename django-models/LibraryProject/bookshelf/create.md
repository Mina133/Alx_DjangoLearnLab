**Command:**

```python
from .models import Book

new_book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_date=1949
)

print(f"Book created: {new_book}")