import datetime
import hashlib
from dataclasses import dataclass, field

from status import Status


@dataclass
class Book:
    __title: str
    __author: str
    __year: int
    __status: Status = Status.IN_STOCK
    __id: int = field(init=False)

    def __post_init__(self):
        hash_string = f"{self.__title}{self.__author}{self.__year}{self.__status}{datetime.datetime.now()}"
        self.__id = int(hashlib.sha256(hash_string.encode()).hexdigest(), 16)

    def __str__(self):
        return (f"Book\n\tid: {self.__id}\n\ttitle: {self.__title}\n"
                f"\tauthor: {self.__author}\n\tyear: {self.__year}\n\tstatus: {self.__status.value}")

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

    @property
    def id(self) -> int:
        return self.__id

    def change_status(self) -> None:
        if self.__status == Status.IN_STOCK:
            self.__status = Status.ISSUED
        else:
            self.__status = Status.IN_STOCK
