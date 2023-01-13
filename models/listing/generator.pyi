import praw
from ..base import PRAWBase as PRAWBase
from .listing import FlairListing as FlairListing, ModNoteListing as ModNoteListing
from _typeshed import Incomplete
from typing import Any, Dict, Iterator, Optional, Union

class ListingGenerator(PRAWBase, Iterator):
    limit: Incomplete
    params: Incomplete
    url: Incomplete
    yielded: int
    def __init__(self, reddit: praw.Reddit, url: str, limit: int = ..., params: Optional[Dict[str, Union[str, int]]] = ...) -> None: ...
    def __iter__(self) -> Iterator[Any]: ...
    def __next__(self) -> Any: ...
