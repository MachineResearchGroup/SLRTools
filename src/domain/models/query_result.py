from src.domain.models.search_string import SearchString
from src.domain.models.Filter import Filter
from dataclasses import dataclass
from typing import List


@dataclass
class QueryResult:
    search_string: SearchString
    article_base_results = dict
    filters = List[Filter]

