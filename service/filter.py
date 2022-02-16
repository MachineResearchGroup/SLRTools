from dataclasses import dataclass
from util import data
import pandas as pd


@dataclass
class FilterSLR:

    def __init__(self, query: str):
        self.query = query

    def __word_in_text__(self, text: str, word_list: []):
        for word in word_list:
            if isinstance(text, str) and word in text:
                return True

        return False

    def filter(self, word_list: []):
        dataframe = data.get_csv('geral', 'principal', self.query)
        rows_list = []
        articles = dataframe.T.to_dict().values()

        for article in articles:
            if (self.__word_in_text__(article['title'], word_list) or
                    self.__word_in_text__(article['abstract'], word_list) or
                    self.__word_in_text__(article['keywords'], word_list)):
                rows_list.append(article)

        if rows_list:
            return pd.DataFrame.from_dict([a for a in rows_list])

        return None
