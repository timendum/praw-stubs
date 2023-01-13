from .exceptions import ClientException as ClientException
from _typeshed import Incomplete
from typing import Optional

class _NotSet:
    def __bool__(self) -> bool: ...
    __nonzero__: Incomplete

class Config:
    CONFIG: Incomplete
    CONFIG_NOT_SET: Incomplete
    LOCK: Incomplete
    INTERPOLATION_LEVEL: Incomplete
    @property
    def short_url(self) -> str: ...
    custom: Incomplete
    client_id: Incomplete
    reddit_url: Incomplete
    password: Incomplete
    def __init__(self, site_name: str, config_interpolation: Optional[str] = ..., **settings: str) -> None: ...
