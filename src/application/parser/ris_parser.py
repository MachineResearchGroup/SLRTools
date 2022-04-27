from src.application.auxiliar_models.base_file import BaseFile
from src.application.interfaces.parser import Parser
from src.domain.models.article import Article
from typing import List
import rispy


class RisParser(Parser):

    def __init__(self):
        super().__init__(extension='ris')

    def transform_unique_file_in_articles(self, file: BaseFile, article_base: str) -> List[Article]:
        with open(f"../archives"
                  f"/{file.__getattribute__('directory')}"
                  f"/{file.__getattribute__('article_base')}"
                  f"/{str(file.__getattribute__('number'))}"
                  f".{self.extension}",
                  'r', encoding="utf8") as file:
            entries = rispy.load(file)
        return entries
