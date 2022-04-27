from src.domain.models.block_string import BlockString
from src.domain.models.search_string import SearchString
from dataclasses import dataclass
from typing import List
import itertools


@dataclass
class CombinationString:

    def generate_combinations(self, options_list: List[List[str]]) -> List[SearchString]:
        block_options = []

        for option in options_list:
            block_option = self.get_blocks_string_options(option)
            block_options.append(block_option)

        string_options = self.get_search_string_options(block_options)

        return string_options

    def get_blocks_string_options(self, terms: List[str]) -> List[BlockString]:
        blocks = []

        for l in range(0, len(terms) + 1):
            for subset in itertools.combinations(terms, l):
                if subset:
                    blocks.append(BlockString(subset))

        return blocks

    def get_search_string_options(self, blocks: List[List[BlockString]]):
        search_strings = []

        combinations = list(itertools.product(*blocks))
        for combination in combinations:

            search_string = SearchString(list(combination))

            if search_string not in search_strings:
                search_strings.append(search_string)

        return search_strings

