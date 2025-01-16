from components.__base__ import Base
from components.__util__ import Utility
from components.post import Post

class Subreddit(Base):
    """ Represents a subreddit.
    Self-serving.
    """
    def __init__(self, name: str):
        super().__init__()
        self.name = name
        self.link = Subreddit.BASE_URL + "/r/" + name

        _json = self._get_json(f"{self.link}/")
        self.description = _json["data"]["children"][0]["data"]["selftext"]

    


    def get_posts(self, **kwargs) -> list[Post]:
        sorting = kwargs.get("sorting", "new")
        posts = []
        _json = self._get_json(f"{self.link}/{sorting}")
        for _post in _json["data"]["children"]:
            post = Utility.make_post(_post)
            posts.append(post)

        return posts