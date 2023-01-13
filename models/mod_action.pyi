import praw
from .base import PRAWBase as PRAWBase
from typing import Union

class ModAction(PRAWBase):
    @property
    def mod(self) -> praw.models.Redditor: ...
    @mod.setter
    def mod(self, value: Union[str, 'praw.models.Redditor']): ...
