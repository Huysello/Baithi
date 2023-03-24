from loguru import logger

class Library:
    def __init__(self, books) -> None:
        self.books = books

    def show_avail_books(self):
        avail_books = '\n----------- List of available books as following --------------\n'
        for book, borrower in self.books.items():
            if borrower == 'Free':
                # logger.info(book)
                avail_books = avail_books + book + '\n'
                
        logger.info(avail_books)

    def lend_book(self, requested_book, borrower):
        if self.books[requested_book] == 'Free':
            logger.info(f'The book {requested_book} is borrowed sucessfuly by {borrower}.')
            self.books[requested_book] = borrower
            return True
        else:
            logger.info(f'Sorry, the book {requested_book} is already borrowed by {self.books[requested_book]}.')
            return False
    
    def return_book(self, returned_book):
        logger.info(f'The book {returned_book} is returned sucessfully by {self.books[returned_book]}.')
        self.books[returned_book] = 'Free'