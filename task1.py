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

class Book:
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
    def __init__(self, id: int, name: str, pages: int):
        self.id = id
        if not isinstance(id, int):
            raise TypeError("ID должно быть типа int")
        self.name = name
        if not isinstance(name, str):
            raise TypeError("name должно быть типа str")

        self.pages = pages
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")

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


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
