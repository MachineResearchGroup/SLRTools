from src.presentation.view.flows.generate_search_string_action_flow import GenerateSearchStringFlow
from src.application.auxiliar_models.ieee_search_string_base import IEEESearchStringBase
from src.application.auxiliar_models.acm_search_string_base import ACMSearchStringBase
from src.presentation.interfaces.selection_menu import SelectionMenu
from src.presentation.views_models.InitOption import InitOption
from src.presentation.views_models.actionOption import ActionOption
from src.presentation.view.actions.return_action_flow import Return


class GenerateSearchStringMenu(SelectionMenu):

    def __init__(self):
        self.title = '-- Generate Search Strings'
        self.options = [ActionOption(1, 'ACM Digital Library', GenerateSearchStringFlow(ACMSearchStringBase())),
                        ActionOption(2, 'IEEE Xplore', GenerateSearchStringFlow(IEEESearchStringBase())),
                        ActionOption(0, 'Return', Return()),
                        ]
        super().__init__(self, self.options)

    def run(self):
        string = input('Insert your string > ')

        selected_option = InitOption()

        while selected_option.__getattribute__('number') != 0:
            self.show_options()
            selected_option = self.get_selected_option()
            selected_option.__getattribute__('action').__setattr__('search_string', string)

            selected_option.run()
            print('--')

        print('Successfully generated dataset!')

