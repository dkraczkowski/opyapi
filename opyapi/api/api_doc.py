from abc import ABC
from abc import abstractmethod


class ApiDoc(ABC):
    @abstractmethod
    def to_doc(self):
        raise NotImplemented()


__all__ = ["ApiDoc"]
