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


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
