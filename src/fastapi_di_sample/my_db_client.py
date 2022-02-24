from time import sleep
from typing import Collection, Protocol, runtime_checkable


@runtime_checkable
class IMyDbClient(Protocol):
    def get_ok_words(self) -> Collection[str]:
        """
        Gets a colection of OK words
        """
        pass


class MyDbClient:
    def __init__(self) -> None:
        # heavy data acquisition process
        print("client init started")
        sleep(3)
        self._data = ["alice", "bob", "charlie"]
        print("client init finished")

    def get_ok_words(self) -> Collection[str]:
        return self._data
