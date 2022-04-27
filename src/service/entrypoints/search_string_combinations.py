from src.application.service.combination_string_app import CombinationString
from src.domain.models.query_result import QueryResult
from typing import List


def generate_search_string_combinations(blocks: List[List[str]]) -> List[QueryResult]:
    search_string = CombinationString().generate_combinations(blocks)
    queries = []

    for string in search_string:
        queries.append(QueryResult(string))

    return queries


