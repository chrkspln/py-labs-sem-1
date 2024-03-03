"""
Importing needed classes from previous lab
"""
from lab5 import Book, BookShop


class Tests:
    """
    Creating a class for staging all the tests
    """

    def test_get_name(self):
        """
        Testing the get_name method of the Book class.
        """
        test_name = "Frankenstein"
        instance = Book(name=test_name)
        actual_name = instance.get_name()
        assert actual_name == test_name


def test_get_price():
    """
    Testing the get_price method of the Book class.
    """
    test_price = 400
    instance = Book(price=test_price)
    actual_price = instance.get_price()
    assert actual_price == test_price


def test_get_num_of_pages():
    """
    Testing the get_num_of_pages method of the Book class.
    """
    test_pages = 500
    instance = Book(num_of_pages=test_pages)
    actual_pages = instance.get_num_of_pages()
    assert actual_pages == test_pages


def test_get_author():
    """
    Testing the get_author method of the Book class.
    """
    test_author = "Oscar Wilde"
    instance = Book(author=test_author)
    actual_author = instance.get_author()
    assert actual_author == test_author


def test_get_quantity():
    """
    Testing the get_quantity method of the Book class.
    """
    test_quantity = 500
    instance = Book(quantity=test_quantity)
    actual_quantity = instance.get_quantity()
    assert actual_quantity == test_quantity


def test_get_num_of_sales():
    """
    Testing the get_num_of_sales method of the Book class.
    """
    test_num_of_sales = 234
    instance = Book(num_of_sales=test_num_of_sales)
    actual_num_of_sales = instance.get_num_of_sales()
    assert actual_num_of_sales == test_num_of_sales


def test_add_new_book_to_shop():
    """
    Testing the add_new_book_to_shop method of the BookShop class.
    """
    instance = BookShop()
    test_book = "some book"
    instance.add_new_book_to_shop(test_book)
    assert test_book in instance.books_in_shop
    assert len(instance.books_in_shop) == 1


def test_delete_book_from_shop():
    """
    Testing the delete_book_from_shop method of the BookShop class.
    """
    instance = BookShop()
    test_book = "some book"
    instance.add_new_book_to_shop(test_book)
    instance.delete_book_from_shop(test_book)
    assert test_book not in instance.books_in_shop
    assert len(instance.books_in_shop) == 0


def test_top_price_books():
    """
    Testing the top_price_books method of the BookShop class.
    """
    instance = BookShop()
    test_book_1 = Book("some book number one", price=1000)
    test_book_2 = Book("some book number two", price=1200)
    test_book_3 = Book("some book number three", price=300)
    instance.add_new_book_to_shop(test_book_1)
    instance.add_new_book_to_shop(test_book_2)
    instance.add_new_book_to_shop(test_book_3)
    sorted_by_price_book_list = instance.top_price_books()
    assert sorted_by_price_book_list[0] == test_book_2
    assert sorted_by_price_book_list[1] == test_book_1
    assert sorted_by_price_book_list[2] == test_book_3


def test_top_sold_books():
    """
    Testing the top_sold_books method of the BookShop class.
    """
    instance = BookShop()
    test_book_1 = Book("some book number one", num_of_sales=1000)
    test_book_2 = Book("some book number two", num_of_sales=1200)
    test_book_3 = Book("some book number three", num_of_sales=300)
    instance.add_new_book_to_shop(test_book_1)
    instance.add_new_book_to_shop(test_book_2)
    instance.add_new_book_to_shop(test_book_3)
    sorted_by_sells_book_list = instance.top_sold_books()
    assert sorted_by_sells_book_list[0] == test_book_2
    assert sorted_by_sells_book_list[1] == test_book_1
    assert sorted_by_sells_book_list[2] == test_book_3
