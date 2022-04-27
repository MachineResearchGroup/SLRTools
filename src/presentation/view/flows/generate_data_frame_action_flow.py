from src.infra.data import data_handler
from src.presentation.views_models.actionOption import ActionOption
from src.service.auxiliar_models.config_set_generation import ConfigSetGeneration
from src.presentation.views_models.to_mark_option import ToMarkOption
from src.presentation.interfaces.selection_menu import SelectionMenu
from src.presentation.view.actions.confirm_action_flow import Confirm
from src.presentation.views_models.InitOption import InitOption
from src.service.entrypoints import metadata_set_generation


class GenerateDataFrameFlow(SelectionMenu):

    def __init__(self):
        self.title = '-- Generate DataFrame'
        self.options = [ToMarkOption(1, 'acm', False, 'ACM Digital Library'),
                        ToMarkOption(2, 'ieee', False, 'IEEE Xplore'),
                        ToMarkOption(3, 'science_direct', False, 'Science Direct'),
                        ToMarkOption(4, 'mdpi', False, 'MDPI'),
                        ToMarkOption(5, 'pub_med', False, 'PubMed'),
                        ActionOption(0, 'Confirm', Confirm()),
                        ]
        super().__init__(self, self.options)

    def run(self):
        selected_article_bases = []
        topic = self.get_input_topic()

        selected_option = InitOption()

        while selected_option.__getattribute__('number') != 0:
            self.show_options()
            selected_option = self.get_selected_option()
            selected_option.run()
            if selected_option.__getattribute__('number') != 0:
                selected_article_bases.append(selected_option.__getattribute__('description'))
            print('--')

        config = ConfigSetGeneration(topic=topic,
                                     article_base_list=selected_article_bases)

        metadata_set_generation.generate_set_articles(config)

        print('Successfully generated dataset!')

    def get_input_topic(self) -> str:
        topic = input('Insert your review topic > ')

        while not data_handler.path_topic_exists(topic):
            print('Invalid topic! type again.')
            topic = input('Insert your review topic > ')

        return topic