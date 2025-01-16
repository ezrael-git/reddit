from subreddit import Subreddit
from components.post import Post
from components.user import User

class Reddit:
    def __init__(self):
        pass

    def get_user(self, username: str) -> User:
        return User(username)
    
    def get_subreddit(self, name: str) -> Subreddit:
        return Subreddit(name)