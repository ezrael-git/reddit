from components.__base__ import Base
from components.__util__ import Utility

class User(Base):
    """ Self-serving. Represents a Reddit user.
    """
    def __init__(self, username: str):
        super().__init__()
        self.username = username

        self._fetch_data()

    def _fetch_data(self) -> None:
        _json = self._get_json(f"{User.BASE_URL}/user/{self.username}/")
        comments = []
        for _comment in _json["data"]["children"]:
            comment = Utility.make_comment(_comment)
            comments.append(comment)
        self.comments = comments