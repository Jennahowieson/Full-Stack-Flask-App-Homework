import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()

author1 = Author("Michelle Obama")
author2 =Author("Tina Fey")

author_repository.save(author1)
author_repository.save(author2)

book1 = Book("Becoming", "Autobiography",author1)
book2 = Book("Bossypants", "Tina Fey", author2)

book_repository.save(book1)
book_repository.save(book2)