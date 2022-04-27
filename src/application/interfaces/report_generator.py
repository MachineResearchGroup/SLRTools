from abc import ABC, abstractmethod
from dataclasses import dataclass
from pandas import DataFrame


@dataclass
class ReportGenerator(ABC):

    name_report: str

    @abstractmethod
    def generate_info_dataset(self, dataframe_master: DataFrame, topic: str):
        pass
