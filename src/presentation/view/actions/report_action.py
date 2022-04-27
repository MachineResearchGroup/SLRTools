from src.service.entrypoints.informations_dataset_generation import generate_reports
from src.application.interfaces.report_generator import ReportGenerator
from src.presentation.interfaces.action import Action
from dataclasses import dataclass


@dataclass
class ReportAction(Action):

    def __init__(self, report: ReportGenerator):
        self.report = report
        self.topic = ''
        self.title = ''

    def run(self):
        generate_reports(self.topic, self.report)
