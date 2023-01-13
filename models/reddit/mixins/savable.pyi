from ....const import API_PATH as API_PATH
from typing import Optional

class SavableMixin:
    def save(self, *, category: Optional[str] = ...): ...
    def unsave(self) -> None: ...
