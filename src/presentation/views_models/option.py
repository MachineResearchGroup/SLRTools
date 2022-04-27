from dataclasses import dataclass
from abc import abstractmethod


@dataclass
class Option:
    number: int
    description: str

    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def run(self):
        pass
