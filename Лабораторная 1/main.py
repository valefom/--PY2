import doctest


# TODO Написать 3 класса с документацией и аннотацией типов
class Car:
    def __init__(self, model: str, number: int):
        """
                Creation of ClassName1
                :param model: car model
                :param number: car number

                :raise TypeError Wrong type
                Примеры:
                >>> car = Car('BMW', 123)
        """
        if not isinstance(model, str):  # проверяем, что прочитанные страницы типа int
            raise TypeError("model should be of type str")  # вызываем ошибку
        if not isinstance(number, int):  # проверяем, что прочитанные страницы типа int
            raise TypeError("number should be of type int")  # вызываем ошибку
        self.model = model
        self.attr2 = number

    def change_model(self, new_model: str) -> None:
        """
        Method changes model

        :param new_model: New value of model
        :raise TypeError Wrong type
        """
        if not isinstance(new_model, str):  # проверяем, что прочитанные страницы типа str
            raise TypeError("New model should be of type str")  # вызываем ошибку

        # и только после всех проверок
        self.model = new_model

    def change_number(self, new_number: int) -> None:
        """
        Method changes number

        :param new_number: New value of new_number
        :raise TypeError Wrong type
        """
        if not isinstance(new_number, int):  # проверяем, что прочитанные страницы типа int
            raise TypeError("New age should be of type int")  # вызываем ошибку

        # и только после всех проверок
        self.number = new_number


class Plane:
    def __init__(self, weight: float, capacity: int):
        """
                Creation of ClassName1
                :param capacity: attribute 1
                :param weight: attribute 2

                :raise TypeError Wrong type
                Примеры:
                >>> plane = Plane(300.0, 5)
        """
        if not isinstance(weight, float):  # проверяем, что прочитанные страницы типа float
            raise TypeError("attr1 should be of type float")  # вызываем ошибку
        if not isinstance(capacity, int):  # проверяем, что прочитанные страницы типа int
            raise TypeError("attr2 should be of type int")  # вызываем ошибку
        self.weight = weight
        self.capacity = capacity

    def add_passenger(self, new_weight) -> None:
        """
            Method adds new passenger

            :param new_weight: New weight of passenger
        """
        self.capacity += 1
        self.weight += new_weight
        return

    def get_average_weight(self) -> float:
        """
        Method shows average passenger weight

        :return average weight in float format
        """
        if self.capacity == 0:  # проверяем, что прочитанные страницы типа int
            raise ValueError("capacity should be equal to 0")  # вызываем ошибку
        average_weight = float(self.weight/self.capacity)
        return average_weight


class Boat:
    def __init__(self, kind: str, holder: str):
        """
                Creation of ClassName1
                :param kind: boat type
                :param holder: boat holder

                :raise TypeError Wrong type
                Примеры:
                >>> boat = Boat("Fishing", "John Smith")
        """
        if not isinstance(kind, str):  # проверяем, что прочитанные страницы типа str
            raise TypeError("kind should be of type str")  # вызываем ошибку
        if not isinstance(holder, str):  # проверяем, что прочитанные страницы типа int
            raise TypeError("holder should be of type str")  # вызываем ошибку
        self.kind = kind
        self.holder = holder  # последняя прочитанная страница

    def change_kind(self, new_kind) -> None:
        """
        Method changes boat kind

        :param new_kind: New kind of boat
        """
        self.kind = new_kind
        return

    def change_holder(self, new_holder) -> None:
        """
        Method changes boat holder

        :param new_holder: New golder of boat
        """
        self.holder = new_holder
        return


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
