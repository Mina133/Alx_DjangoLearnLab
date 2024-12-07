from .models import *

# Query all books by specific author
author_name = "Mina"
author = "author"
author =Author.objects.get(name=author_name).objects.filter(author=author)

library_name = "library"
bookInLib = Library.objects.get(name=library_name).books.all()


# retrieve the Librarian for all libraries
librarian_name = "librarian_name"
librarian = Librarian.objects.get(library=librarian_name)
