class Book:
    def __init__(self):
        self.__title = "Harry Potter"

    def get_title(self):
        print(f"The book's title is: {self.__title}")

    def set_title(self, title):
        self.__title = title


book = Book()
book.get_title()

book.__title = "The Clementine"
book.get_title()

book.set_title("The Clementine")
book.get_title()
