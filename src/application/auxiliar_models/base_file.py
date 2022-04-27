from dataclasses import dataclass


@dataclass
class BaseFile:
    directory: str
    article_base: str
    number: int
    extension: str
