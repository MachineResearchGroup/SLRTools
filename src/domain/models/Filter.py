from dataclasses import dataclass


@dataclass
class Filter:
    type: str
    value: str
