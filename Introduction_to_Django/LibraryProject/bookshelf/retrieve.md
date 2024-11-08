**Command:**

```python
from .models import Book

retrieved_book = Book.objects.get(pk=2)

for details in retrieved_book:
    print(f'\n"{retrieved_book}"')