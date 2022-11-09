import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()

author1 = Author("Michelle Obama")
author2 =Author("Tina Fey")
author3 = Author("Malala Yousafzai")

author_repository.save(author1)
author_repository.save(author2)
author_repository.save(author3)


book1 = Book("Becoming", "Autobiography",author1)
book2 = Book("Bossypants", "Autobiography", author2)
book3 = Book("I Am Malala", "Autobiography", author3)

book_repository.save(book1)
book_repository.save(book2)
book_repository.save(book3)

pdb.set_trace()
