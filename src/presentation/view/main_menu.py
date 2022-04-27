from src.presentation.view.menus.generate_search_strings_menu import GenerateSearchStringMenu
from src.presentation.view.menus.generate_dataframe_menu import GenerateDataFrameMenu
from src.presentation.interfaces.selection_menu import SelectionMenu
from src.presentation.views_models.actionOption import ActionOption
from src.presentation.view.actions.close_action_flow import Close
from src.presentation.views_models.InitOption import InitOption


class MainMenu(SelectionMenu):

    def __init__(self):
        self.options = [ActionOption(1, 'Generate dataset from the Articles metadata', GenerateDataFrameMenu()),
                        ActionOption(2, 'Generating search strings for databases', GenerateSearchStringMenu()),
                        ActionOption(0, 'Exit', Close()),
                        ]
        super().__init__(self, self.options)

    def run(self):
        print(' _____  __     _____  _____            _      \n'
              '|   __||  |   | __  ||_   _| ___  ___ | | ___ \n'
              '|__   ||  |__ |    -|  | |  | . || . || ||_ -|\n'
              '|_____||_____||__|__|  |_|  |___||___||_||___|\n'
              '\n'
              'Tool with useful features for conducting a systematic review of the literature.\n')
        selected_option = InitOption()

        while selected_option.__getattribute__('number') != 0:
            self.show_options()
            selected_option = self.get_selected_option()
            selected_option.run()
            print('--')
