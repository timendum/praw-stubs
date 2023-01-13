import praw
from ..base import PRAWBase as PRAWBase
from _typeshed import Incomplete
from typing import Any, Dict, Iterator

class BaseList(PRAWBase):
    CHILD_ATTRIBUTE: Incomplete
    def __init__(self, reddit: praw.Reddit, _data: Dict[str, Any]) -> None: ...
    def __contains__(self, item: Any) -> bool: ...
    def __getitem__(self, index: int) -> Any: ...
    def __iter__(self) -> Iterator[Any]: ...
    def __len__(self) -> int: ...