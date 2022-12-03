import doctest


# TODO Написать 3 класса с документацией и аннотацией типов
class ClassName1:
    def __init__(self, attr1: str, attr2: int):
        """
                Creation of ClassName1
                :param attr1: attribute 1
                :param attr2: attribute 2

                :raise TypeError Wrong type
                Примеры:
                >>> cn = ClassName1('ab', 0)
        """
        if not isinstance(attr1, str):  # проверяем, что прочитанные страницы типа int
            raise TypeError("attr1 should be of type str")  # вызываем ошибку
        if not isinstance(attr2, int):  # проверяем, что прочитанные страницы типа int
            raise TypeError("attr2 should be of type int")  # вызываем ошибку
        self.attr1 = attr1
        self.attr2 = attr2  # последняя прочитанная страница

    def changeAttr1(self, new_attr1: str) -> None:
        """
        Method changes attr1

        :param new_attr1: New value of attr1
        :raise TypeError Wrong type
        """
        if not isinstance(new_attr1, str):  # проверяем, что прочитанные страницы типа int
            raise TypeError("New attr1 should be of type str")  # вызываем ошибку

        # и только после всех проверок
        self.attr1 = new_attr1

    def changeAttr2(self, new_attr2: int) -> None:
        """
        Method changes attr2

        :param new_attr2: New value of attr2
        :raise TypeError Wrong type
        """
        if not isinstance(new_attr2, int):  # проверяем, что прочитанные страницы типа int
            raise TypeError("New age should be of type int")  # вызываем ошибку

        # и только после всех проверок
        self.attr2 = new_attr2


class ClassName2:
    def __init__(self, attr1: float, attr2: int):
        """
                Creation of ClassName1
                :param attr1: attribute 1
                :param attr2: attribute 2

                :raise TypeError Wrong type
                Примеры:
                >>> cn = ClassName2(1.23, 0)
        """
        if not isinstance(attr1, float):  # проверяем, что прочитанные страницы типа int
            raise TypeError("attr1 should be of type float")  # вызываем ошибку
        if not isinstance(attr2, int):  # проверяем, что прочитанные страницы типа int
            raise TypeError("attr2 should be of type int")  # вызываем ошибку
        self.attr1 = attr1
        self.attr2 = attr2  # последняя прочитанная страница

    def attr1ToString(self) -> str:
        """
        Method converts attr1 to String

        :return attr1 in string format
        """
        return str(self.attr1)

    def attr2ToString(self) -> str:
        """
        Method converts attr2 to String

        :return attr2 in string format
        """
        return str(self.attr2)


class ClassName3:
    def __init__(self, attr1: float, attr2: int):
        """
                Creation of ClassName1
                :param attr1: attribute 1
                :param attr2: attribute 2

                :raise TypeError Wrong type
                Примеры:
                >>> cn = ClassName3(1.23, 0)
        """
        if not isinstance(attr1, float):  # проверяем, что прочитанные страницы типа int
            raise TypeError("attr1 should be of type float")  # вызываем ошибку
        if not isinstance(attr2, int):  # проверяем, что прочитанные страницы типа int
            raise TypeError("attr2 should be of type int")  # вызываем ошибку
        self.attr1 = attr1
        self.attr2 = attr2  # последняя прочитанная страница

    def getSum(self) -> float:
        """
        Method returns sum of attr1 and attr2

        :return sum of attr1 and attr2
        """
        return float(self.attr1 + self.attr2)

    def getDiff(self) -> float:
        """
        Method gets difference between attr1 and attr2

        :return difference between attr1 and attr2
        """
        return abs(self.attr1 - self.attr2)


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
