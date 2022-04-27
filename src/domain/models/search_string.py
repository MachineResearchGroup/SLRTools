from src.domain.models.block_string import BlockString
from dataclasses import dataclass
from typing import List


@dataclass
class SearchString:
    blocks: List[BlockString]

    def get_string(self):
        string = ''
        count_blocks = 0

        for block in self.blocks:
            if count_blocks == 0:
                string += '('
                count_blocks += count_blocks
            else:
                string = string + 'AND ('

            for term in block.__getattribute__('terms'):
                string += term + ' OR '

            string += ')'

        return string

    def __eq__(self, other):
        return self.blocks == other.blocks



