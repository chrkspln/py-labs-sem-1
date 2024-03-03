class Book:
    def __init__(self, name="Pollyanna", price=345, num_of_pages=500,
                 author="Eleonor Porter", quantity=45, num_of_sales=234):
        self.__name = name
        self.__price = price
        self.__num_of_pages = num_of_pages
        self.__author = author
        self.__quantity = quantity
        self.__num_of_sales = num_of_sales

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_num_of_pages(self):
        return self.__num_of_pages

    def get_author(self):
        return self.__author

    def get_quantity(self):
        return self.__quantity

    def get_num_of_sales(self):
        return self.__num_of_sales

    def __str__(self):
        return (f'book name is {self.get_name()}, it\'s author is {self.get_author()}.\n'
                f'number of pages is {self.get_num_of_pages()} and the price is {self.get_price()} uah.\n'
                f'available quantity - {self.get_quantity()}, the book was sold {self.get_num_of_sales()} times.')


class BookShop:
    def __init__(self):
        self.books_in_shop = []

    def add_new_book_to_shop(self, book):
        self.books_in_shop.append(book)

    def delete_book_from_shop(self, book):
        if book in self.books_in_shop:
            self.books_in_shop.remove(book)

    def top_price_books(self):
        books_sorted_by_price = sorted(self.books_in_shop, key=lambda book: book.get_price(), reverse=True)
        return books_sorted_by_price

    def top_sold_books(self):
        books_sorted_by_sells = sorted(self.books_in_shop, key=lambda book: book.get_num_of_sales(), reverse=True)
        return books_sorted_by_sells


if __name__ == "__main__":
    frank_book = Book("Frankenstein", 400, 231, "Mary Shelley", 14, 678)
    dorian_book = Book("The Picture of Dorian Grey", 389, 258, "Oskar Wilde", 13, 133)
    secret_book = Book("The Secret History", 500, 467, "Donna Tartt", 7, 121)
    default_book = Book()

    book_shop = BookShop()
    book_shop.add_new_book_to_shop(frank_book)
    book_shop.add_new_book_to_shop(dorian_book)
    book_shop.add_new_book_to_shop(secret_book)
    book_shop.add_new_book_to_shop(default_book)

    top_price_books = book_shop.top_price_books()
    top_sold_books = book_shop.top_sold_books()

    print("Top-price books are:\n")
    for i in top_price_books:
        print(i, '\n')

    print("\nTop-sold books are:\n")
    for i in top_sold_books:
        print(i, '\n')
