import praw
from ...util.cache import cachedproperty as cachedproperty
from .subreddit import Subreddit as Subreddit, SubredditModeration as SubredditModeration
from typing import Dict, Union

class UserSubreddit(Subreddit):
    def __init__(self, reddit: praw.Reddit, *args, **kwargs) -> None: ...
    def mod(self) -> praw.models.reddit.user_subreddit.UserSubredditModeration: ...
    def __getitem__(self, item): ...

class UserSubredditModeration(SubredditModeration):
    def update(self, **settings: Union[str, int, bool]) -> Dict[str, Union[str, int, bool]]: ...
