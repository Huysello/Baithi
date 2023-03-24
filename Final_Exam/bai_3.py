class Book:
    def __init__(self, title, author, publisher, isbn):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.isbn = isbn

class Library:
    def __init__(self):
        self.books = []

    def view_books(self):
        for book in self.books:
            print(f"Title: {book.title}\nAuthor: {book.author}\nPublisher: {book.publisher}\nISBN: {book.isbn}\n")

    def add_book(self, book):
        self.books.append(book)

    def update_book(self, title, author, publisher, isbn):
        for book in self.books:
            if book.title == title:
                book.author = author
                book.publisher = publisher
                book.isbn = isbn
                print(f"{title} has been updated.")
                break
        else:
            print(f"{title} not found.")

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"{title} has been removed.")
                break
        else:
            print(f"{title} not found.")

    def search_books(self, keyword):
        for book in self.books:
            if keyword in book.title or keyword in book.author:
                print(f"Title: {book.title}\nAuthor: {book.author}\nPublisher: {book.publisher}\nISBN: {book.isbn}\n")

    def sort_books(self, sort_key):
        self.books.sort(key=lambda book: getattr(book, sort_key))
        print("Books sorted by", sort_key)

library = Library()

# thêm sách

book1 = Book("python", "codebasic", "NXB.Trẻ", "9780")

library.add_book(book1)

# xem
library.view_books()

# cập nhật
library.update_book("pythonbasic", "codebasic", "NXB.Trẻ", "9780")
library.view_books()

# xóa
library.remove_book("9780")
library.view_books()

# tìm kiếm
library.search_books("9780")

