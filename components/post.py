from components.__base__ import Base

class Post(Base):
    """ Represents a Reddit post. Not self-serving.
    """
    def __init__(self, title: str | None, body: str | None, subreddit: str | None, author: str | None, url: str, **kwargs):
        super().__init__()
        self.title = title
        self.body = body
        self.subreddit = subreddit
        self.author = author
        self.url = url
        self.upvotes = kwargs.get("upvotes", None)
        self.attachments = kwargs.get("attachments", [])
        self.sorting = kwargs.get("sorting", None)
        if self.sorting and not (self.sorting in ["new", "hot", "top"]):
            raise Exception(f"Invalid sorting: {self.sorting}")
        
    def __repr__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nSubreddit: r/{self.subreddit}\nBody: {self.body}\nUpvotes: {self.upvotes}\nPermalink: {self.url}\n"