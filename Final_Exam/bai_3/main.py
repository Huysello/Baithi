from loguru import logger
from library import Library


def create_library():
    books = {
        'Gone with the wind': 'Free',
        'Python programing for every one': 'Free',
        'Clean code': 'Free',
        'Software design pattern': 'Free'
    }
    libr = Library(books)
   

    while True:
        logger.info('''
        ----------- LIBRARY FUNCTION MENU -------------
        1. Display available books
        2. Borrow a book
        3. Return a book
        4. View borrowed books
        5. Exit program
        ''')

        std_choise = int(input('Choise a function number: '))
        if std_choise == 1:
            libr.show_avail_books()
        else:
            exit()

if __name__ == '__main__':
    create_library()