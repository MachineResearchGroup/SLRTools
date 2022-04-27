from src.presentation.views_models.option import Option
from dataclasses import dataclass


@dataclass
class InitOption(Option):

    def __init__(self):
        self.number = -1

    def run(self):
        pass
