from abc import ABC
from dataclasses import dataclass


@dataclass
class Action(ABC):

    title: str

    def run(self):
        print('Not Implemented!')
