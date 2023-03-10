import praw
from ....util.cache import cachedproperty as cachedproperty
from ..generator import ListingGenerator as ListingGenerator
from .base import BaseListingMixin as BaseListingMixin
from .gilded import GildedListingMixin as GildedListingMixin
from typing import Dict, Iterator, Union

class SubListing(BaseListingMixin):
    def __init__(self, reddit: praw.Reddit, base_path: str, subpath: str) -> None: ...

class RedditorListingMixin(BaseListingMixin, GildedListingMixin):
    def comments(self) -> SubListing: ...
    def submissions(self) -> SubListing: ...
    def downvoted(self, **generator_kwargs: Union[str, int, Dict[str, str]]) -> Iterator[Union['praw.models.Comment', 'praw.models.Submission']]: ...
    def gildings(self, **generator_kwargs: Union[str, int, Dict[str, str]]) -> Iterator[Union['praw.models.Comment', 'praw.models.Submission']]: ...
    def hidden(self, **generator_kwargs: Union[str, int, Dict[str, str]]) -> Iterator[Union['praw.models.Comment', 'praw.models.Submission']]: ...
    def saved(self, **generator_kwargs: Union[str, int, Dict[str, str]]) -> Iterator[Union['praw.models.Comment', 'praw.models.Submission']]: ...
    def upvoted(self, **generator_kwargs: Union[str, int, Dict[str, str]]) -> Iterator[Union['praw.models.Comment', 'praw.models.Submission']]: ...
