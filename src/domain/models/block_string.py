from dataclasses import dataclass
from typing import List


@dataclass
class BlockString:
    terms: List[str]

    def __eq__(self, other):
        return self.terms == other.terms
