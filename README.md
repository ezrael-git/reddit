# reddit.py
A barebones, synchronous Reddit wrapper. No need for an API key.
Can be used for scraping.

## Installation
Assuming you have Python and git bash installed.
Run the following commands:
```
git clone https://github.com/ezrael-git/mass-chatbot
pip install requests
```

## Examples
```
from reddit import Reddit
reddit = Reddit()

# get posts in r/cats
sub = reddit.get_subreddit('cats')
sub.get_posts()

# sort by top
sub.get_posts(sorting='top')

# get user
user = reddit.get_user('xyz')

# get user comments
user.comments
```

Feel free to contribute!
