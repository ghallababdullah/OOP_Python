class Table:
    def __init__(self, material: str, color: str, legs: int) -> None:
        """
        Инициализация объекта Стол.

        :param material: Материал стола .
        :param color: Цвет стола .
        :param legs: Количество ножек .
        :raises ValueError: Если количество ножек меньше или равно 0.
        """
        if legs <= 0:
            raise ValueError("Количество ножек должно быть больше 0.")
        self.material = material
        self.color = color
        self.legs = legs

    def paint(self, new_color: str) -> None:
        """
        Покрасить стол в новый цвет.

        :param new_color: Новый цвет для стола.
        :return: None

        >>> table = Table("wood", "brown", 4)
        >>> table.paint("white")
        >>> table.color
        'white'
        """
        self.color = new_color

    def extend(self, extra_space: float) -> None:
        """
        Увеличить площадь стола.

        :param extra_space: Дополнительная площадь, которую нужно добавить (должна быть больше 0).
        :raises ValueError: Если площадь отрицательная или равна 0.

        >>> table = Table("metal", "black", 4)
        >>> table.extend(2.5)
        Площадь стола увеличена на 2.5 м²
        """
        if extra_space <= 0:
            raise ValueError("Дополнительная площадь должна быть больше 0.")
        print(f"Площадь стола увеличена на {extra_space} м²")


class Tree:
    def __init__(self, species: str, age: int, height: float) -> None:
        """
        Инициализация объекта Дерево.

        :param species: Вид дерева (например, "дуб", "сосна").
        :param age: Возраст дерева (в годах, должен быть >= 0).
        :param height: Высота дерева (в метрах, должна быть > 0).
        :raises ValueError: Если возраст отрицательный или высота меньше или равна 0.
        """
        if age < 0:
            raise ValueError("Возраст дерева не может быть отрицательным.")
        if height <= 0:
            raise ValueError("Высота дерева должна быть больше 0.")
        self.species = species
        self.age = age
        self.height = height

    def grow(self, years: int) -> None:
        """
        Увеличить возраст дерева и его высоту.

        :param years: Количество лет, на которое дерево стареет (должно быть больше 0).
        :raises ValueError: Если years <= 0.

        >>> tree = Tree("елка", 10, 5.0)
        >>> tree.grow(5)
        >>> tree.age
        15
        """
        if years <= 0:
            raise ValueError("Количество лет должно быть больше 0.")
        self.age += years
        self.height += years * 0.5  # Дерево растет на 0.5 м в год

    def cut(self) -> None:
        """
        Срубить дерево.

        :return: None

        >>> tree = Tree("pine", 15, 7.0)
        >>> tree.cut()
        Дерево срублено.
        """
        print("Дерево срублено.")


class FacebookAccount:
    def __init__(self, username: str, friends_count: int, is_active: bool) -> None:
        """
        Инициализация объекта Аккаунт Facebook.

        :param username: Имя пользователя.
        :param friends_count: Количество друзей (должно быть >= 0).
        :param is_active: Активен ли аккаунт.
        :raises ValueError: Если количество друзей меньше 0.
        """
        if friends_count < 0:
            raise ValueError("Количество друзей не может быть отрицательным.")
        self.username = username
        self.friends_count = friends_count
        self.is_active = is_active

    def add_friend(self, friend_name: str) -> bool:
        """
        Добавить друга.

        :param friend_name: Имя нового друга.
        :return: True, если друг успешно добавлен.

        >>> account = FacebookAccount("user123", 0, True)
        >>> account.add_friend("friend456")
        friend456 добавлен в друзья.
        True
        """
        if not self.is_active:
            print("Невозможно добавить друга: аккаунт неактивен.")
            return False
        self.friends_count += 1
        print(f"{friend_name} добавлен в друзья.")
        return True

    def deactivate(self) -> None:
        """
        Деактивировать аккаунт.

        :return: None

        >>> account = FacebookAccount("user123", 5, True)
        >>> account.deactivate()
        Аккаунт деактивирован.
        """
        self.is_active = False
        print("Аккаунт деактивирован.")

    def post_status(self, status: str) -> bool:
        """
        Опубликовать статус.

        :param status: Текст статуса.
        :return: True, если статус опубликован успешно.

        >>> account = FacebookAccount("user123", 5, True)
        >>> account.post_status("Всем привет , я Абдулла и  я учусь в Политехе!")
        Статус опубликован: Всем привет , я Абдулла и  я учусь в Политехе!
        True
        """
        if not self.is_active:
            print("Невозможно опубликовать статус: аккаунт неактивен.")
            return False
        print(f"Статус опубликован: {status}")
        return True

table = Table("Железо ", "Черный", 4)
print(table.color)  # brown
table.paint("Белый")
print(table.color)  # white
table.extend(2.0)
print("\n")# Площадь стола увеличена на 2.0 м²
print("*"*20)
print("\n")
tree = Tree("Елка", 15, 7.0)
print("Тип дерева :" ,tree.species )
print("Возраст : ",tree.age, "лет.")  # 15
tree.grow(5)
print("Дерево выросло 5 лет и ему стало  ",tree.age , "лет.")  # 20
print("Высота : ",tree.height)  # 9.5
tree.cut()  # Дерево срублено.
print("\n")
print("*"*20)
print("\n")

account = FacebookAccount("user123", 5, True)
account.add_friend("friend456")  # friend456 добавлен в друзья.
account.post_status("Всем привет , я Абдулла и  я учусь в Политехе!")  # Статус опубликован: Hello, world!
account.deactivate()  # Аккаунт деактивирован.
account.add_friend("friend789")  # Невозможно добавить друга: аккаунт неактивен.
