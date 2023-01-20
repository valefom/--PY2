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


# TODO написать класс Library
# TODO написать класс Book
class Library:
    def __init__(self, books=[]):
        """
                Creation of ClassName1
                :param id: book id
                :param name: book name
                :param pages: book pages

                :raise TypeError Wrong type
                Примеры:
                >>> lib = Library([])
        """
        self.books = books

    def get_next_book_id(self) -> int:
        """
        Method returns book name
        """
        if not self.books:
            return 1
        return len(self.books) + 1

    def get_index_by_book_id(self, id) -> int:
        """
        Method returns book name
        """
        for i, b in enumerate(self.books):
            if b.id == id:
                return i
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
