from src.application.interfaces.search_string_base import SearchStringBase
from dataclasses import dataclass


@dataclass
class ACMSearchStringBase(SearchStringBase):

    def make_string(self, search_string: str):
        self.string = 'oieeeee'
