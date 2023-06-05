from abc import ABC, abstractmethod
from typing import TypeVar, Dict, List, Union, Generic

T = TypeVar('T')
Key = Union[str, int]


class Interface(ABC, Generic[T]):
    @abstractmethod
    def add(self, key: Key, item: T) -> None:
        pass

    @abstractmethod
    def get(self) -> Dict[Key, List[T]]:
        pass

    @abstractmethod
    def update(self, key: Key, updated_item: T) -> None:
        pass

    @abstractmethod
    def delete(self, key: Key) -> None:
        pass

    @abstractmethod
    def search(self, key: Key) -> Dict[Key, List[T]]:
        pass


