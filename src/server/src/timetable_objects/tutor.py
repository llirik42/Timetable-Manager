from dataclasses import dataclass
from typing import Optional

from src.serialization.serializable import Serializable


@dataclass
class Tutor(Serializable):
    name: Optional[str]
    href: Optional[str]
    is_empty: bool = False


def empty_tutor() -> Tutor:
    return Tutor(name=None, href=None, is_empty=True)
