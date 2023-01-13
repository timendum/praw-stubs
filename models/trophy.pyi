import praw
from .base import PRAWBase as PRAWBase
from typing import Any, Dict, Union

class Trophy(PRAWBase):
    def __init__(self, reddit: praw.Reddit, _data: Dict[str, Any]) -> None: ...
    def __eq__(self, other: Union['Trophy', Any]) -> bool: ...
