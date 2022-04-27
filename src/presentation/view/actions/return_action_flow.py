from src.presentation.interfaces.action_flow import ActionFlow


class Return(ActionFlow):

    def __init__(self):
        self.title = 'Returning...'

    def run(self):
        print(self.title)
