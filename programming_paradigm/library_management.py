class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    # We check if a book has been checked out or not
    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    # We check if a book is returned or not
    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return False
        return True
    
    # We check is the book is avaible inside the list
    def book_is_avaible(self):
        return not self._is_checked_out

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

class Library:

    def __init__(self):
        self._books = []

    def add_book(self,title, author):
        new_book = Book(title,author)
        self._books.append(new_book)


    def check_out_book(self,title):
        for book in self._books:
            if book.title == title:
                if Book.check_out():
                    print("The book {title} has been already checked out")
                    return False
                else:
                    self._books.remove(title)
                    print("The book {title} has been checked out succesfully")
                    return True
        print (f"{title} is not available on our library")
        return False
    
    def list_available_books(self):
        checker = [book for book in self._books if Book.book_is_avaible()]
        if checker:
            for books in self._books:
                print(f"- {books.title} by {books.author}")
        else:
            print("There is no books available. ")
