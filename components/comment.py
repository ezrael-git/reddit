from components.__base__ import Base

class Comment:
    """ Represents a single comment.
    Not self-serving.
    """
    def __init__(self, author: str, subreddit: str, text: str | None, url: str, **kwargs):
        super().__init__()
        self.author = author
        self.subreddit = subreddit
        self.text = text
        self.url = url
        self.upvotes = kwargs.get("upvotes", None)

    def __repr__(self):
        return f"Author: {self.author}\nSubreddit: r/{self.subreddit}\nText: {self.text}\nUpvotes: {self.upvotes}\nPermalink: {self.url}\n"