from .my_db_client import IMyDbClient


class MyService:
    def __init__(self, client: IMyDbClient) -> None:
        self._client = client

    def run(self, word: str) -> bool:
        ok_words = self._client.get_ok_words()
        return word in ok_words
