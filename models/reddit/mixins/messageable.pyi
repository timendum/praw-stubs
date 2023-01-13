import praw
from ....const import API_PATH as API_PATH
from typing import Optional, Union

class MessageableMixin:
    def message(self, *, from_subreddit: Optional[Union['praw.models.Subreddit', str]] = ..., message: str, subject: str): ...
