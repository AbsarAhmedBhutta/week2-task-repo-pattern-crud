from __future__ import annotations
from abc import ABC, abstractmethod
import EntityRepository
from typing import TypeVar, Dict, List, Union

T = TypeVar('T')
Key = Union[str, int]


class IUnitOfWork(ABC):
    User: EntityRepository.Interface

    @abstractmethod
    def commit(self, commit_name):
        ...

    @abstractmethod
    def rollback(self, key: Key) -> None:
        ...
