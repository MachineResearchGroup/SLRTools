from src.application.auxiliar_models.base_file import BaseFile
from src.application.interfaces.parser import Parser
from src.domain.models.article import Article
from typing import List


class PubMedRisParser(Parser):

    def __init__(self):
        super().__init__(extension='txt')
        self.mapping = {
            'PMID': 'start',
            'TI': 'title',
            'AB': 'abstract',
            'PT': 'ENTRYTYPE',
            'JT': 'journal',
            'AID': 'doi',
            'OT': 'keywords',
            'DP': 'year',
            'SO': 'end',
            'FAU': 'end_abstract'
        }

    def transform_unique_file_in_articles(self, file: BaseFile, article_base: str) -> List[Article]:

        article_files = self.get_article_files(file)
        articles = []

        for article_file in article_files:
            article = {}
            keywords = ''
            abstract = ''
            actual_key = ''

            for field in article_file:
                key = self.get_key_of_mapping(field)
                value = self.get_value_of_line(field)

                if key == 'abstract':
                    actual_key = 'abstract'
                if key == 'end_abstract':
                    actual_key = 'other'

                if actual_key == 'abstract':
                    abstract = abstract + ' ' + value
                    article[actual_key] = abstract

                else:
                    actual_key = 'other'

                    if key == 'keywords':
                        keywords = keywords + value.replace('*', '') + ';'
                        article[key] = keywords

                    elif key == 'doi':
                        article[key] = value.replace('[doi]', '')

                    elif key == 'year':
                        article[key] = value.split(' ')[0]

                    elif key == 'ENTRYTYPE':
                        if key not in article.keys():
                            article[key] = value

                    else:
                        article[key] = value

            articles.append(self.article_mapper.json_to_domain_article(article, article_base))

        return articles

    def get_article_files(self, file: BaseFile):
        with open(f"../archives"
                  f"/{file.__getattribute__('directory')}"
                  f"/{file.__getattribute__('article_base')}"
                  f"/{str(file.__getattribute__('number'))}"
                  f".{self.extension}",
                  'r', encoding="utf8") as file:
            aux_files = []
            article_ris = []
            for line in file:

                key = self.get_key_of_mapping(line)

                if key and key == 'end':
                    aux_files.append(article_ris)
                    article_ris = []
                elif key:
                    article_ris.append(line)

        return aux_files

    def get_key_of_mapping(self, line: str):
        if line.split('-')[0].replace(' ', '') in self.mapping.keys():
            return self.mapping.get(line.split('-')[0].replace(' ', ''))
        return None

    def get_value_of_line(self, line: str):
        return line.split('- ')[1].replace('\n', '')
