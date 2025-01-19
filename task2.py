from pydantic import BaseModel

BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book(BaseModel):
    """
    Класс для представления книги с использованием Pydantic для валидации.

    Атрибуты:
        id (int): Идентификатор книги.
        name (str): Название книги.
        pages (int): Количество страниц в книге.

    Методы:
        __str__: Возвращает строковое представление книги.
        __repr__: Возвращает строку, по которой можно инициализировать объект.

    Примеры:
        >>> book = Book(id=1, name='Преступление и наказание', pages=671)
        >>> str(book)
        'Книга "Преступление и наказание"'
        >>> repr(book)
        "Book(id=1, name='Преступление и наказание', pages=671)"
    """

    id: int
    name: str
    pages: int

    def __str__(self) -> str:
        """
        Возвращает строковое представление книги в формате:
        Книга "название_книги"
        """
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """
        Возвращает строку, по которой можно инициализировать объект.
        """
        return f"Book(id={self.id}, name='{self.name}', pages={self.pages})"


class Library:
    def __init__(self, books=None):
        """
        Конструктор класса Library.

        :param books: Список книг (по умолчанию пустой список).
        """
        self.books = books if books is not None else []

    def get_next_book_id(self) -> int:
        """
        Метод для получения следующего идентификатора книги.

        :return: Следующий доступный идентификатор для новой книги.
        """
        if not self.books:
            return 1

        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Метод для поиска индекса книги по ее id.

        :param book_id: Идентификатор книги.
        :return: Индекс книги в списке.
        :raises ValueError: Если книга с данным id не существует.
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError(f"Книги с запрашиваемым id {book_id} не существует.")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
