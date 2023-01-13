import praw
from ....const import API_PATH as API_PATH
from typing import Union

class EditableMixin:
    def delete(self) -> None: ...
    def edit(self, body: str) -> Union['praw.models.Comment', 'praw.models.Submission']: ...
