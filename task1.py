class Table:
    def __init__(self, material: str, color: str, legs: int) -> None:
        """
        Инициализация объекта Стол.

        :param material: Материал стола.
        :param color: Цвет стола.
        :param legs: Количество ножек.
        :raises ValueError: Если количество ножек <= 0 или типы данных неверные.
        """
        if not isinstance(material, str) or not isinstance(color, str):
            raise TypeError("Материал и цвет стола должны быть строками.")
        if not isinstance(legs, int):
            raise TypeError("Количество ножек должно быть целым числом.")
        if legs <= 0:
            raise ValueError("Количество ножек должно быть больше 0.")

        self.material = material
        self.color = color
        self.legs = legs

    def paint(self, new_color: str) -> None:
        if not isinstance(new_color, str):
            raise TypeError("Цвет должен быть строкой.")
        self.color = new_color

    def extend(self, extra_space: float) -> None:
        if not isinstance(extra_space, (int, float)):
            raise TypeError("Дополнительная площадь должна быть числом.")
        if extra_space <= 0:
            raise ValueError("Дополнительная площадь должна быть больше 0.")
        print(f"Площадь стола увеличена на {extra_space} м²")


class Tree:
    def __init__(self, species: str, age: int, height: float) -> None:
        if not isinstance(species, str):
            raise TypeError("Вид дерева должен быть строкой.")
        if not isinstance(age, int) or not isinstance(height, (int, float)):
            raise TypeError("Возраст должен быть целым числом, а высота числом.")
        if age < 0:
            raise ValueError("Возраст дерева не может быть отрицательным.")
        if height <= 0:
            raise ValueError("Высота дерева должна быть больше 0.")

        self.species = species
        self.age = age
        self.height = height

    def grow(self, years: int) -> None:
        if not isinstance(years, int):
            raise TypeError("Количество лет должно быть целым числом.")
        if years <= 0:
            raise ValueError("Количество лет должно быть больше 0.")
        self.age += years
        self.height += years * 0.5

    def cut(self) -> None:
        print("Дерево срублено.")


class FacebookAccount:
    def __init__(self, username: str, friends_count: int, is_active: bool) -> None:
        if not isinstance(username, str):
            raise TypeError("Имя пользователя должно быть строкой.")
        if not isinstance(friends_count, int) or friends_count < 0:
            raise ValueError("Количество друзей должно быть неотрицательным целым числом.")
        if not isinstance(is_active, bool):
            raise TypeError("Параметр is_active должен быть булевым значением.")

        self.username = username
        self.friends_count = friends_count
        self.is_active = is_active

    def add_friend(self, friend_name: str) -> bool:
        if not isinstance(friend_name, str):
            raise TypeError("Имя друга должно быть строкой.")
        if not self.is_active:
            print("Невозможно добавить друга: аккаунт неактивен.")
            return False
        self.friends_count += 1
        print(f"{friend_name} добавлен в друзья.")
        return True

    def deactivate(self) -> None:
        self.is_active = False
        print("Аккаунт деактивирован.")

    def post_status(self, status: str) -> bool:
        if not isinstance(status, str):
            raise TypeError("Статус должен быть строкой.")
        if not self.is_active:
            print("Невозможно опубликовать статус: аккаунт неактивен.")
            return False
        print(f"Статус опубликован: {status}")
        return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()

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
