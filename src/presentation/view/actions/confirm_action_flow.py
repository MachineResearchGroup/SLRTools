from src.presentation.interfaces.action_flow import ActionFlow


class Confirm(ActionFlow):

    def __init__(self):
        self.title = 'Options confirmed!'

    def run(self):
        print(self.title)
