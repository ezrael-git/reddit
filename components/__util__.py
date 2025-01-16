from components.__base__ import Base
from components.post import Post
from components.comment import Comment

class Utility(Base):

    @staticmethod
    def make_post(_post: dict) -> Post:
        data = _post["data"]
        subreddit = data['subreddit']
        body = data.get('selftext', None)
        author = data.get('author', None)
        title = data.get('title', None)
        url = Utility.BASE_URL + data['permalink']
        upvotes = data['score']
        attachments = []
        
        post = Post(title, body, subreddit, author, url, upvotes=upvotes, attachments=attachments)
        return post
    
    @staticmethod
    def make_comment(_comment: dict) -> Comment:
        data = _comment["data"]
        author = data["author"]
        text = data.get("body", None)
        subreddit = data["subreddit"]
        url = Utility.BASE_URL + data["permalink"]
        upvotes = data['score']

        comment = Comment(author, subreddit, text, url, upvotes=upvotes)
        return comment