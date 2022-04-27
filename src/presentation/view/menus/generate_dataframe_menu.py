from src.presentation.view.flows.generate_path_structure_action_flow import GeneratePathStructureFlow
from src.presentation.view.flows.generate_data_frame_action_flow import GenerateDataFrameFlow
from src.presentation.interfaces.selection_menu import SelectionMenu
from src.presentation.view.flows.generate_reports_action_flow import GenerateReportsFlow
from src.presentation.views_models.actionOption import ActionOption
from src.presentation.view.actions.return_action_flow import Return


class GenerateDataFrameMenu(SelectionMenu):

    def __init__(self):
        self.title = '-- Generate DataFrame'
        self.options = [ActionOption(1, 'Generate Path Structure', GeneratePathStructureFlow()),
                        ActionOption(2, 'Generate Main DataFrame', GenerateDataFrameFlow()),
                        ActionOption(3, 'Generate Reports', GenerateReportsFlow()),
                        ActionOption(0, 'Return', Return()),
                        ]
        super().__init__(self, self.options)
