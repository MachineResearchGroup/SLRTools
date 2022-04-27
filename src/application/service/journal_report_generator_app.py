from src.application.auxiliar_models.dataset import Dataset
from src.application.interfaces.report_generator import ReportGenerator
from src.infra.data import data_handler
from dataclasses import dataclass
from collections import Counter
from pandas import DataFrame
import pandas as pd


@dataclass
class JournalReportGenerator(ReportGenerator):

    def __init__(self):
        self.name_report = 'journal_report'

    def generate_info_dataset(self, dataframe_master: DataFrame, topic: str):
        columns = ["Journal", "Quantity"]

        dataset = pd.DataFrame(columns=columns)

        types = dataframe_master["sourceTitle"].unique()

        for tp in types:
            qtd = dataframe_master.loc[dataframe_master["sourceTitle"] == tp].count()
            dataset = dataset.append(
                {
                    "Journal": tp,
                    "Quantity": qtd['doi'],
                }
                , ignore_index=True
            )

        dataset.sort_values(by=['Quantity'], ascending=False)

        data_handler.save_dataframe(Dataset(name=f"{topic}_{self.name_report}",
                                            type='report',
                                            dataframe=dataset,
                                            extension='csv'))

    def keywords_report(self):
        type_report = 'keyword_report'

        list_keys = []

        keys = [key.split(";") for key in self.dataframe_master['keywords'] if isinstance(key, str)]
        for k in keys:
            for word in k:
                if word != '':
                    word = word if word[0] != ' ' else word[1:]
                    word = word.lower()
                    list_keys.append(word)

        count = Counter(list_keys)

        dataset = pd.DataFrame.from_dict(count, orient='index').reset_index()
        dataset = dataset.rename(columns={'index': 'word', 0: 'weight'})
        dataset = dataset[['weight', 'word']]
        dataset.sort_values(by=['weight'], ascending=False)
        dataset = dataset.head(30)

        data_handler.save_dataframe(Dataset(name=f"{self.topic}_{type_report}",
                                            type='report',
                                            dataframe=dataset,
                                            extension='csv'))
