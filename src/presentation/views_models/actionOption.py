from src.presentation.interfaces.action import Action
from dataclasses import dataclass

from src.presentation.views_models.option import Option


@dataclass
class ActionOption(Option):

    action: Action

    def print(self):
        print(f"[{self.number}] - {self.description}")

    def run(self):
        self.action.run()
