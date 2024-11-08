**Command:**

```python
from .models import Book

retrieved_book = Book.objects.get(pk=2)

print(f"Retrieved book details:\n{retrieved_book}")