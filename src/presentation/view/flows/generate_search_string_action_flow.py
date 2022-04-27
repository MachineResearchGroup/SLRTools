from src.application.interfaces.search_string_base import SearchStringBase
from src.presentation.interfaces.action import Action


class GenerateSearchStringFlow(Action):

    def __init__(self, search_string_base: SearchStringBase):
        self.search_string_base = search_string_base
        self.search_string = ''

    def run(self):
        self.search_string_base.__setattr__('string', self.search_string)
        self.search_string_base.make_string('ola')
        print(self.search_string_base.__getattribute__('string'))
