import praw
from ....const import API_PATH as API_PATH
from typing import Optional, Union

class ReplyableMixin:
    def reply(self, body: str) -> Optional[Union['praw.models.Comment', 'praw.models.Message']]: ...
