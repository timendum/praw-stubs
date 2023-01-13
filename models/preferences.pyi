import praw
from ..const import API_PATH as API_PATH
from typing import Dict, Union

class Preferences:
    def __call__(self) -> Dict[str, Union[bool, int, str]]: ...
    def __init__(self, reddit: praw.Reddit) -> None: ...
    def update(self, **preferences: Union[bool, int, str]): ...