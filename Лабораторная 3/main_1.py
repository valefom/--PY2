class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    @property
    def name(self) -> str:
        return self.name

    @property
    def author(self) -> str:
        return self.author

    def __setattr__(self, name: str, author: str):
        raise AttributeError("Cannot modify name and author")

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name=name, author=author)
        self.pages = pages

    @property
    def pages(self) -> int:
        return self.pages

    @pages.setter
    def pages(self, pages: int) -> None:
        if not isinstance(pages, int):
            raise TypeError
        self.pages = pages



class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name=name, author=author)
        self.duration = duration

    @property
    def duration(self) -> float:
        return self.duration

    @duration.setter
    def duration(self, duration: float) -> None:
        if not isinstance(duration, float):
            raise TypeError
        self.duration = duration
