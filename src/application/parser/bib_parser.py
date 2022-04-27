from src.application.auxiliar_models.base_file import BaseFile
from src.application.interfaces.parser import Parser
from src.domain.models.article import Article
from typing import List
import bibtexparser
import json


class BibParser(Parser):

    def __init__(self):
        super().__init__(extension='bib')

    def transform_unique_file_in_articles(self, file: BaseFile, article_base: str) -> List[Article]:

        with open(f"../archives"
                  f"/{file.__getattribute__('directory')}"
                  f"/{file.__getattribute__('article_base')}"
                  f"/{str(file.__getattribute__('number'))}"
                  f".{self.extension}",
                  encoding="utf8") as file:
            bib_archive = bibtexparser.load(file).entries_dict
            json_archive = json.loads(json.dumps(bib_archive, indent=False))

        articles = self.get_articles_list(json_archive, article_base)

        return articles

    def get_articles_list(self, json_archive: dict, article_base: str) -> List[Article]:
        articles = []

        for index in json_archive:
            article = self.article_mapper.json_to_domain_article(json_archive[index],
                                                                 article_base)
            if article not in articles and self.get_extra_condition(index, json_archive):
                articles.append(article)

        return articles

    def get_extra_condition(self, index: str, json_archive: dict):
        return True


class IEEEBibParser(BibParser):

    def get_extra_condition(self, index: str, json_archive: dict):
        return 'ENTRYTYPE' in json_archive[index] and json_archive[index]['ENTRYTYPE'] != 'inbook'
