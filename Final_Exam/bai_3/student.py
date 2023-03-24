from loguru import logger

class Student:
    def __init__(self, std_name, library) -> None:
        self.std_name = std_name
        self.books = []
        self.library = library

    def view_brrowed_books(self):
        if not self.books:
            logger.info('You have not borrowed any book!')
        else:
            logger.info('-------- List borrowed books -------------')
            for ind, book in enumerate(self.books):
                logger.info(f'{ind+1}. {book}')

    def request_book(self):
        book_name = input('Enter the name of book which you want to borrow: ')
        if self.library.lend_book(book_name, self.std_name):
            logger.info(f'You borrowed the book {book_name} sucessfully!')
            self.books.append(book_name)
        else:
            logger.info(f'You can not borrow the book {book_name}. Try to choose another!')

    def return_book(self):
        self.view_brrowed_books()
        return_book_id = int(input('Choose a book in above list to return (1, 2, ...): '))
        return_book_name = self.books[return_book_id-1]
        self.library.return_book(return_book_name)
        self.books.pop(return_book_id-1)
        logger.info(f'You returned the book {return_book_name} sucessfully!')