class Library:
    def __init__(self, list_of_books):
        self.books = list_of_books

    def display_Available_books(self):
        print("Books Present in library are -> ")
        for book in self.books:
            print("-> ", book)
        pass

    def borrow_book(self, book_name):
        if book_name in self.books:
            print(f"book issued {book_name}. Please keep it safe and return it in 30 days")
            self.books.remove(book_name)
            return True
        else:
            print("Sorry! this book is unavailable right now, Book is issued to some one else. Please wait until the "
                  "book is returned")
            return False

    def return_Book(self, book_name):
        self.books.append(book_name)
        print("Thanks for returning this book")


class Student:
    def request_book(self):
        self.book = input("Enter the book name you want to borrow ->  ")
        return self.book

    def return_book(self):
        self.book = input("Enter the book name you want to borrow ->  ")
        return self.book


if __name__ == "__main__":
    central_Library = Library(['Algorithms', 'Django', 'Flask', 'Python notes', 'Hack the world'])
    student = Student()
    # central_Library.display_Available_books()

    while True:
        WelcomeMsg = '''Welcome to Central Library
        Please choose an option: 
        1. List all Books
        2. Request a book
        3. Return/Add a book
        4. Exit the Library
        '''
        print(WelcomeMsg)

        user_input = int(input("Enter your choice -> "))
        if user_input == 1:
            central_Library.display_Available_books()
        elif user_input == 2:
            central_Library.borrow_book(student.request_book())
        elif user_input == 3:
            central_Library.return_Book(student.return_book())
        elif user_input == 4:
            print("Thanks for choosing central library. ")
            exit()
        else:
            print('Invalid choice!')
