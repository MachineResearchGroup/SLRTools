from src.application.auxiliar_models.dataset import Dataset
from src.application.interfaces.report_generator import ReportGenerator
from src.infra.data import data_handler
from dataclasses import dataclass
from collections import Counter
from pandas import DataFrame
import pandas as pd


@dataclass
class BasesPerYearReportGenerator(ReportGenerator):

    def __init__(self):
        self.name_report = 'article_bases_per_year_report'

    def generate_info_dataset(self, dataframe_master: DataFrame, topic: str):
        columns = ["Year", "Base", "Quantity"]
        dataset = pd.DataFrame(columns=columns)

        years = dataframe_master["year"].unique()
        bases = dataframe_master["base"].unique()

        for year in years:
            for base in bases:
                qtd_year = dataframe_master.loc[dataframe_master['year'] == year]
                qtd_year = qtd_year.loc[dataframe_master['base'] == base].count()
                dataset = dataset.append(
                    {
                        "Year": year,
                        "Base": base,
                        "Quantity": qtd_year['doi'],
                    }
                    , ignore_index=True
                )

        dataset.sort_values(by=['Year'])

        data_handler.save_dataframe(Dataset(name=f"{topic}_{self.name_report}",
                                            type='report',
                                            dataframe=dataset,
                                            extension='csv'))
