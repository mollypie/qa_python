import pytest

from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_added_new_book(self):
        book = BooksCollector()
        book.add_new_book('Дюна')

        assert "Дюна" in book.books_genre

    def test_add_new_book_book_without_genre_returned_empty_string(self):
        book = BooksCollector()
        book.add_new_book('Дюна')

        assert book.get_book_genre('Дюна') == ''

    def test_set_book_genre_existing_book_genre_successfully_applied(self):
        book = BooksCollector()
        book.books_genre = {'Дюна': ''}

        book.set_book_genre('Дюна', 'Фантастика')

        assert book.books_genre['Дюна'] == 'Фантастика'

    def test_get_book_genre_existing_book_returned_genre(self):
        book = BooksCollector()
        book.books_genre = {'Дюна': 'Фантастика'}

        genre = book.get_book_genre('Дюна')

        assert genre == 'Фантастика'

    def test_get_books_with_specific_genre_one_genre_returned_list_books(self):
        book = BooksCollector()
        book.books_genre = {'Дюна': 'Фантастика', 'Русалочка': 'Мультфильмы', 'Пикник на обочине': 'Фантастика'}

        list_books = book.get_books_with_specific_genre('Фантастика')

        assert list_books == ['Дюна', 'Пикник на обочине']

    def test_get_books_genre_returned_dictionary_with_books_and_genre(self):
        book = BooksCollector()
        book.books_genre = {'Дюна': 'Фантастика'}

        assert book.get_books_genre() == {'Дюна': 'Фантастика'}

    @pytest.mark.parametrize('genre', ['Фантастика', 'Мультфильмы', 'Комедии'])
    def test_get_books_for_children_genre_without_rating_returned_one_book(self, genre):
        book = BooksCollector()
        book.books_genre = {'Детская книжка': genre}

        approved_book = book.get_books_for_children()

        assert len(approved_book) == 1

    def test_add_book_in_favorites_one_book_added_to_list_favorites(self):
        book = BooksCollector()
        book.books_genre = {'Дюна': 'Фантастика'}

        book.add_book_in_favorites('Дюна')

        assert len(book.favorites) == 1

    def test_delete_book_from_favorites_one_book_got_empty_list_favorites(self):
        book = BooksCollector()
        book.favorites = ['Дюна']

        book.delete_book_from_favorites('Дюна')

        assert len(book.favorites) == 0

    def test_get_list_of_favorites_books_two_books_returned_list_favorites_books(self):
        book = BooksCollector()
        book.favorites = ['Дюна', 'Пикник на обочине']

        list_favorites_book = book.get_list_of_favorites_books()

        assert list_favorites_book == ['Дюна', 'Пикник на обочине']
