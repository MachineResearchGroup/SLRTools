from src.presentation.views_models.InitOption import InitOption
from src.presentation.views_models.option import Option
from src.presentation.interfaces.action import Action
from dataclasses import dataclass
from abc import ABC
from typing import List


@dataclass
class SelectionMenu(Action, ABC):

    options: List[Option]

    def show_options(self):
        for option in self.options:
            option.print()

    def run(self):
        print(self.title)
        selected_option = InitOption()

        while selected_option.__getattribute__('number') != 0:
            self.show_options()
            selected_option = self.get_selected_option()
            selected_option.run()
            print('--')

    def get_selected_option(self):
        selected_option = None
        selected_index = input('Option > ')

        while selected_option is None:
            while type(selected_index) != int and int(selected_index) > len(self.options):
                print('Invalid option! type again.')
                selected_index = input('Option > ')

            selected_option = self.get_option_by_number(int(selected_index))

        return selected_option

    def get_option_by_number(self, number: int):

        for option in self.options:
            if option.__getattribute__("number") == number:
                return option

        return None
