**Command:**

```python
from .models import Book

retrieved_book = Book.objects.get(pk=new_book.id)

print(f"Retrieved book details:\n{retrieved_book}")