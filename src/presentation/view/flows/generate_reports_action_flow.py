from src.application.service.bases_per_year_report_generator_app import BasesPerYearReportGenerator
from src.application.service.journal_report_generator_app import JournalReportGenerator
from src.application.service.keywords_report_generator_app import KeywordsReportGenerator
from src.application.service.missing_data_report_generator_app import MissingDataReportGenerator
from src.infra.data import data_handler
from src.presentation.view.actions.report_action import ReportAction
from src.presentation.views_models.actionOption import ActionOption
from src.presentation.interfaces.selection_menu import SelectionMenu
from src.presentation.view.actions.confirm_action_flow import Confirm
from src.presentation.views_models.InitOption import InitOption


class GenerateReportsFlow(SelectionMenu):

    def __init__(self):
        self.title = '-- Generate Reports'
        self.options = [ActionOption(1, 'Missing data', ReportAction(MissingDataReportGenerator())),
                        ActionOption(2, 'Bases per year', ReportAction(BasesPerYearReportGenerator())),
                        ActionOption(3, 'Journals', ReportAction(JournalReportGenerator())),
                        ActionOption(4, 'Keywords', ReportAction(KeywordsReportGenerator())),
                        ActionOption(0, 'Confirm', Confirm()),
                        ]
        super().__init__(self, self.options)

    def run(self):
        topic = self.get_input_topic()

        selected_option = InitOption()

        while selected_option.__getattribute__('number') != 0:
            self.show_options()
            selected_option = self.get_selected_option()

            if selected_option.__getattribute__('number') != 0:
                selected_option.action.__setattr__('topic', topic)

            selected_option.run()
            print('--')

        print('Successfully generated report!')

    def get_input_topic(self) -> str:
        topic = input('Insert your review topic > ')

        while not data_handler.path_topic_exists(topic):
            print('Invalid topic! type again.')
            topic = input('Insert your review topic > ')

        return topic
