import json
import requests
from collections.abc import Iterable

class Base:
    BASE_URL = "https://www.reddit.com"
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    HEADERS = {"User-Agent": USER_AGENT}
    
    @staticmethod
    def type_check(_iter, type) -> None:
        """ Convenient typechecker
        """
        if not isinstance(_iter, Iterable):
            raise Exception("Argument must be iterable")
        for obj in _iter:
            if not isinstance(obj, type):
                raise Exception(f"Argument must be of type {type}, got {obj} instead")

    def _get_json(self, link: str):
        """ Get the json of a Reddit page
        """
        r = requests.get(link + ".json", headers=Base.HEADERS)
        return json.loads(r.content)