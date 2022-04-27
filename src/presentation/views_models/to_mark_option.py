from src.presentation.views_models.option import Option
from dataclasses import dataclass


@dataclass
class ToMarkOption(Option):

    isMarked: bool
    name: str

    def print(self):
        print(f"{self.number} - {self.name} [{'x' if self.isMarked else ' '}] ")

    def run(self):
        self.isMarked = True if not self.isMarked else False
