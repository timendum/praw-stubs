import praw
from ....util.cache import cachedproperty as cachedproperty
from ...base import PRAWBase as PRAWBase
from ..generator import ListingGenerator as ListingGenerator
from .base import BaseListingMixin as BaseListingMixin
from .gilded import GildedListingMixin as GildedListingMixin
from .rising import RisingListingMixin as RisingListingMixin
from _typeshed import Incomplete
from typing import Any, Dict, Iterator, Optional, Union

class CommentHelper(PRAWBase):
    subreddit: Incomplete
    def __init__(self, subreddit: praw.models.Subreddit) -> None: ...
    def __call__(self, **generator_kwargs: Union[str, int, Dict[str, str]]) -> Iterator['praw.models.Comment']: ...

class SubredditListingMixin(BaseListingMixin, GildedListingMixin, RisingListingMixin):
    def comments(self) -> CommentHelper: ...
    def __init__(self, reddit: praw.Reddit, _data: Optional[Dict[str, Any]]) -> None: ...
