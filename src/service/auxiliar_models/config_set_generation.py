from dataclasses import dataclass
from typing import List


@dataclass
class ConfigSetGeneration:

    topic: str
    article_base_list: List[str]
