from dataclasses import dataclass, field

from .status import Status


@dataclass
class Book:
    """
    Implementation of the entity of the book
    :ivar __title: (str) The title of the book
    :ivar __author: (str) The author of the book
    :ivar __year: (int) The year of the book's release
    """

    __title: str
    __author: str
    __year: int
    __status: Status = Status.IN_STOCK
    __id: int = field(init=False)

    def __post_init__(self):
        self.__id = id(self)

    def __str__(self):
        return (f"Book\n\tid: {self.__id}\n\ttitle: {self.__title}\n"
                f"\tauthor: {self.__author}\n\tyear: {self.__year}\n\tstatus: {self.__status.value}")

    def to_dict(self) -> dict:
        return {
            'title': self.__title,
            'author': self.__author,
            'year': self.__year,
            'status': self.__status.value,
            'id': self.__id
        }

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, var: str) -> None:
        self.__title = var

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, var: str) -> None:
        self.__author = var

    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, var: int) -> None:
        self.__year = var

    @property
    def status(self) -> str:
        return self.__status.value

    @status.setter
    def status(self, status: Status) -> None:
        self.__status = status

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, new_id: int) -> None:
        self.__id = new_id

    def change_status(self) -> None:
        """
        Change self.__status to inverse
        """

        if self.__status == Status.IN_STOCK:
            self.__status = Status.ISSUED
        else:
            self.__status = Status.IN_STOCK
