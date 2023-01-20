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


# TODO написать класс Book
class Book:
    def __init__(self, id: int, name: str, pages: int):
        """
                Creation of ClassName1
                :param id: book id
                :param name: book name
                :param pages: book pages

                :raise TypeError Wrong type
                Примеры:
                >>> book = Book(1, 'test_name', 10)
        """
        if not isinstance(id, int):
            raise TypeError("id should be of type int")
        if not isinstance(name, str):
            raise TypeError("name should be of type str")
        if not isinstance(pages, int):
            raise TypeError("pages should be of type int")
        self.id = id
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        """
        Method returns book name
        """
        b = f'Книга {self.name}'
        return b

    def __repr__(self) -> str:
        """
        Method returns book name
        """
        ini = f'Book(id={self.id},name=\'{self.name}\',pages={self.pages})'
        return ini


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
