from abc import ABC, abstractmethod


class Section(ABC):
    @abstractmethod
    def describe(self):
        raise NotImplementedError
