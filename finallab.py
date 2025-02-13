class SocialNetwork:
    """
    Базовый класс для представления социальной сети.

    Атрибуты:
        name (str): Название социальной сети.
        users (list[str]): Список пользователей социальной сети.
        _api_key (str): Приватный атрибут для хранения API ключа.
    """

    def __init__(self, name: str, api_key: str) -> None:
        """
        Инициализирует объект социальной сети.

        Аргументы:
            name (str): Название социальной сети.
            api_key (str): API ключ для доступа к социальной сети.
        """
        self.name = name
        self.users: list[str] = []
        self._api_key = api_key  # Инкапсуляция: API ключ не должен быть доступен извне.

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        Возвращает:
            str: Строковое представление социальной сети.
        """
        return f"Социальная сеть: {self.name}, Пользователей: {len(self.users)}"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление объекта.

        Возвращает:
            str: Формальное строковое представление социальной сети.
        """
        return f"SocialNetwork(name={self.name}, users={len(self.users)})"

    def add_user(self, user: str) -> None:
        """
        Добавляет пользователя в социальную сеть.

        Аргументы:
            user (str): Имя пользователя.
        """
        if user not in self.users:
            self.users.append(user)
            print(f"Пользователь {user} добавлен в {self.name}.")
        else:
            print(f"Пользователь {user} уже существует в {self.name}.")

    def get_api_key(self) -> str:
        """
        Возвращает API ключ.

        Возвращает:
            str: API ключ.
        """
        return self._api_key

class VK(SocialNetwork):
    """
    Дочерний класс для представления социальной сети VK.

    Атрибуты:
        name (str): Название социальной сети.
        users (list[str]): Список пользователей социальной сети.
        _api_key (str): Приватный атрибут для хранения API ключа.
        groups (list[str]): Список групп в VK.
    """

    def __init__(self, name: str, api_key: str, groups: list[str]) -> None:
        """
        Инициализирует объект социальной сети VK.

        Аргументы:
            name (str): Название социальной сети.
            api_key (str): API ключ для доступа к социальной сети.
            groups (list[str]): Список групп в VK.
        """
        super().__init__(name, api_key)
        self.groups: list[str] = groups

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        Возвращает:
            str: Строковое представление социальной сети VK.
        """
        return f"VK: {self.name}, Пользователей: {len(self.users)}, Групп: {len(self.groups)}"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление объекта.

        Возвращает:
            str: Формальное строковое представление социальной сети VK.
        """
        return f"VK(name={self.name}, users={len(self.users)}, groups={len(self.groups)})"

    def add_group(self, group: str) -> None:
        """
        Добавляет группу в VK.

        Аргументы:
            group (str): Название группы.
        """
        if group not in self.groups:
            self.groups.append(group)
            print(f"Группа {group} добавлена в VK.")
        else:
            print(f"Группа {group} уже существует в VK.")

    def get_api_key(self) -> str:
        """
        Перегрузка метода для возврата API ключа с дополнительным сообщением.

        Возвращает:
            str: API ключ с сообщением.
        """
        return f"API ключ для VK: {self._api_key}"
class Facebook(SocialNetwork):
    """
    Дочерний класс для представления социальной сети Facebook.

    Атрибуты:
        name (str): Название социальной сети.
        users (list[str]): Список пользователей социальной сети.
        _api_key (str): Приватный атрибут для хранения API ключа.
        pages (list[str]): Список страниц в Facebook.
    """

    def __init__(self, name: str, api_key: str, pages: list[str]) -> None:
        """
        Инициализирует объект социальной сети Facebook.

        Аргументы:
            name (str): Название социальной сети.
            api_key (str): API ключ для доступа к социальной сети.
            pages (list[str]): Список страниц в Facebook.
        """
        super().__init__(name, api_key)
        self.pages: list[str] = pages

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        Возвращает:
            str: Строковое представление социальной сети Facebook.
        """
        return f"Facebook: {self.name}, Пользователей: {len(self.users)}, Страниц: {len(self.pages)}"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление объекта.

        Возвращает:
            str: Формальное строковое представление социальной сети Facebook.
        """
        return f"Facebook(name={self.name}, users={len(self.users)}, pages={len(self.pages)})"

    def add_page(self, page: str) -> None:
        """
        Добавляет страницу в Facebook.

        Аргументы:
            page (str): Название страницы.
        """
        if page not in self.pages:
            self.pages.append(page)
            print(f"Страница {page} добавлена в Facebook.")
        else:
            print(f"Страница {page} уже существует в Facebook.")

    def get_api_key(self) -> str:
        """
        Перегрузка метода для возврата API ключа с дополнительным сообщением.

        Возвращает:
            str: API ключ с сообщением.
        """
        return f"API ключ для Facebook: {self._api_key}"

if __name__ == "__main__":
    # Создаем объект социальной сети VK
    vk = VK(name="VKontakte", api_key="vk12345", groups=[])
    vk.add_user("Иван Иванов")
    vk.add_user("Мария Петрова")
    vk.add_group("Программисты")
    vk.add_group("Дизайнеры")

    # Создаем объект социальной сети Facebook
    fb = Facebook(name="Facebook", api_key="fb67890", pages=[])
    fb.add_user("Алексей Сидоров")
    fb.add_user("Елена Кузнецова")
    fb.add_page("IT Новости")
    fb.add_page("Кино и сериалы")

    # Выводим информацию о социальных сетях
    print(vk)
    print(fb)

    # Получаем API ключи
    print(vk.get_api_key())
    print(fb.get_api_key())
