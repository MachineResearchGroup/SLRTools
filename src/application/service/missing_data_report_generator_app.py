from src.application.auxiliar_models.dataset import Dataset
from src.application.interfaces.report_generator import ReportGenerator
from src.infra.data import data_handler
from dataclasses import dataclass
from pandas import DataFrame


@dataclass
class MissingDataReportGenerator(ReportGenerator):

    def __init__(self):
        self.name_report = 'missing_data_report'

    def generate_info_dataset(self, dataframe_master: DataFrame, topic: str):
        info = dataframe_master.isnull().sum()

        data_handler.save_dataframe(Dataset(name=f"{topic}_{self.name_report}",
                                            type='report',
                                            dataframe=info,
                                            extension='csv'))
