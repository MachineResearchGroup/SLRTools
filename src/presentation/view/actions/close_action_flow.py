from src.presentation.interfaces.action_flow import ActionFlow


class Close(ActionFlow):

    def __init__(self):
        self.title = 'Application closed!'

    def run(self):
        print(self.title)
