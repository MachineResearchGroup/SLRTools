from abc import ABC, abstractmethod
from dataclasses import dataclass


class SearchStringBase(ABC):

    def __init__(self, string: str = ''):
        self.string = string

    @abstractmethod
    def make_string(self, search_string: str):
        pass

    def __repr__(self):
        return self.string
