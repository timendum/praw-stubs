import praw
from .editable import EditableMixin as EditableMixin
from .fullname import FullnameMixin as FullnameMixin
from .gildable import GildableMixin as GildableMixin
from .inboxable import InboxableMixin as InboxableMixin
from .inboxtoggleable import InboxToggleableMixin as InboxToggleableMixin
from .messageable import MessageableMixin as MessageableMixin
from .modnote import ModNoteMixin as ModNoteMixin
from .replyable import ReplyableMixin as ReplyableMixin
from .reportable import ReportableMixin as ReportableMixin
from .savable import SavableMixin as SavableMixin
from .votable import VotableMixin as VotableMixin
from _typeshed import Incomplete
from typing import Optional

class ThingModerationMixin(ModNoteMixin):
    REMOVAL_MESSAGE_API: Incomplete
    def approve(self) -> None: ...
    def distinguish(self, *, how: str = ..., sticky: bool = ...): ...
    def ignore_reports(self) -> None: ...
    def lock(self) -> None: ...
    def remove(self, *, mod_note: str = ..., spam: bool = ..., reason_id: Optional[str] = ...): ...
    def send_removal_message(self, *, message: str, title: str = ..., type: str = ...) -> Optional['praw.models.Comment']: ...
    def undistinguish(self) -> None: ...
    def unignore_reports(self) -> None: ...
    def unlock(self) -> None: ...

class UserContentMixin(EditableMixin, GildableMixin, InboxToggleableMixin, ReplyableMixin, ReportableMixin, SavableMixin, VotableMixin):
    id: str
    permalink: str
    fullname: str
    author: None | 'praw.models.Redditor'
    subreddit: 'praw.models.Subreddit'
    @property
    def mod(self) -> 'praw.models.reddit.mixins.ThingModerationMixin': ...
    
