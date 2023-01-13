import praw
from ...const import API_PATH as API_PATH
from ..base import PRAWBase as PRAWBase
from _typeshed import Incomplete
from typing import Any, Dict, List, Union

class MoreComments(PRAWBase):
    count: Incomplete
    children: Incomplete
    submission: Incomplete
    def __init__(self, reddit: praw.Reddit, _data: Dict[str, Any]) -> None: ...
    def __eq__(self, other: Union[str, 'MoreComments']) -> bool: ...
    def __lt__(self, other: MoreComments) -> bool: ...
    def comments(self, *, update: bool = ...) -> List['praw.models.Comment']: ...
